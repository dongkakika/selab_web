from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.home, name='home'),
    path('test/', views.test, name='test'),

    path('login/', views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('agreement/', views.AgreementView.as_view(), name='agreement'),
    path('sign_up/', views.sign_up.as_view(), name='sign_up'),
    path('activate/', views.activate_sign_up, name='activate_sign_up'),
    path('registerauth/', views.register_success, name='register_success'),
    path('activate/<str:uid64>/<str:token>/', views.activate, name='activate'),

    path('login/choose_one/', views.choose_one, name='choose_one'),
    path('recovery/id/', views.IdRecoveryView.as_view(), name='recovery_id'),
    path('recovery/id/find/', views.ajax_find_id_view, name='ajax_id'),

    path('recovery/pw/', views.RecoveryPwView.as_view(), name='recovery_pw'),
    path('recovery/pw/find/', views.ajax_find_pw_view, name='ajax_pw'),
    path('recovery/pw/auth/', views.auth_confirm_view, name='recovery_auth'),
    path('recovery/pw/reset/', views.auth_pw_reset_view, name='recovery_pw_reset'),


]
