from django.shortcuts import render,redirect
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
