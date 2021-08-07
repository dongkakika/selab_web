from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from main.models import User
from django.http import HttpResponse

# 'at sign'+login_required 의 기능을 하는 decorator 부분

# 아래는 로그인에 대해 지속해서 사용할 decorator 함수 정의

# 로그인 확인
def login_message_required(function):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:  # request.user로 데이터에 접근해서 접속 '상태' 확인 --> 로그인인지 판별
            messages.info(request, "Only for users who logged in")
            return redirect(settings.LOGIN_URL)
        return function(request, *args, **kwargs)

    return wrap


# 관리자 권한 확인 --> 게시글 작성, 삭제 등의 사용 권한 설정
def admin_required(function):
    def wrap(request, *args, **kwargs):
        # 권한 있을 때
        if request.user.level == '1' or request.user.level == '0':  # 접근 권한 검사
            return function(request, *args, **kwargs)
        # 권한 없을 때
        messages.info(request, "No access authority")
        return redirect('/')  # 권한이 없으므로 알림 받고 메인으로 이동

    return wrap

# 비로그인 확인
def logout_message_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:  # 이미 로그인한 사용자의 로그인과 회원가입을 막기 위해 is_authenticated로 확인
            messages.info(request, "You are already logged in")
            return redirect('/')
        return function(request, *args, **kwargs)
    return wrap