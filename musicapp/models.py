from django.db import models
from enum import Enum

# Enums

class RecommendationType(Enum):
    PLAYLIST = 'Playlist'
    ALBUM = 'Album'
    SONG = 'Song'

class UserRatingType(Enum):
    PLAYLIST = 'Playlist'
    ALBUM = 'Album'
    SONG = 'Song'

# Models

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
         return self.first_name + ' ' + self.last_name

class Album(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
         return self.name

class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
         return self.name

class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
         return self.name

class Song(models.Model):
    title = models.CharField(max_length=200)
    file_location = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    album = models.ForeignKey(Album, on_delete=models.PROTECT)

    def __str__(self):
         return self.title

class Playlist(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)

    def __str__(self):
         return self.name

class Recommendation(models.Model):
    recommended_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='recommended_by')
    recommended_to = models.ForeignKey(User, on_delete=models.PROTECT, related_name='recommended_to')
    type = models.CharField(
      max_length=100,
      choices=[(key, key.value) for key in RecommendationType]
    )
    item_id = models.IntegerField()

class SongArtist(models.Model):
    song = models.ForeignKey(Song, on_delete=models.PROTECT)
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT)

class PlaylistSong(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.PROTECT)
    song = models.ForeignKey(Song, on_delete=models.PROTECT)

class UserRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    type = models.CharField(
      max_length=100,
      choices=[(key, key.value) for key in UserRatingType]
    )
    item_id = models.IntegerField()
    rating = models.IntegerField()