from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect


from main.decorators import logout_message_required, admin_required
from django.views.generic import FormView, View, CreateView
from .forms import LoginForm, RegisterForm, IdRecoveryForm, RecoveryPwForm
from .models import User
from ppr.models import International_Journal, Domestic_Journal
from notice.models import Notice
from django.utils.decorators import method_decorator
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse, resolve
from django.shortcuts import resolve_url
from django.contrib import messages
from django.shortcuts import get_object_or_404

from .helper import send_mail
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError


# Create your views here.
def test(request):
    context = {
        'selected': 'Test',
    }
    return render(request, 'main/test.html', context)

def home(request):
    # 캐러셀 슬라이드 내용 뽑아오기
    international_journal = International_Journal.objects.last()
    domestic_journal = Domestic_Journal.objects.last()
    notice = Notice.objects.last()

    if international_journal == None:
        international_journal = International_Journal(title="Welcome", journals="DEFAULT", issued_date="DEFAULT")
    if domestic_journal == None:
        domestic_journal = Domestic_Journal(title="Welcome", journals="DEFAULT_", issued_date="DEFAULT_")
    if notice == None:
        notice = Notice(title="Welcome", content="DEFAULT__", hits="DEFAULT__")

    context = {
        'journal': international_journal,
        'publication': domestic_journal,
        'notice': notice,
        'selected': 'Home',
    }

    return render(request, 'main/home.html', context)

# 로그인 후,
@method_decorator(logout_message_required, name='dispatch')
class LoginView(FormView):
    template_name = 'main/login.html'
    form_class = LoginForm

    #success_url = '/' # reverse_lazy("main:home") # 로그인 성공했을 때 들어가는 주소

    def form_valid(self, form):
        userid = form.cleaned_data.get("userid")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, userid=userid, password=password)

        if user is not None:
            self.request.session['userid'] = userid
            login(self.request, user)
            # holding login: SESSION_...을 이용해 로그인 유지
            remember_session = self.request.POST.get('remember_session', False)
            if remember_session:
                settings.SESSION_EXPIRE_AT_BROWSER_CLOSE = False

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # global hello
        #hello = self.request.GET.get('next')
        #if hello == '/ppr/publication/':
        #    hello += '?q=1&?page=1'
        # 하.. 방법을 못찾고 있었는데, 이 몇 줄에 너무 뿌듯하다.
        hello_next_url = self.request.GET.get('next')
        if hello_next_url == '/ppr/publication/':
            hello_next_url += '?q=1&?page=1'
        LoginView.success_url = hello_next_url
        return super().get_context_data(**kwargs)

    def get_success_url(self, **kwargs):
        # global hello
        # if hello == None:
        # hello = '/'
        # 회원 가입 후 리디렉션, next가 없음.
        if LoginView.success_url == None:
            LoginView.success_url = '/'
        return LoginView.success_url # str(hello)

def get_next(request):
    gn = request.GET['next']
    if gn == '/ppr/publication/':
        gn += '?q=1&?page=1'
    return gn

# 약관 동의 cbv 구현
# decorators.py의 'logout...'를 decorator로 사용 --> 로그인 중인 사용자 접근 금지
@method_decorator(logout_message_required, name='dispatch')
class AgreementView(View):
    # 1. agreement에 대해 False를 주고 시작 (agreement.html을 참조)
    def get(self, request, *args, **kwargs):
        request.session['agreement'] = False
        user = User.objects.get(id=1)
        user_activate = user.activate

        if(user_activate == False):
            messages.success(request, "Ask a manager to register !")
            return redirect('/')

        else:
            return render(request, 'main/agreement.html')

    # 2. 사용자에 의해 저장된 agreement가 True인지 False인지 검사
    def post(self, request, *args, **kwarg):
        user = User.objects.get(id=1)
        user_activate = user.activate
        if(user_activate == False):
            return render(request, 'main/login.html')

        # 3-1. 동의했는지 검사
        if request.POST.get('agreement1', False) and request.POST.get('agreement2', False):
            request.session['agreement'] = True
            # 동의했다면 직원 가입 or 일반 가입 검사
            if request.POST.get('sign_up') == 'sign_up':
                return redirect('main:sign_up')
            else:
                return redirect('main:sign_up')
        # 3-2. 동의하지 않았다면 다시 back
        else:
            messages.info(request, "Please agree to all the terms and conditions.")
            return redirect('.')

# 직원 회원가입
class sign_up(CreateView):
    model = User
    template_name = 'main/sign_up.html'
    form_class = RegisterForm

    def get(self, request, *args, **kwargs):
        if not request.session.get('agreement', False):
            raise PermissionDenied
        request.session['agreement'] = False
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        # 세션을 생성하여 강제적인 url 이동을 방지
        self.request.session['register_auth'] = True
        return reverse('main:register_success')
        #return '/login/?next=/'

    def form_valid(self, form):
        self.object = form.save()

        send_mail(
            '[SELab] {}, this is your verification e-mail'.format(self.object.userid),
            [self.object.email],
            html=render_to_string('main/register_email.html', {
                'user': self.object,
                'uid': urlsafe_base64_encode(force_bytes(self.object.pk)).encode().decode(),
                # ‘uid’ 부분에서 .decode(‘UTF-8’)로 디코딩을 할 시 오류가 발생 --> python3에서 이미 디코딩을 해주기에 .encode().decode()로 구현)
                'domain': self.request.META['HTTP_HOST'],
                'token': default_token_generator.make_token(self.object),
            }),
        )

        return redirect(self.get_success_url())

