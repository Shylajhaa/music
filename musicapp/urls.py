from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('search', views.search, name='search'),
    path('login', views.login, name='login'),
    path('song/recommend', views.recommend, name='recommend'),
    path('playlist-create', views.createPlaylist, name='createPlaylist'),
    path('song/playlist-add', views.addSongToPlaylist, name='addSongToPlaylist'),
    path('song/rate', views.rate, name='rate'),
    path('error', views.error, name='error'),
    path('song/<int:id>', views.getSong, name='getSong'),
    path('signup', views.signup, name='signup'),
    path('createUser', views.createUser, name='createUser'),
    path('playlists', views.playlists, name='playlists'),
    path('recommendations', views.recommendations, name='recommendations')
]