import os
import csv

from musicapp.models import Album
from musicapp.models import Artist
from musicapp.models import Genre
from musicapp.models import Playlist
from musicapp.models import Song

separator = os.path.sep

currentDir = os.getcwd()
dataDir = currentDir + separator + 'musicapp' + separator + 'data' + separator

print("Hello World")
albumsFile = dataDir + 'albums.csv'
artistsFile = dataDir + 'artists.csv'
genresFile = dataDir + 'genres.csv'
playlistsFile = dataDir + 'playlists.csv'
songsFile = dataDir + 'songs.csv'

with open(albumsFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lineNum = 0
    for row in csv_reader:
        if lineNum != 0:
            album = Album(name=row[0])
            album.save()

        lineNum += 1

print("Populated " + str(lineNum-1) + " albums")

with open(artistsFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lineNum = 0
    for row in csv_reader:
        if lineNum != 0:
            artist = Artist(name=row[0])
            artist.save()

        lineNum += 1

print("Populated " + str(lineNum-1) + " artists")

with open(genresFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lineNum = 0
    for row in csv_reader:
        if lineNum != 0:
            genre = Genre(name=row[0])
            genre.save()

        lineNum += 1

print("Populated " + str(lineNum-1) + " genres")

with open(playlistsFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lineNum = 0
    for row in csv_reader:
        if lineNum != 0:
            playlist = Playlist(name=row[0])
            playlist.save()

        lineNum += 1

print("Populated " + str(lineNum-1) + " playlists")

with open(songsFile) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    lineNum = 0
    for row in csv_reader:
        if lineNum != 0:
            genre = Genre.objects.filter(name=row[2]).first()
            album = Album.objects.filter(name=row[3]).first()
            song = Song(title=row[0], file_location=row[1], genre=genre, album=album)
            song.save()

        lineNum += 1
    
print("Populated " + str(lineNum-1) + " songs")