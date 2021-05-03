## DB Design
-------------
users
	id
	name
	email
	password (hashed)

albums
	id
	name

genres
	id
	name

artists
	id
	name

songs
	id
	title
	file
	genre_id
	album_id

songs_artists
	id
	song_id
	artist_id

playlists
	id
	name
	user_id (Allow NULL - in case of recommended playlists)

playlists_songs
	id
	playlist_id
	song_id

recommendations
	id
	recommended_by
	recommended_to
	type (playlist, album, song)
	item_id

users_ratings
	id
	user_id
	type (playlist, album, song - if in future song rating is extended)
	item_id
	rating


## Components
---------------
* Login/Signup - Done
* Search module (search by genre, album, artist, playlist) - Done
* Listen to songs
* Recommendations - Done
	* View
	* Create
* Playlists - Done
	* View
	* Create
* Rating - Done
	* Rate songs/Edit past ratings
* Dashboard/Feed with system generated playlists/recommended songs/genres/artists


## Installation Steps
-----------------------
* Setup db credentials in settings.py
* In the project's directory (i.e. ``music``)
	* Run ``python manage.py migrate``
	* Setup test data
		* Run ``python manage.py shell < musicapp/populate_data.py``
* Open <host>/musicapp to access the application