from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='main'),
    path('home/', views.home, name='home'),
    path('login/', views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),

]
