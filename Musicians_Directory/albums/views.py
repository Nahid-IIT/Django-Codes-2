from django.shortcuts import render,redirect
from albums.forms import AlbumForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from albums.models import Album
from albums.forms import AlbumForm
def addAlbum(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addAlbum')
    else:
        form = AlbumForm()
    return render(request,'addAlbum.html',{'form':form})

class AddAlbum(CreateView):
    model  = Album
    form_class = AlbumForm
    template_name = 'addAlbum.html'
    success_url = reverse_lazy('addAlbum')
    def form_valid(self, form):
        return super().form_valid(form)