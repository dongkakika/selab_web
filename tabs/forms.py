from django import forms
from .models import activities, award, Conference

# forms의 ModelForm을 사용,
# form에 사용할 모델과 필드를 결정하는 Meta 클래스 쪽에 content 필드를 추가
class ActivitiesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ActivitiesForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Please write a title',
            'class': 'form-control',
            'autofocus': True,
        })
        self.fields['announced_date'].widget.attrs.update({
            'placeholder': 'Please write the announced date',
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
            'placeholder': 'Please write the date',
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
            'placeholder': 'Please enter the period',
            'class': 'form-control',
            'autofocus': True
        })

    class Meta:
        model = Conference
        fields = ['title', 'academic_conference', 'period']

