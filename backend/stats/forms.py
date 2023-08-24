from django import forms
from . import models

class PlayerForm(forms.ModelForm):
    class Meta:
        model = models.Player
        fields = ['first_name', 'last_name', 'jersey_number', 'height', 'team', 'position']