# 상단의 sign_up 클래스의 get_success_url 메소드와 호응하는 함수
# 세션을 생성하여 강제적인 url 이동을 방지
def register_success(request):
    if not request.session.get('register_auth', False):
        raise PermissionDenied
    request.session['register_auth'] = False

    return render(request, 'main/register_success.html')

# 토큰 값이 담긴 메일 링크를 클릭하면 계정이 활성화
def activate(request, uid64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uid64))
        current_user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist, ValidationError):
        messages.error(request, 'Mail authentication failed.')
        return redirect('main:login')

    if default_token_generator.check_token(current_user, token):
        current_user.is_active = True
        current_user.save()

        messages.info(request, 'Mail authentication is complete.\n Congratulations on your membership.')
        return redirect('main:login')

    messages.error(request, 'Failed or Already approved.')
    return redirect('main:login')

# 로그아웃 후,
def logout_view(request):
    logout(request)
    next = request.GET['next']
    if next == '/ppr/publication/':
        next += '?q=1&?page=1'
    return redirect(next)

@admin_required
def activate_sign_up(request):
    activate_value = User.objects.get(id=1).activate
    if(request.user.level == '0' or request.user.level == '1'):
        if(activate_value == False):
            admin_level_zero = User.objects.filter(level=0)
            for u in admin_level_zero:
                u.activate = True
                u.save()
        else:
            admin_level_zero = User.objects.filter(level=0)
            for u in admin_level_zero:
                u.activate = False
                u.save()

    return redirect('/')

def choose_one(request):
    return render(request, "main/choose_one.html")

# 아이디 찾기 영역
@method_decorator(logout_message_required, name='dispatch')
class IdRecoveryView(View):
    template_name = 'main/recovery_id.html'
    form = IdRecoveryForm

    def get(self, request):
        if request.method == 'GET':
            form_id = self.form(None)
        else:
            messages.success(request, "E: something problem about the form.")
            form_id = None
        return render(request, self.template_name, {'form' : form_id,})

import json
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
def ajax_find_id_view(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    result_id = User.objects.get(email=email, username=name)
    # HttpResponse를 통해 응답하고 반환되는 값이 없으면 DoesNotExist 에러를 발생
    return HttpResponse(json.dumps({"result_id": result_id.userid}, cls=DjangoJSONEncoder), content_type="application/json")

# 비밀번호 찾기 영역
# 페이지 연결 view
@method_decorator(logout_message_required, name='dispatch')
class RecoveryPwView(View):
    template_name = 'main/recovery_pw.html'
    recovery_pw = RecoveryPwForm

    def get(self, request):
        if request.method=='GET':
            form = self.recovery_pw(None)
            return render(request, self.template_name, { 'form':form, })

from .helper import email_auth_num

# 비밀번호 찾기 창에서 필드 값들을 입력한 후 Ajax 요청을 하는 view
# Ajax로 요청된 값들을 User 모델에서 찾은 후 반환된 target_user의 auth필드에 방금 구현한 인증번호 생성함수를 통해 auth_num를 저장
# 그 다음 send_mail 함수로 인증번호인 auth_num을 담은 메일을 사용자에게 발송
def ajax_find_pw_view(request):
    userid = request.POST.get('userid')
    username = request.POST.get('name')
    email = request.POST.get('email')
    target_user = User.objects.get(userid=userid, username=username, email=email)

    if target_user:
        auth_num = email_auth_num()
        target_user.auth = auth_num
        target_user.save()

        send_mail(
            '[SELab] Verification e-mail for recovering PW.',
            [email],
            html=render_to_string('main/recovery_email.html', {
                'auth_num': auth_num,
            }),
        )
    return HttpResponse(json.dumps({"result": target_user.userid}, cls=DjangoJSONEncoder), content_type = "application/json")

# 템플릿으로부터 입력된 인증번호를 확인하는 view
# 마찬가지로 Ajax로 요청된 userid와 입력된 인증번호인 input_auth_num가 일치하는 쿼리를 User 모델에서 찾아 반환한 후 auth 세션을 생성
# 그 다음 비밀번호를 찾으려는 사용자의 userid를 세션값으로 생성
def auth_confirm_view(request):
    userid = request.POST.get('userid')
    input_auth_num = request.POST.get('input_auth_num')
    target_user = User.objects.get(userid=userid, auth=input_auth_num)
    target_user.auth = ""
    target_user.save()
    request.session['auth'] = target_user.userid

    return HttpResponse(json.dumps({"result": target_user.userid}, cls=DjangoJSONEncoder),
                        content_type="application/json")


# 마지막으로 auth_confirm_view를 통해 Ajax통신이 성공했다면,
# redirect 될 비밀번호 변경창의 view
from .forms import CustomSetPasswordForm

@logout_message_required
def auth_pw_reset_view(request):
    if request.method == 'GET':
        if not request.session.get('auth', False):
            raise PermissionDenied

    if request.method == 'POST':
        session_user = request.session['auth']
        current_user = User.objects.get(userid=session_user)
        login(request, current_user)

        reset_password_form = CustomSetPasswordForm(request.user, request.POST)

        if reset_password_form.is_valid():
            user = reset_password_form.save()
            messages.success(request, "PW has been changed successfully !")
            logout(request)
            return redirect('main:login')
        else:
            logout(request)
            request.session['auth'] = session_user
    else:
        reset_password_form = CustomSetPasswordForm(request.user)

    return render(request, 'main/password_reset.html', {'form': reset_password_form})
