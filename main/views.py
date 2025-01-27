from django.shortcuts import render, redirect
from .models import Album, Artist
from .forms import AlbumForm, ArtistForm

def index(request):
    albums = Album.objects.all()
    return render(request, 'main/index.html', {'albums': albums})

def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AlbumForm()
    return render(request, 'main/add_album.html', {'form': form})

def add_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ArtistForm()
    return render(request, 'main/add_artist.html', {'form': form})
