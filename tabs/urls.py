from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'tabs'

urlpatterns = [
    path('activities_write/', views.activities_write, name='activities_write'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

