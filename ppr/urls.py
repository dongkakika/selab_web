from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'ppr'

urlpatterns = [
    path('professor/', views.professor, name='professor'),
    path('professor/modifyContent/', views.modifyProfessor, name='modifyProfessor'),
    path('members/', views.members, name='members'),
    path('add_member/', views.add_member, name='add_member'),
    path('add_other_staff/', views.add_other_staff, name='add_other_staff'),
    path('members/modify/<int:pk>/', views.member_modify, name='member_modify'),
    path('members/modify/staff/<int:pk>/', views.staff_modify, name='staff_modify'),
    path('members/delete/<int:pk>/', views.member_delete, name='member_delete'),
    path('members/delete/staff/<int:pk>/', views.staff_delete, name='staff_delete'),

    path('ip_write/', views.ip_write, name='ip_write'),
    path('rp_write/', views.rp_write, name='rp_write'),

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

    path('gallery/', views.gallery, name='gallery'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

