from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    title = models.CharField(max_length=255)
    songs = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return self.title
