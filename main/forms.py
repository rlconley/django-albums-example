from django import forms
from .models import Album, Artist

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['artist', 'title', 'songs', 'release_date', 'cover']
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),  # Add the calendar widget
        }


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name', 'bio']
