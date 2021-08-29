from django import forms
from .models import People, Professor, Staff

class PeopleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PeopleForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Please write your name',
            'class': 'form-control',
            'autofocus': True,
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Please enter your e-mail',
            'class': 'form-control',
            'autofocus': True
        })
        self.fields['img_upload'].widget.attrs.update({
            'placeholder': 'Upload your image',
            'class': 'form-control',
            'type': 'file',
            'autofocus': True
        })

    class Meta:
        model = People
        fields = ['name', 'content', 'email', 'img_upload']

class StaffForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StaffForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'placeholder': 'Please write your name',
            'class': 'form-control',
            'autofocus': True,
        })
        self.fields['email'].widget.attrs.update({
            'placeholder': 'Please enter your e-mail',
            'class': 'form-control',
            'autofocus': True
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Please write your information\nex) 2020 - Present, B.S. Computer Science, CBNU',
            'class': 'form-control',
            'autofocus': True
        })
        self.fields['img_upload'].widget.attrs.update({
            'placeholder': 'Upload your image',
            'class': 'form-control',
            'type': 'file',
            'autofocus': True
        })

    class Meta:
        model = Staff
        fields = ['name', 'content', 'email', 'img_upload']

class ProfessorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProfessorForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Professor
        fields = ['content'] # 보여지는 field는 오로지 content