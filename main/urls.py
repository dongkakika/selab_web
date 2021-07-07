from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='main'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),

]
