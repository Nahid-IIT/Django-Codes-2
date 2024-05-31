from django.shortcuts import render, redirect
from authors import forms
# Create your views here.

def addAuthor(request):
    if request.method == "POST":
        authorForm = forms.AuthorForm(request.POST)
        if authorForm.is_valid():
            authorForm.save()
            return redirect('addAuthor')
    else:
        authorForm= forms.AuthorForm()
    return render(request,  'addAuthor.html', {'form':authorForm})