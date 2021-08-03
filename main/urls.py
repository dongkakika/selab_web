from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('agreement/', views.AgreementView.as_view(), name='agreement'),
    path('sign_up/', views.sign_up.as_view(), name='sign_up'),
    path('activate/', views.activate, name='activate')
]
