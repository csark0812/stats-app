from rest_framework import serializers
from . import models

class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.League
        fields = '__all__'

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Season
        fields = '__all__'

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Division
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Team
        fields = '__all__'

class TeamSeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TeamSeason
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Player
        fields = '__all__'

class PlayerSeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PlayerSeason
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Game
        fields = '__all__'

class StatLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StatLine
        fields = '__all__'

class RecordedStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RecordedStat
        fields = '__all__'