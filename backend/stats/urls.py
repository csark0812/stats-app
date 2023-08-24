# chat/urls.py
from django.urls import include,path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'leagues', views.LeagueViewSet)
router.register(r'seasons', views.SeasonViewSet)
router.register(r'divisions', views.DivisionViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'players', views.PlayerViewSet)
router.register(r'teamseasons', views.TeamSeasonViewSet)
router.register(r'playerseasons', views.PlayerSeasonViewSet)
router.register(r'games', views.GameViewSet)
router.register(r'statlines', views.StatLineViewSet)
router.register(r'recordedstats', views.RecordedStatViewSet)


urlpatterns = [
    path("", views.index, name="index"),
    path("players/", views.players, name="players"),
    path("teams/", views.teams, name="teams"),
    path("newgame/", views.game_init, name="newgame"),
    # path("boxscore/", views.boxscore, name="boxscore"),
    path("<str:room_name>/", views.room, name="room"),
    path('api/', include(router.urls)),
    
]