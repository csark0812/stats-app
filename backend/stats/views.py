from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "stats/index.html")

def room(request, room_name):
    return render(request, "stats/room.html", {"room_name": room_name})

def boxscore(request):
    return render(request, "stats/boxscore.html")
