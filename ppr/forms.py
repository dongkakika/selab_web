from django import forms
from .models import Publication, Journal, Research

# forms의 ModelForm을 사용,
# form에 사용할 모델과 필드를 결정하는 Meta 클래스 쪽에 content 필드를 추가


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
        fields = ['title', 'img', 'content', 'left_right_check']



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
            'placeholder': '"MUST" follow this form 2021-08-01',
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
            'placeholder': '"MUST" follow this form 2021-08-01',
            'class': 'form-control',
            'autofocus': True
        })

    class Meta:
        model = Journal
        fields = ['title', 'journals', 'issued_date', ] # 입력 받는 field




