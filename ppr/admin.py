from django.contrib import admin
from .models import International_Journal, Domestic_Journal, Research

from django.contrib.auth.models import Group
class InternationalJournalAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'issued_date',
        'journals'
    )
    search_fields = ('title', 'issued_date', 'journals')

class DomesticJournalAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'issued_date',
        'journals'
    )
    search_fields = ('title', 'issued_date', 'journals')

class ResearchAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'img',
        'content',
        'left_right_check'
    )
    search_fields = ('title', 'publisher', 'published_date', 'left_right_check')

admin.site.register(International_Journal, InternationalJournalAdmin)
admin.site.register(Domestic_Journal, DomesticJournalAdmin)
admin.site.register(Research, ResearchAdmin)
#admin.site.unregister(Group) # Admin 페이지의 GROUP 삭제