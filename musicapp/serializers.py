from dataclasses import field, fields
from pyexpat import model
from statistics import mode
from rest_framework import serializers
from .models import Song, Artiste, Lyric

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = "__all__"

class LyricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lyric
        fields = "__all__"

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = "__all__"