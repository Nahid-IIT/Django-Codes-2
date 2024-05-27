from django import forms 
from django.core import validators

class PasswordMatching(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs = {'placeholder': 'Enter your name'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}))
    confirmPassword = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Retype password'}))
    
    def clean(self):
        cleaned_data = super().clean()
        valName = self.cleaned_data['name']
        password  = self.cleaned_data['password']
        rePassword  = self.cleaned_data['confirmPassword']
        if password != rePassword:
            raise forms.ValidationError("Password dosen't match")
        if len(valName) <10:
            raise forms.ValidationError('Name must be at least 10 chars')