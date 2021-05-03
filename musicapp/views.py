from django.http import HttpResponse
from django.shortcuts import redirect
from django.db.models import Q

from .models import Song
from .models import User
from .models import Album
from .models import Playlist
from .models import Artist
from .models import Recommendation
from .models import RecommendationType
from .models import UserRating
from .models import UserRatingType
from .models import PlaylistSong
from .models import SongArtist

import os

# user signup - creates a new user
def createUser(request):
    firstName = request.GET.get('fname')
    lastName = request.GET.get('lname')
    email = request.GET.get('email')
    password = request.GET.get('password')
    confirmPassword = request.GET.get('confirm')

    if password != confirmPassword:
        response = "<html><body><h1>Passwords don't match</h1></body></html>"
        return HttpResponse(response)

    user = User.objects.filter(email=email).first()
    if user is not None:
        response = HttpResponse("<html><body><h1>User already found. Please login</h1></body></html>")
        return response
    
    user = User(first_name=firstName, last_name=lastName, email=email, password=password)
    user.save()
   
    response = HttpResponse(status=302)
    response['Location'] = '/musicapp'
    return response

# loads the signup screen
def signup(request):
    currentDir = os.getcwd()
    responseFile = open(currentDir + "/musicapp/views/signup.html", "r")
    response = responseFile.read()
    return HttpResponse(response)

# validates user's login
def login(request):
    email = request.GET.get('email')
    password = request.GET.get('password')

    user = User.objects.filter(email=email).first()

    if user is None or user.password != password:
        response = HttpResponse(status=302)
        response['Location'] = '/musicapp/error'
        return response
    
    request.session['user'] = user.id
    response = HttpResponse(status=302)
    response['Location'] = '/musicapp/dashboard'
    return response

# loads the error page
def error(request):
    currentDir = os.getcwd()
    responseFile = open(currentDir + "/musicapp/views/error.html", "r")
    response = responseFile.read()
    return HttpResponse(response)

# main page of app
def index(request):
    currentDir = os.getcwd()
    responseFile = open(currentDir + "/musicapp/views/login.html", "r")
    response = responseFile.read()
    return HttpResponse(response)

# user's dashboard after logging in with songs, playlist, recommendations
def dashboard(request):
    songs = Song.objects.values()
    body = "<html><body><h1>Your Dashboard</h1><br>"

    currentDir = os.getcwd()
    searchHTML = open(currentDir + "/musicapp/views/search.html", "r")
    searchComponent = searchHTML.read()

    body += searchComponent
    
    songsList = "<ul>"
    for song in songs:
        songURL = "/musicapp/song/" + str(song['id'])
        songsList = songsList + "<li><a href=" + songURL + ">" + song['title'] + "</li>" 
    songsList += "</ul>"
    
    body = body + songsList + "</body></html>"
    return HttpResponse(body)

# searches by song/album/playlist/artist
def search(request):
    keyword = request.GET.get('keyword')
    songs = Song.objects.filter(title__icontains=keyword).values()
    songsInAlbums = Song.objects.filter(album__name__icontains=keyword).values()
    songsInGenres = Song.objects.filter(genre__name__icontains=keyword).values()
    songsInPlaylists = PlaylistSong.objects.filter(Q(song__title__icontains=keyword)|Q(playlist__name__icontains=keyword)).select_related().all()
    songsByArtists = SongArtist.objects.filter(song__title__icontains=keyword).select_related().values()
    
    result = list()

    for song in songs:
        result.append(song['title'])
    
    for song in songsInAlbums:
        result.append(song['title'])
    
    for song in songsInGenres:
        result.append(song['title'])

    for song in songsInPlaylists:
        result.append(song.song.title)
    
    for song in songsByArtists:
        result.append(song.song.title)

    body = "<html><body>"
    formattedResult = "<ul>"
    for resultEntry in result:
        formattedResult = formattedResult + "<a href='www.google.com'><li>" + resultEntry + "</li>" 
    formattedResult += "</ul>"
    
    body = body + formattedResult + "</body></html>"
    return HttpResponse(body)

# recommends a song to another user
def recommend(request):
    recommendedBy = User.objects.filter(id=request.session['user']).first()
    song = request.session['currentsong']

    email = request.GET.get('email')
    recommendedTo = User.objects.filter(email=email).first()
    recommendationType = RecommendationType.SONG

    recommendation = Recommendation(
        recommended_by=recommendedBy,
        recommended_to=recommendedTo,
        type=recommendationType,
        item_id=song
    )
    recommendation.save()

    return HttpResponse("Recommendation added")

# lists all playlists available for user
def playlists(request):
    user = request.session['user']
    playlists = Playlist.objects.filter(Q(user_id__isnull=True) | Q(user_id=user)).values()
    body = "<html><body><h1>Your Playlists</h1><br>"

    currentDir = os.getcwd()
    searchHTML = open(currentDir + "/musicapp/views/playlist.html", "r")
    playlistComponent = searchHTML.read()

    body += playlistComponent
    
    playlistsResponse = "<ul>"
    for playlist in playlists:
        playlistsResponse = playlistsResponse + "<li>" + playlist['name'] + "</li>" 
    playlistsResponse += "</ul>"
    
    body = body + playlistsResponse + "</body></html>"
    return HttpResponse(body)

# lists all recommendation given for the user
def recommendations(request):
    user = request.session['user']
    recommendations = Recommendation.objects.filter(recommended_to=user).select_related().all()
    body = "<html><body><h1>Your Recommendations</h1><br>"
    
    recommendationsResponse = "<ul>"
    for recommendation in recommendations:
        song = Song.objects.filter(id=recommendation.item_id).first()
        recommendationsResponse = recommendationsResponse + "<li>" +  str(recommendation.recommended_by) + " recommended " + song.title + " </li>" 
    recommendationsResponse += "</ul>"
    
    body = body + recommendationsResponse + "</body></html>"
    return HttpResponse(body)

# creates a playlist
def createPlaylist(request):
    userRec = User.objects.filter(id=request.session['user']).first()
    name = request.GET.get('name')

    playlist = Playlist(name=name, user=userRec)
    playlist.save()
    return HttpResponse("Creates Playlist.")

# adds the song to the playlist
def addSongToPlaylist(request):
    playlist = Playlist.objects.filter(name=request.GET.get('playlist')).first()
    song = Song.objects.filter(id=request.session['currentsong']).first()

    playlistSong = PlaylistSong(playlist=playlist, song=song)
    playlistSong.save()
    return HttpResponse("Song added to playlist.")

# rates a given song
def rate(request):
    song = request.session['currentsong']
    user = request.session['user']
    ratingVal = request.GET.get('rating')

    rating = UserRating.objects.filter(type=UserRatingType.SONG, item_id=song, user=user).first()
    if rating is None:
        userRec = User.objects.filter(id=user).first()
        rating = UserRating(
            user=userRec,
            type=UserRatingType.SONG,
            item_id=song,
            rating=ratingVal
        )
    else:
        rating.rating = ratingVal
    
    rating.save()
    return HttpResponse("Rating saved")

# displays a song's information
def getSong(request, id):
    song = Song.objects.filter(id=id).first()
    
    currentDir = os.getcwd()
    songView = open(currentDir + "/musicapp/views/song.html", "r")
    songView = songView.read()
    response = "<html><body><h1>" + song.title + "</h1><br><br>"
    songLink = "<a href='" + song.file_location + "'>Listen</a><br><br>"
    response = response + songLink + songView + "</body></html>"
    request.session['currentsong'] = song.id

    return HttpResponse(response)