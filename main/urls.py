from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='main'),
    path('people/', views.people, name='main'),
    path('research/', views.research, name='main'),
    path('publication/', views.publication, name='main'),
]
