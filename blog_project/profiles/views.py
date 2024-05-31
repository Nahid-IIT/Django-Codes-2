from django.shortcuts import render,redirect
from profiles import forms
def addProfile(request):
    if request.method == 'POST':
        profileForm = forms.ProfileForm(request.POST)
        if profileForm.is_valid():
            profileForm.save()
            return redirect('addProfile')
    else:
        profileForm = forms.ProfileForm()
    return render(request, 'addProfile.html', {'form': profileForm})
