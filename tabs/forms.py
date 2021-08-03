from django import forms
from .models import activities, award, Conference, ip, rp

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
            'placeholder': '"MUST" follow this form 2021-08-01',
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
            'placeholder': '"MUST" follow this form 2021-08-01 ~ 2021-12-01',
            'class': 'form-control',
            'autofocus': True
        })

    class Meta:
        model = rp
        fields = ['title', 'org', 'period']

class ActivitiesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ActivitiesForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Please write a title',
            'class': 'form-control',
            'autofocus': True,
        })
        self.fields['announced_date'].widget.attrs.update({
            'placeholder': '"MUST" follow this form 2021-08-01',
            'class': 'form-control',
            'autofocus': True
        })

    class Meta:
        model = activities
        fields = ['title', 'announced_date']

class AwardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AwardForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Please write a title',
            'class': 'form-control',
            'autofocus': True,
        })
        self.fields['content'].widget.attrs.update({
            'placeholder': 'Please enter the content',
            'class': 'form-control',
            'autofocus': True
        })
        self.fields['date'].widget.attrs.update({
            'placeholder': '"MUST" follow this form 2021-08-01',
            'class': 'form-control',
            'autofocus': True
        })

    class Meta:
        model = award
        fields = ['title', 'content', 'date']

class ConferenceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ConferenceForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Please write a title',
            'class': 'form-control',
            'autofocus': True,
        })
        self.fields['academic_conference'].widget.attrs.update({
            'placeholder': 'Please fill in the conference name',
            'class': 'form-control',
            'autofocus': True
        })
        self.fields['period'].widget.attrs.update({
            'placeholder': '"MUST" follow this form 2021-08-01 ~ 2021-12-01',
            'class': 'form-control',
            'autofocus': True
        })

    class Meta:
        model = Conference
        fields = ['title', 'academic_conference', 'period']

