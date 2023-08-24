# chat/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("players/", views.players, name="players"),
    path("teams/", views.teams, name="teams"),
    path("newgame/", views.game_init, name="newgame"),
    # path("boxscore/", views.boxscore, name="boxscore"),
    path("<str:room_name>/", views.room, name="room"),
]