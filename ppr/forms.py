from django import forms
from .models import People, Professor, Publication, Journal, Staff, Research, rp, ip

# forms의 ModelForm을 사용,
# form에 사용할 모델과 필드를 결정하는 Meta 클래스 쪽에 content 필드를 추가
class IPForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(IPForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Please write a title',
            'class': 'form-control',
            'autofocus': True,
        })
        self.fields['type'].widget.attrs.update({
            'placeholder': 'Please enter the registered type',
            'class': 'form-control',
            'autofocus': True
        })
        self.fields['applicant'].widget.attrs.update({
            'placeholder': 'Please write the applicant',
            'class': 'form-control',
            'autofocus': True
        })
        self.fields['date'].widget.attrs.update({
            'placeholder': 'Please write the applied date',
            'class': 'form-control',
            'autofocus': True
        })

    class Meta:
        model = ip
        fields = ['title', 'type', 'applicant', 'date']

class RPForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(RPForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Please write a title',
            'class': 'form-control',
            'autofocus': True,
        })
        self.fields['org'].widget.attrs.update({
            'placeholder': 'Please enter the related organization',
            'class': 'form-control',
            'autofocus': True
        })
        self.fields['period'].widget.attrs.update({
            'placeholder': 'Please make the period',
            'class': 'form-control',
            'autofocus': True
        })

    class Meta:
        model = rp
        fields = ['title', 'org', 'period']

class ResearchForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ResearchForm, self).__init__(*args, **kwargs)
        self.fields['img'].widget.attrs.update({
            'placeholder': 'Please upload an image',
            'class': 'form-control',
            'type': 'file',
            'autofocus': True,
        })
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Please write a title',
            'class': 'form-control',
            'autofocus': True,
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Please make the content',
            'class': 'form-control',
            'autofocus': True
        })

    class Meta:
        model = Research
        fields = ['title', 'img', 'content']

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
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Please write your information\nex) 2020 - Present, M.S. Computer Science, CBNU',
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

class PublicationWriteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PublicationWriteForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Title'
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Please write a title',
            'class': 'form-control',
            'autofocus': True,
        })
        self.fields['publisher'].widget.attrs.update({
            'placeholder': 'Please enter the publisher\nex1) Institute of Electrical and Electronics Engineers ( IEEE )\nex2) 한빛미디어',
            'class': 'form-control',
            'autofocus': True
        })
        self.fields['published_date'].widget.attrs.update({
            'placeholder': 'ex) 2021-06-21',
            'class': 'form-control',
            'autofocus': True
        })
    class Meta:
        model = Publication
        fields = ['title', 'publisher', 'published_date'] # 입력 받는 field

class JournalWriteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(JournalWriteForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Title'
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Please write a title',
            'class': 'form-control',
            'autofocus': True,
        })
        self.fields['journals'].widget.attrs.update({
            'placeholder': 'Please enter the journals\nex1) 정보처리학회\nex2) Korea Information Processing Society',
            'class': 'form-control',
            'autofocus': True
        })
        self.fields['issued_date'].widget.attrs.update({
            'placeholder': 'ex) 2021-06-21',
            'class': 'form-control',
            'autofocus': True
        })
    class Meta:
        model = Journal
        fields = ['title', 'journals', 'issued_date'] # 입력 받는 field




