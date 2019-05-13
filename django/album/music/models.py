from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=200)
    album_title = models.CharField(max_length=1000)
    genre = models.CharField(max_length=50)
    def __str__(self):
        return self.artist + ' - ' + self.album_title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=200)
    file_type = models.CharField(max_length=10)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title