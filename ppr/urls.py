from django.urls import path
from . import views

app_name = 'ppr'

urlpatterns = [
    path('people/', views.people, name='people'),
    path('people/modifyContent/', views.modifyContent, name='modifyContent'),
    path('gallery/', views.gallery, name='gallery'),
]