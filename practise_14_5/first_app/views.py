from django.shortcuts import render
from . import forms
def form_1(request):
    if request.method=="POST":
        form = forms.Form_1(request.POST)
        if form.is_valid():
             print(form.cleaned_data) 
    else:
        form = forms.Form_1()
    return render(request,'form_1.html', {'form': form})
