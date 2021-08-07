from django import forms
from .models import User
from .choice import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, SetPasswordForm, PasswordChangeForm

class LoginForm(forms.Form):
    userid = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', }),
        error_messages={'required': '아이디를 입력해주세요.'},
        max_length=20,
        label='ID'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', }),
        error_messages={'required': '비밀번호를 입력해주세요.'},
        label='PW'
    )

    def clean(self):
        cleaned_data = super().clean()
        userid = cleaned_data.get('userid')
        password = cleaned_data.get('password')

        if userid and password:
            try:
                user = User.objects.get(userid=userid)
            except User.DoesNotExist:
                self.add_error('userid', '아이디 또는 비밀번호가 존재하지 않습니다.')
                return

            if not check_password(password, user.password):
                self.add_error('password', '아이디 또는 비밀번호가 존재하지 않습니다.')


# 휴대폰 번호 자릿수 검사, 이런 식으로 확장하면 된다.
def hp_validator(value):
    if len(str(value)) != 10:
        raise forms.ValidationError('정확한 핸드폰 번호를 입력해주세요!')


class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['userid'].label = 'ID'
        self.fields['userid'].widget.attrs.update({
            'class': 'form-control',
            'autofocus': False
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': '비밀번호를 입력해주세요.'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': '비밀번호를 다시 입력해주세요.'
        })

        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'E-mail for recovering your ID or PW.'
        })

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Kil Dong Hong',
        })

    class Meta:
        model = User
        fields = ['userid', 'password1', 'password2', 'email', 'username',]

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.level = '3'
        user.is_active = False
        user.is_staff = True
        user.save()

        return user

# 아이디 찾기 영역
class IdRecoveryForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    email = forms.EmailField(widget=forms.EmailInput)

    class Meta:
        fields = ['name', 'email']

    def __init__(self, *args, **kwargs):
        super(IdRecoveryForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Name'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'form_name',
            'placeholder': 'Kil Dong Hong'
        })
        self.fields['email'].label = 'E-mail'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'form_email'
        })

# 비밀번호 찾기 영역
class RecoveryPwForm(forms.Form):
    userid = forms.CharField(
        widget=forms.TextInput,)
    name = forms.CharField(
        widget=forms.TextInput,)
    email = forms.EmailField(
        widget=forms.EmailInput,)

    class Meta:
        fields = ['userid', 'name', 'email']

    def __init__(self, *args, **kwargs):
        super(RecoveryPwForm, self).__init__(*args, **kwargs)
        self.fields['userid'].label = 'ID'
        self.fields['userid'].widget.attrs.update({
            'class': 'form-control',
            'id': 'pw_form_id',
        })
        self.fields['name'].label = 'Name'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'pw_form_name',
            'placeholder': 'Kil Dong Hong'
        })
        self.fields['email'].label = 'E-mail'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'id': 'pw_form_email',
        })

# 인증번호 입력 후 사용자의 비밀번호 변경 창에 사용할 SetPasswordForm을 상속받는 form
from django.contrib.auth.forms import SetPasswordForm
class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)
        self.fields['new_password1'].label = 'New PW'
        self.fields['new_password1'].widget.attrs.update({
            'class': 'form-control',
        })
        self.fields['new_password2'].label = 'New PW Check'
        self.fields['new_password2'].widget.attrs.update({
            'class': 'form-control',
        })