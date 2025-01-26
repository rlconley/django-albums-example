from django.shortcuts import render
from .models import Album

def index(request):
    albums = Album.objects.all()
    return render(request, 'main/index.html', {'albums': albums})
