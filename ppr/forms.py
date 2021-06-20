from django import forms
from .models import People

# forms의 ModelForm을 사용,
# form에 사용할 모델과 필드를 결정하는 Meta 클래스 쪽에 content 필드를 추가
class PeopleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PeopleForm, self).__init__(*args, **kwargs)

    class Meta:
        model = People
        fields = ['content'] # 보여지는 field는 오로지 content







