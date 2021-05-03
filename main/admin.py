from django.contrib import admin

# Register your models here.
from .models import User
from django.contrib.auth.models import Group

class UserAdmin(admin.ModelAdmin):
    list_display = (
        'userid',
        'username',
        'level',
        'date_joined'
    )
    search_fields = ('userid', 'username')

admin.site.register(User, UserAdmin)
admin.site.unregister(Group) # Admin 페이지의 GROUP 삭제