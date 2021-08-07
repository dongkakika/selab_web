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
    path('publication_write/', views.write_publication, name='write_publication'),
    path('publications/<int:pk>/', views.publication_detail_view, name='publication_detail'),
    path('publications/<int:pk>/delete/', views.publication_delete, name='publication_delete'),

    path('journal_write/', views.write_journal, name='write_journal'),
    path('journal/<int:pk>/', views.journal_detail_view, name='journal_detail'),
    path('journal/<int:pk>/delete/', views.journal_delete, name='journal_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

