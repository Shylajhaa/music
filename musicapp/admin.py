from django.contrib import admin
from .models import User
from .models import Artist
from .models import Album
from .models import Song
from .models import Playlist
from .models import Recommendation
from .models import Genre
from .models import UserRating
from .models import SongArtist
from .models import PlaylistSong

# Register your models here.
admin.site.register(User)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(PlaylistSong)
admin.site.register(Recommendation)
admin.site.register(SongArtist)
admin.site.register(Genre)
admin.site.register(UserRating)