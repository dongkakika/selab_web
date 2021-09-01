from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'people'

urlpatterns = [
    path('professor/', views.professor, name='professor'),
    path('professor/modifyContent/', views.modifyProfessor, name='modifyProfessor'),
    path('members/', views.members, name='members'),
    path('add_member/<int:pk>/', views.add_member, name='add_member'),
    path('add_other_staff/', views.add_other_staff, name='add_other_staff'),
    path('members/modify/<int:pk>/', views.member_modify, name='member_modify'),

    path('members/alumni/<int:pk>/', views.alumni_registration, name='member_modify'),

    path('members/modify/staff/<int:pk>/', views.staff_modify, name='staff_modify'),
    path('members/delete/<int:pk>/', views.member_delete, name='member_delete'),
    path('members/delete/staff/<int:pk>/', views.staff_delete, name='staff_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

