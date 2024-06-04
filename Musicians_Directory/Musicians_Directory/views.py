from django.shortcuts import render,redirect
from musicians.models import Musician
from musicians.forms import MusicianForm
from albums.models import Album
from albums.forms import AlbumForm

def home(request):
    data = Album.objects.all()
    return render(request, 'home.html', {'form': data})

def edit(request, id):
    post  = Musician.objects.get(pk=id)
    form = MusicianForm(instance=post)
    if request.method =="POST":
        form = MusicianForm(request.POST,  instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'addMusician.html',{'form': form})
 
        
def delete(request, id):
    post = Musician.objects.get(pk=id).delete()
    return redirect('home')


def editAlbum(request, id):
    album = Album.objects.get(pk=id)
    form = AlbumForm(instance=album)
    if request.method =="POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'addAlbum.html', {'form':form})

def deleteAlbum(request, id):
    album = Album.objects.get(pk=id).delete()
    return redirect('home')