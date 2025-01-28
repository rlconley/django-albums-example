from django.db import models

class Artist(models.Model):
    '''Represents an artist (individual or group) who has released albums. 
    No two artists can have the same name. If artists collaborate on an album together, 
    the group is its own instance of Artist (i.e. Simon & Garfunkel and Paul Simon are 
    separate instances of Artist).'''   
    name = models.CharField(max_length=255, unique=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        '''returns a string representation of the artist'''
        return self.name


class Album(models.Model):
    '''Represents an album released by an artist. An album can have multiple songs, 
    listed as text. An album can have one artist. Aut an artist can have many albums'''
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    title = models.CharField(max_length=255)
    songs = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    notes_as_json = models.JSONField(blank=True, null=True)

    def __str__(self):
        '''returns a string representation of the album'''
        return self.title
