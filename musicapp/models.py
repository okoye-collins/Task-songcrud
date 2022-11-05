from email.policy import default
from django.utils import timezone
from django.db import models

# Create your models here.
class Artiste(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f'Artist {self.first_name} {self.last_name}'

class Song(models.Model):
    title = models.CharField(max_length=200)
    date_released = models.DateTimeField(default=timezone.now)
    likes = models.PositiveIntegerField()
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    def __str__(self):
        return f'Title {self.title} by {self.artiste_id.first_name}' 

class Lyric(models.Model):
    content = models.TextField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)

    def __str__(self):
        return f'Lyric content for {self.song_id.title} music by {self.song_id.artiste_id.first_name}'