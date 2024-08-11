from django.urls import path
from . import views

urlpatterns = [
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('news', views.news, name='news'),
    path('news/list', views.news_list, name='news_list'),
    path('news/new/', views.news_create, name='news_create'),
    path('news/<int:pk>/edit/', views.news_update, name='news_update'),
    path('news/<int:pk>/delete/', views.news_delete, name='news_delete'),
]
