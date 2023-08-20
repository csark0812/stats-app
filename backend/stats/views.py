from django.shortcuts import render, redirect
from rest_framework import viewsets
from . import models
from . import forms
from . import serializers

class LeagueViewSet(viewsets.ModelViewSet):
    queryset = models.League.objects.all()
    serializer_class = serializers.LeagueSerializer

class SeasonViewSet(viewsets.ModelViewSet):
    queryset = models.Season.objects.all()
    serializer_class = serializers.SeasonSerializer

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = models.Division.objects.all()
    serializer_class = serializers.DivisionSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSeasonSerializer

class TeamSeasonViewSet(viewsets.ModelViewSet):
    queryset = models.TeamSeason.objects.all()
    serializer_class = serializers.TeamSeasonSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = models.Player.objects.all()
    serializer_class = serializers.PlayerSerializer

class PlayerSeasonViewSet(viewsets.ModelViewSet):
    queryset = models.PlayerSeason.objects.all()
    serializer_class = serializers.PlayerSeasonSerializer

class GameViewSet(viewsets.ModelViewSet):
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer

class StatLineViewSet(viewsets.ModelViewSet):
    queryset = models.StatLine.objects.all()
    serializer_class = serializers.StatLineSerializer

class RecordedStatViewSet(viewsets.ModelViewSet):
    queryset = models.RecordedStat.objects.all()
    serializer_class = serializers.RecordedStatSerializer


# Create your views here.
def index(request):
    return render(request, "stats/index.html")

def room(request, room_name):
    return render(request, "stats/room.html", {"room_name": room_name})

def boxscore(request):
    return render(request, "stats/boxscore.html")
def players(request):
    players_list = models.Player.objects.all() 
    if request.method == 'POST':
        player_form = forms.PlayerForm(request.POST)
        if player_form.is_valid():
            player_form.save()
            return redirect('players')  # Redirect to refresh the page
    else:
        player_form = forms.PlayerForm()
    return render(request, "stats/players.html", {"players_list": players_list, "player_form":player_form})
def teams(request):
    return render(request, "stats/teams.html")
def game_init(request):
    return render(request, "stats/game_init.html")
