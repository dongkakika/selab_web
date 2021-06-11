from django.db import models
import os
from django.conf import settings
from django.db import models

# Create your models here.

class Notice(models.Model):
    # AUTH_USER_MODEL인 사용자 모델과 ForeignKey 관계로 연결
    # 게시글이 삭제되어도 on_delete를 사용해 NULL 작성자로 변경 후 해당 내용을 유지
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, verbose_name='작성자')
    title = models.CharField(max_length=128, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    # top_fixed --> True라면 게시글 리스트의 상단에 고정되도록 구현, BooleanField로 True | False를 받음.
    top_fixed = models.BooleanField(verbose_name='상단고정', default=False)
    like_count = models.IntegerField(verbose_name="좋아요", default=0)

    def __str__(self):
        return self.title

    class Meta:
        db_table = '게시판'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'