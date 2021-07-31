from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'tabs'

urlpatterns = [
    path('activities_write/', views.activities_write, name='activities_write'),
    path('activities/<int:pk>/', views.activities_modify, name='activities_modify'),

    path('ip_write/', views.ip_write, name='ip_write'),
    path('ip/<int:pk>/', views.ip_modify, name='ip_modify'),
    path('rp_write/', views.rp_write, name='rp_write'),
    path('rp/<int:pk>/', views.rp_modify, name='rp_modify'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

