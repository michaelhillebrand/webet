from django.urls import path

from . import views

app_name = 'events'
urlpatterns = [
    path('', views.EventView.as_view({'get': 'list'}), name='list'),
    path('<int:pk>/',
         views.EventView.as_view({'get': 'retrieve'}), name='get'),
]
