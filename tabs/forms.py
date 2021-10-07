from django import forms
from .models import activities, award, Conference, ip, rp, Etc

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
        self.fields['number'].widget.attrs.update({
            'placeholder': 'Please write the serial number',
            'class': 'form-control',
            'autofocus': True
        })
        self.fields['date'].widget.attrs.update({
            'placeholder': '"MUST" follow this form 2021 .08 .01 or 2021 .08',
            'class': 'form-control',
            'autofocus': True
        })

    class Meta:
        model = ip
        fields = ['title', 'type', 'number', 'date']

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
            'placeholder': '"MUST" follow this form 2021 .08 .01 or 2021 .08',
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
            'placeholder': '"MUST" follow this form 2021 .08 .01 or 2021 .08',
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
            'placeholder': '"MUST" follow this form 2021 .08 .01 or 2021 .08',
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
            'placeholder': 'Please write a title, ex) D.H. Kim, Investigation for Software',
            'class': 'form-control',
            'autofocus': True,
        })
        self.fields['academic_conference'].widget.attrs.update({
            'placeholder': 'Please fill the conference name in.',
            'class': 'form-control',
            'autofocus': True
        })
        self.fields['period'].widget.attrs.update({
            'placeholder': '"MUST" follow this form 2021 .08 .01 or 2021 .08',
            'class': 'form-control',
            'autofocus': True
        })

    class Meta:
        model = Conference
        fields = ['title', 'academic_conference', 'period']

class EtcWriteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EtcWriteForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Title'
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
            'placeholder': '"MUST" follow this form 2021 .08 .01 or 2021 .08',
            'class': 'form-control',
            'autofocus': True
        })
    class Meta:
        model = Etc
        fields = ['title', 'content', 'date', ] # 입력 받는 field
