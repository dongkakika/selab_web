from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('gallery_add/', views.gallery_add, name='gallery_add'),
    path('gallery_delete/<int:pk>/', views.gallery_delete, name='gallery_delete'),
    path('gallery_modify/<int:pk>/', views.gallery_modify, name='gallery_modify'),

    path('temp/', views.temp)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
