from django.urls import path
from . import views

# App별 관리를 위해
app_name = 'notice'

urlpatterns=[
    path('', views.NoticeListView.as_view(), name='notice_list'),
    path('<int:pk>/', views.notice_detail_view, name='notice_detail'),
    path('write/', views.notice_write_view, name='notice_write'),
    path('<int:pk>/edit/', views.notice_edit_view, name='notice_edit'),
    path('<int:pk>/delete/', views.notice_delete_view, name='notice_delete'),

    # 좋아요 버튼 --> 비동기 방식을 통해 페이지가 새로고침이나 render되지 않도록 구현
    path('<int:pk>/like_notice', views.like_notice, name='like_notice'),
    # 좋아요 취소 버튼
    path('<int:pk>/cancel_like_notice', views.cancel_like_notice, name='cancel_like_notice'),
]