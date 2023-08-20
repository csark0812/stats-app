# In your app's models.py file

from django.db import models
from . import validators
from datetime import timedelta


class League(models.Model):
    league_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)  # Name of the league
    foul_out = models.PositiveIntegerField()  # Number of fouls needed to foul out
    bonus_foul_amt = models.PositiveIntegerField()  # Number of fouls for bonus free throws
    dbl_bonus_foul_amt = models.PositiveIntegerField()  # Number of fouls for double bonus free throws
    full_timeouts = models.PositiveIntegerField()  # Number of full timeouts per team
    s30_timeouts = models.PositiveIntegerField()  # Number of 30-second timeouts per team
    possession_arrow = models.BooleanField(default=True)  # Possession arrow direction
    period_length = models.DurationField()
      # Length of a period in minutes
    period_amt = models.PositiveIntegerField()  # Number of periods in a game
    shot_clock_length = models.DurationField()  # Length of shot clock in seconds
    overtime_length = models.DurationField()  # Length of overtime period in minutes

    def __str__(self):
        return self.name

class Season(models.Model):
    season_id = models.AutoField(primary_key=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='seasons')
    name = models.CharField(max_length=100) # Name of the season
    def __str__(self):
        return self.name

class Division(models.Model):
    division_id = models.AutoField(primary_key=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='divisions')
    name = models.CharField(max_length=100) # name of the division

    def __str__(self):
        return self.name  
class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='teams')
    name = models.CharField(max_length=100) # Name of the team
    abbreviation = models.CharField(max_length=10) # abbrevation of the team
    logo = models.ImageField(upload_to='team_logos/',blank=True, null=True)  # Assuming you want to upload logos

    def __str__(self):
        return self.name

class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='players')
    first_name = models.CharField(max_length=50) # first name of player
    last_name = models.CharField(max_length=50) # last name of player
    height = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class TeamSeason(models.Model):
    team_season_id = models.AutoField(primary_key=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='teams')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='seasons', null=True,blank=True)
    division = models.ForeignKey(Division, on_delete=models.SET_NULL, null=True, related_name='teams')
    head_coach = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        unique_together = ('team', 'season')  # Enforce one TeamSeason per team per season

    def __str__(self):
        return f"{self.team} - {self.season}"
    
class PlayerSeason(models.Model):
    player_season_id = models.AutoField(primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='seasons')
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='players')
    team_season = models.ForeignKey(TeamSeason, on_delete=models.SET_NULL, null= True, related_name='players')
    jersey_number = models.PositiveIntegerField()
    
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
    class Meta:
        unique_together = ('player', 'season')  # Enforce one PlayerSeason per player per season

    def __str__(self):
        return f"{self.player.first_name} {self.player.last_name} - {self.season.season_name}"

class Game(models.Model):
    game_id = models.AutoField(primary_key=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='games')
    home_team = models.ForeignKey(TeamSeason, on_delete=models.CASCADE, related_name='home_games')
    away_team = models.ForeignKey(TeamSeason, on_delete=models.CASCADE, related_name='away_games')
    location = models.CharField(max_length=50)
    date_time = models.DateTimeField()
    counts_towards_record = models.BooleanField(default=True)
    time_on_clock = models.DurationField(default=0)  # Default value set to 0
    period = models.PositiveIntegerField(default=1)
    away_s30_timeouts_taken = models.PositiveIntegerField(default=0)
    home_s30_timeouts_taken = models.PositiveIntegerField(default=0)
    away_full_timeouts_taken = models.PositiveIntegerField(default=0)
    home_full_timeouts_taken = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} - {self.date_time}"

    def save(self, *args, **kwargs):
        # Set the default value for time_on_clock using the starting_clock_time method
        self.time_on_clock = self.starting_clock_time()
        super().save(*args, **kwargs)

    def starting_clock_time(self):
        return self.season.league.period_length



class StatLine(models.Model):
    statline_id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='statsheet')
    team = models.ForeignKey(TeamSeason, on_delete=models.CASCADE, related_name='statsheet')
    player = models.ForeignKey(PlayerSeason, on_delete=models.CASCADE, related_name='statlines')
    mins = models.DurationField()
    fg2m = models.PositiveIntegerField()
    fg2a = models.PositiveIntegerField()
    fg3m = models.PositiveIntegerField()
    fg3a = models.PositiveIntegerField()
    ftm = models.PositiveIntegerField()
    fta = models.PositiveIntegerField()
    oreb = models.PositiveIntegerField()
    dreb = models.PositiveIntegerField()
    ast = models.PositiveIntegerField()
    stl = models.PositiveIntegerField()
    blk = models.PositiveIntegerField()
    tov = models.PositiveIntegerField()
    pf = models.PositiveIntegerField()
    tf = models.PositiveIntegerField()

    @property
    def pts(self):
        return 2 * self.fg2m + 3 * self.fg3m + self.ftm

    @property
    def reb(self):
        return self.oreb + self.dreb
    
    def __str__(self):
        return f"{self.player}'s stats in {self.game}"
    
class RecordedStat(models.Model):
    stat_id = models.AutoField(primary_key=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="statistics")
    statline = models.ForeignKey(StatLine, on_delete=models.CASCADE, related_name="statistics")
   
    STAT_CHOICES = [
    ('fg2m', 'Two-point Field Goal Made'),
    ('fg2a', 'Two-point Field Goal Attempted'),
    ('fg3m', 'Three-Point Field Goal Made'),
    ('fg3a', 'Three-Point Field Goal Attempted'),
    ('ftm', 'Free Throw Made'),
    ('fta', 'Free Throw Attempted'),
    ('oreb', 'Offensive Rebound'),
    ('dreb', 'Defensive Rebound'),
    ('ast', 'Assist'),
    ('stl', 'Steal'),
    ('blk', 'Block'),
    ('tov', 'Turnover'),
    ('pf', 'Personal Foul'),
    ('tf', 'Technical Foul'),
    ('sub_in', 'Substitute In'),
    ('sub_out', 'Substitute Out'),
    ('period_start', 'Start of Period'),
    ('period_end', 'End of Period')
    ]

    stat = models.CharField(max_length=12, choices=STAT_CHOICES)
    period = models.PositiveIntegerField()
    timestamp = models.DurationField()
    linked_statID = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        player_name = self.statline.player.player.first_name + ' ' + self.statline.player.player.last_name
        stat_name = dict(self.STAT_CHOICES)[self.stat]
        timestamp = str(timedelta(seconds=self.timestamp.seconds))
        
        return f"{player_name} - {stat_name} ({timestamp})"