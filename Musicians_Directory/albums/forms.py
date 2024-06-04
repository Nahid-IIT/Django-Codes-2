from django import forms
from albums import models

class  AlbumForm(forms.ModelForm):
    class Meta:
        model = models.Album
        fields = '__all__'
        widgets = {
            'releseDate': forms.DateInput(attrs={'type': 'date'}),
        }