from django.shortcuts import render,redirect
from .forms import MusicianForm
from .models import Musician
from django.views.generic import CreateView
from django.urls import reverse_lazy
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
    
class AddMusician(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'addMusician.html'
    success_url = reverse_lazy('addMusician')
    def form_valid(self, form):
        return super().form_valid(form)