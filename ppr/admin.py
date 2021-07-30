from django.contrib import admin
from .models import Journal

from django.contrib.auth.models import Group
class JournalAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'issued_date',
        'journals'
    )
    search_fields = ('title', 'issued_date', 'journals')

admin.site.register(Journal, JournalAdmin)
#admin.site.unregister(Group) # Admin 페이지의 GROUP 삭제