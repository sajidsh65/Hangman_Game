from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new/', views.new_game, name='new_game'),
    path('guess/', views.guess_letter, name='guess_letter'),
    path('status/', views.game_status, name='game_status'),
]
