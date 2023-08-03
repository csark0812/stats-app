from . import models
from django.contrib import admin

admin.site.register(models.Player)
admin.site.register(models.Team)
admin.site.register(models.Game)