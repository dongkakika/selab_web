from django.contrib import admin
from .models import Journal, Publication, Research

from django.contrib.auth.models import Group
class JournalAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'issued_date',
        'journals'
    )
    search_fields = ('title', 'issued_date', 'journals')

class PublicationAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'publisher',
        'published_date'
    )
    search_fields = ('title', 'publisher', 'published_date')

class ResearchAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'img',
        'content',
        'left_right_check'
    )
    search_fields = ('title', 'publisher', 'published_date', 'left_right_check')

admin.site.register(Journal, JournalAdmin)
admin.site.register(Publication, PublicationAdmin)
admin.site.register(Research, ResearchAdmin)
#admin.site.unregister(Group) # Admin 페이지의 GROUP 삭제