from django import forms
from .models import Notice

# forms의 ModelForm을 사용,
# form에 사용할 모델과 필드를 결정하는 Meta 클래스 쪽에 제목과, 내용 필드를 추가
# 게시글 작성의 내용부분은 위지위그 텍스트 에디터를 적용하므로 init메소드에는 title 필드만 추가
class NoticeWriteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NoticeWriteForm, self).__init__(*args, **kwargs)
        self.fields['title'].label = 'Title'
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Please write a title',
            'class': 'form-control',
            'autofocus': True,
        })
    class Meta:
        model = Notice
        fields = ['title', 'content', 'top_fixed'] # 게시글 (작성하면서) 상단에 고정 체크 --> 모델에서 BooleanField로 생성한 top_fixed 필드를 활용







