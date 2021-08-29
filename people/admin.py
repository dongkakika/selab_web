from django.contrib import admin
from .models import People, Staff, Professor

from django.contrib.auth.models import Group

class PeopleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'content',
    )
    search_fields = ('name', 'content')

class ProfessorAdmin(admin.ModelAdmin):
    list_display = (
        'content',
    )
    search_fields = ('content',)

admin.site.register(People, PeopleAdmin)
admin.site.register(Professor, ProfessorAdmin)
#admin.site.unregister(Group) # Admin 페이지의 GROUP 삭제