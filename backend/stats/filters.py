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