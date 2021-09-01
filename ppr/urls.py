from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'ppr'

urlpatterns = [

    path('research/', views.research, name='research'),
    path('research/write/', views.research_write, name='research_write'),
    path('research/modify/<int:pk>/', views.research_modify, name='research_modify'),
    path('research/delete/<int:pk>/', views.research_delete, name='research_delete'),

    path('publication/', views.publication, name='publication'),

    path('domestic_journal_write/', views.write_domestic_journal, name='write_domestic_journal'),
    path('domestic/<int:pk>/', views.domestic_journal_detail_view, name='publication_detail'),
    path('domestic/<int:pk>/delete/', views.domestic_journal_delete, name='publication_delete'),

    path('international_journal_write/', views.write_international_journal, name='write_international_journal'),
    path('international/<int:pk>/', views.international_journal_detail_view, name='journal_detail'),
    path('international/<int:pk>/delete/', views.international_journal_delete, name='journal_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

