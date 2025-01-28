from django import forms
from .models import Album, Artist

class AlbumForm(forms.ModelForm):
    # Use Django's built-in ModelForm to create a form for the Album model with corresponding fields
    class Meta:
        model = Album
        fields = ['artist', 'title', 'songs', 'release_date', 'cover']
        # Display a calendar widget for the release_date field
        widgets = {
            'release_date': forms.DateInput(attrs={'type': 'date'}),  # Add the calendar widget
        }


class ArtistForm(forms.ModelForm):
    # Use Django's built-in ModelForm to create a form for the Artist model with corresponding fields
    class Meta:
        model = Artist
        fields = ['name', 'bio']
