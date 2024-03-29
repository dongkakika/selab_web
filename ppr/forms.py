from django import forms
from .models import International_Journal, Domestic_Journal, Research

# forms의 ModelForm을 사용,
# form에 사용할 모델과 필드를 결정하는 Meta 클래스 쪽에 content 필드를 추가


class ResearchForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ResearchForm, self).__init__(*args, **kwargs)
        self.fields['number'].widget.attrs.update({
            'placeholder': 'Enter order number.',
            'class': 'form-control',
            'autofocus': True,
            'default': 2147483647,
        })
        self.fields['img'].label = 'Upload'
        self.fields['img'].widget.attrs.update({
            'placeholder': 'Please upload an image',
            'class': 'form-control',
            'type': 'file',
            'autofocus': True,
            'name': 'upload',
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
        fields = ['number', 'title', 'img', 'content', 'left_right_check']



class InternationalJournalWriteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InternationalJournalWriteForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Title'
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Please write a title\nex)J.W. Lee, D.H. Kim and J.E. Hong, "Estimation of Energy Consumption for Mobile Software using UML State Machine Diagram"',
            'class': 'form-control',
            'autofocus': True,
        })
        self.fields['journals'].widget.attrs.update({
            'placeholder': 'Please enter the journals\nex1) 정보처리학회\nex2) Korea Information Processing Society',
            'class': 'form-control',
            'autofocus': True
        })
        self.fields['issued_date'].widget.attrs.update({
            'placeholder': '"MUST" follow this form 2021. 08. 01 or 2021. 08',
            'class': 'form-control',
            'autofocus': True
        })
    class Meta:
        model = International_Journal
        fields = ['title', 'journals', 'issued_date', ] # 입력 받는 field

class DomesticJournalWriteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DomesticJournalWriteForm, self).__init__(*args, **kwargs)
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
            'placeholder': '"MUST" follow this form 2021. 08. 01 or 2021. 08',
            'class': 'form-control',
            'autofocus': True
        })

    class Meta:
        model = Domestic_Journal
        fields = ['title', 'journals', 'issued_date', ] # 입력 받는 field




