from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect

# Create your views here.
from main.decorators import logout_message_required, admin_required
from django.views.generic import FormView, View, CreateView
from .forms import LoginForm, RegisterForm
from .models import User
from ppr.models import Journal, Publication
from notice.models import Notice
from django.utils.decorators import method_decorator
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy, reverse, resolve
from django.shortcuts import resolve_url
from django.contrib import messages
from django.shortcuts import get_object_or_404

def home(request):
    # 캐러셀 슬라이드 내용 뽑아오기
    journal = Journal.objects.last()
    publication = Publication.objects.last()
    notice = Notice.objects.last()

    if journal == None:
        journal = Journal(title="Welcome", journals="DEFAULT", issued_date="DEFAULT")
    if publication == None:
        publication = Publication(title="Welcome", publisher="DEFAULT_", published_date="DEFAULT_")
    if notice == None:
        notice = Notice(title="Welcome", content="DEFAULT__", hits="DEFAULT__")

    context = {
        'journal': journal,
        'publication': publication,
        'notice': notice,
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

    def get_success_url(self, **kwargs):
        return str(hello)

    def get_context_data(self, **kwargs):
        global hello
        hello = self.request.GET.get('next')
        return super().get_context_data(**kwargs)

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
            return redirect('/agreement')

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
        return '/login/?next=/'

    def form_valid(self, form):
        self.object = form.save()
        messages.success(self.request, "Successfully registered.")
        return redirect(self.get_success_url())

# 로그아웃 후,
def logout_view(request):
    logout(request)
    next = request.GET['next']
    return redirect(next)

@admin_required
def activate(request):
    user = User.objects.get(id=1)
    if(request.user.level == '0' or request.user.level == '1'):
        if(user.activate == False):
            user.activate = True
            user.save()
        else:
            user.activate = False
            user.save()

    return redirect('/')