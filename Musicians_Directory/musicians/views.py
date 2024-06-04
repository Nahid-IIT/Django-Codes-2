from django.shortcuts import render,redirect
from .forms import MusicianForm
# Create your views here.

def addMusician(request):
    if request.method=="POST":
       form = MusicianForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect('addMusician')
    else:
        form = MusicianForm()
    return render(request, 'addMusician.html', {'form': form})
    