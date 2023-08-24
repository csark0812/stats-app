# In your app's models.py file

from django.db import models
from . import validators

class Team(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=10)
    head_coach = models.CharField(max_length=255)
    # logo = models.ImageField(upload_to='team_logos/')

    def __str__(self):
        return self.name


class Player(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    jersey_number = models.PositiveIntegerField()
    height = models.CharField(max_length=20, validators=[validators.validate_height])
    # image = models.ImageField(upload_to='player_images/')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True,blank=True)
    POSITION_CHOICES = [
        ('G', 'Guard'),
        ('F', 'Forward'),
        ('PG', 'Point Guard'),
        ('SG', 'Shooting Guard'),
        ('SF', 'Small Forward'),
        ('PF', 'Power Forward'),
        ('C', 'Center'),
    ]
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Game(models.Model):
    home_team = models.ForeignKey(Team, related_name='home_games', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_games', on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.home_team.name} vs {self.away_team.name} - {self.date}"


class GameStat(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    oreb = models.PositiveIntegerField()
    dreb = models.PositiveIntegerField()
    ast = models.PositiveIntegerField()
    stl = models.PositiveIntegerField()
    blk = models.PositiveIntegerField()
    two_fgm = models.PositiveIntegerField()
    two_fga = models.PositiveIntegerField()
    three_fgm = models.PositiveIntegerField()
    three_fga = models.PositiveIntegerField()
    ftm = models.PositiveIntegerField()
    fta = models.PositiveIntegerField()
    pf = models.PositiveIntegerField()
    tov = models.PositiveIntegerField()

    # Add more fields as needed

    def __str__(self):
        return f"{self.player} - Game: {self.game}"
