from django.shortcuts import render, redirect
from .models import Album, Artist
from .forms import AlbumForm, ArtistForm

def index(request):
    '''Renders the home page with a list of all albums'''
    # Get all albums from the database and store them in a variable
    albums = Album.objects.all()
    # Create a context dictionary to pass the albums to the template
    context = {'albums': albums}
    # Render the template with the context data 
    return render(request, 'main/index.html', context)

def add_album(request):
    '''Renders a form to add a new album to the database'''
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        # use Django's built-in form validation
        if form.is_valid():
            form.save()
            return redirect('home')
    # If the form has not been submitted yet, render the form (GET request)
    else:
        form = AlbumForm()
    # Render the form by passing it in the context dictionary
    return render(request, 'main/add_album.html', {'form': form})

def add_artist(request):
    '''Renders a form to add a new artist to the database'''
    # Check if the form has been submitted with a POST request
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        # use Django's built-in form validation
        if form.is_valid():
            form.save()
            return redirect('home')
    # If the form has not been submitted yet, render the form (GET request)
    else:
        form = ArtistForm()
    # Render the form by passing it in the context dictionary
    return render(request, 'main/add_artist.html', {'form': form})
