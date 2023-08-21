from . import models
from django_filters import rest_framework as filters

class LeagueFilter(filters.FilterSet):
    class Meta:
        model = models.League
        fields = {
            'league_id': ['exact'],
            'name': ['exact', 'icontains'],
            'is_open': ['exact'],
        }

class SeasonFilter(filters.FilterSet):
    class Meta:
        model = models.Season
        fields = {
            'season_id': ['exact'],
            'league': ['exact'],
            'name': ['exact', 'icontains'],
            'is_complete': ['exact'],
        }

class TeamFilter(filters.FilterSet):
    class Meta:
        model = models.Team
        fields = {
            'team_id': ['exact'],
            'league': ['exact'],
            'name': ['exact', 'icontains'],
            'abbreviation': ['exact', 'icontains'],
        }