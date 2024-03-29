# Generated by Django 3.0.2 on 2021-05-01 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0008_auto_20210501_1848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='playlist',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='playlistsong',
            old_name='playlist_id',
            new_name='playlist',
        ),
        migrations.RenameField(
            model_name='playlistsong',
            old_name='song_id',
            new_name='song',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='album_id',
            new_name='album',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='genre_id',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='songartist',
            old_name='artist_id',
            new_name='artist',
        ),
        migrations.RenameField(
            model_name='songartist',
            old_name='song_id',
            new_name='song',
        ),
        migrations.RenameField(
            model_name='userrating',
            old_name='user_id',
            new_name='user',
        ),
    ]
