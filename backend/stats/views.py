from django.shortcuts import render, redirect
from . import models
from . import forms

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
