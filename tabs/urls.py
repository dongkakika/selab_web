from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'tabs'

urlpatterns = [
    path('award_write/', views.award_write, name='award_write'),
    path('award/<int:pk>/', views.award_modify, name='award_modify'),
    path('award/<int:pk>/delete/', views.award_delete.as_view(), name='award_delete'),

    path('activities_write/', views.activities_write, name='activities_write'),
    path('activities/<int:pk>/', views.activities_modify, name='activities_modify'),
    path('activities/<int:pk>/delete/', views.activities_delete.as_view(), name='activities_delete'),

    path('ip_write/', views.ip_write, name='ip_write'),
    path('ip/<int:pk>/', views.ip_modify, name='ip_modify'),
    path('ip/<int:pk>/delete/', views.ip_delete.as_view(), name='ip_delete'),

    path('rp_write/', views.rp_write, name='rp_write'),
    path('rp/<int:pk>/', views.rp_modify, name='rp_modify'),
    path('rp/<int:pk>/delete/', views.rp_delete.as_view(), name='rp_delete'),

    path('conference_write/', views.conference_write, name='conference_write'),
    path('conference/<int:pk>/', views.conference_modify, name='conference_modify'),
    path('conference/<int:pk>/delete/', views.conference_delete.as_view(), name='conference_delete'),

    path('etc_write/', views.etc_write, name='etc_write'),
    path('etc/<int:pk>/', views.etc_modify, name='etc_modify'),
    path('etc/<int:pk>/delete/', views.etc_delete.as_view(), name='etc_delete'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

