from django.urls import path

from . import views

app_name = 'players'
urlpatterns = [
    path('', views.player_list, name='list'),
    path('create/', views.player_list, name='create'),
    path('<int:player_id>/', views.player_read, name='get'),
    path('<int:player_id>/update/', views.player_update, name='update'),
    path('<int:player_id>/delete/', views.player_delete, name='delete'),
]