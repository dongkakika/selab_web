from django.contrib import admin
from .models import People, Journal

from django.contrib.auth.models import Group

class PeopleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'content',
    )
    search_fields = ('name', 'content')

class JournalAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'issued_date',
        'journals'
    )
    search_fields = ('title', 'issued_date', 'journals')

admin.site.register(People, PeopleAdmin)
admin.site.register(Journal, JournalAdmin)
#admin.site.unregister(Group) # Admin 페이지의 GROUP 삭제