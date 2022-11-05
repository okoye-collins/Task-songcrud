from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('', views.ApiOverview),
    path('artists/', views.ArtistsList, name="artists"),
    path('songs/', views.SongList, name="songs"),
    path('songs/<int:id>', views.SongDetail, name="songs-id"),
    path('songs/<int:id>/update', views.UpdateSong),
    path('songs/<int:id>/delete', views.DeleteSong),

]
