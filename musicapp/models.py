from django.utils import timezone
from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()

class Song(models.Model):
    title = models.CharField(max_length=200)
    date_released = models.DateTimeField(default=timezone.now)
    likes = models.PositiveIntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)