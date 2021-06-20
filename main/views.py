from django.shortcuts import render
from django.conf import settings
from django.shortcuts import redirect

# Create your views here.
from main.decorators import logout_message_required
from django.views.generic import FormView
from .forms import LoginForm
from django.utils.decorators import method_decorator
from django.contrib.auth import login, logout, authenticate


def home(request):
    return render(request, 'main/home.html')


def research(request):
    return render(request, 'main/research.html')

def publication(request):
    return render(request, 'main/publication.html')

# 로그인 후,
@method_decorator(logout_message_required, name='dispatch')
class LoginView(FormView):
    template_name = 'main/login.html'
    form_class = LoginForm
    success_url = '/' # 로그인 성공했을 때 들어가는 주소

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

# 로그아웃 후,
def logout_view(request):
    logout(request)
    return redirect('/')