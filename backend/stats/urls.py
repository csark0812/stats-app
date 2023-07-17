# chat/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    # path("boxscore/", views.boxscore, name="boxscore"),
    path("<str:room_name>/", views.room, name="room"),
]