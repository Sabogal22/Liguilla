from django.urls import path
from . import views

urlpatterns = [
    # Rutas para el panel de usuario y administrador
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

    # Rutas para las noticias
    path('news/', views.news, name='news'),
    path('news/list/', views.news_list, name='news_list'),
    path('news/new/', views.news_create, name='news_create'),
    path('news/<int:pk>/edit/', views.news_update, name='news_update'),
    path('news/<int:pk>/delete/', views.news_delete, name='news_delete'),

    # Rutas para los equipos
    path('teams/', views.team_list, name='team_list'),
    path('teams/new/', views.team_create, name='team_create'),
    path('teams/<int:pk>/edit/', views.team_update, name='team_update'),
    path('teams/<int:pk>/delete/', views.team_delete, name='team_delete'),

    # Rutas para los jugadores
    path('teams/<int:team_id>/players/', views.player_list, name='player_list'),
    path('teams/<int:team_id>/players/new/', views.player_create, name='player_create'),
    path('teams/<int:team_id>/players/<int:pk>/edit/', views.player_update, name='player_update'),
    path('teams/<int:team_id>/players/<int:pk>/delete/', views.player_delete, name='player_delete'),

    # Rutas para los partidos
    path('matches/', views.match_list, name='match_list'),
    path('matches/new/', views.match_create, name='match_create'),
    path('matches/<int:pk>/edit/', views.match_update, name='match_update'),
    path('matches/<int:pk>/delete/', views.match_delete, name='match_delete'),

    # Rutas para los eventos
    path('matches/<int:match_id>/events/new/', views.event_create, name='event_create'),

    # Ruta para la tabla de posiciones
    path('standings/', views.standings, name='standings'),
]
