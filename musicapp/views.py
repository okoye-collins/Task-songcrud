from cProfile import run
from django.shortcuts import get_object_or_404, render
from django.urls import is_valid_path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import SongSerializer, ArtisteSerializer
from .models import Artiste, Song
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'List of Song': '/songs',
        'List of Artist': '/artist',
        'Song Detail': '/songs/song-pk',
        'Update song': 'songs/song-pk/update',
        'Delete': '/songs/song-pk/delete'
    }
  
    return Response(api_urls)

@api_view(['GET'])
def ArtistsList(request):
    artiste = Artiste.objects.all()
    serializer = ArtisteSerializer(artiste, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def SongList(request):
    song = Song.objects.all()
    serializer = SongSerializer(song, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def SongDetail(request, id):
    song = Song.objects.filter(id=id)
    serializer = SongSerializer(song.first(), many=False)
    return Response(serializer.data)

@api_view(['POST'])
def UpdateSong(request, id):
    song = Song.objects.get(id=id)
    data = SongSerializer(instance=song, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    return Response(data.data)

@api_view(['DELETE'])
def DeleteSong(request, id):
    song = get_object_or_404(Song, id=id)
    song.delete()
    return Response(status=status.HTTP_202_ACCEPTED)