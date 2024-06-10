from django.shortcuts import render,redirect
from musicians.models import Musician
from musicians.forms import MusicianForm
from albums.models import Album
from albums.forms import AlbumForm
from django.views.generic import UpdateView,DeleteView
from django.urls import reverse_lazy
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
 
class Edit(UpdateView):
    model = Musician
    form = MusicianForm
    template_name = 'addMusician.html'
    success_url = reverse_lazy('home')
        
def delete(request, id):
    post = Musician.objects.get(pk=id).delete()
    return redirect('home')

class Delete(DeleteView):
    model = Musician
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'

def editAlbum(request, id):
    album = Album.objects.get(pk=id)
    form = AlbumForm(instance=album)
    if request.method =="POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'addAlbum.html', {'form':form})

class EditAlbum(UpdateView):
    model= Album
    form_class = AlbumForm
    template_name='addAlbum.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
    
def deleteAlbum(request, id):
    album = Album.objects.get(pk=id).delete()
    return redirect('home')

class DeleteAlbum(DeleteView):
    model = Album
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg= 'id'