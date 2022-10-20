from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Artiste)
admin.site.register(models.Song)
admin.site.register(models.Lyric) 