from django.contrib import admin
from .models import Notice

# Register your models here.
class NoticeAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'writer',
        'hits',
        'registered_date',

    )

    # admin 커스텀 중, ForeignKey가 search_fields에 포함되어 있으면, incontains 에러가 발생
    # --> 작성자인 writer가 User 모델과, ForeignKey로 엮여있기 때문에 search_fields에 'writer__user_id'와 같이 추가
    search_fields = ('title', 'content', 'writer__user_id')


admin.site.register(Notice, NoticeAdmin)