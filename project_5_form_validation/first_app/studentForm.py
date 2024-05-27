from django import forms
from django.core import validators
# class StudentForm(forms.Form):
#     name = forms.CharField(label='Name', widget=forms.TextInput)
#     email = forms.EmailField(label='Email', widget=forms.EmailInput)
    
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError("Enter a name with at least 10 characters")
    #     else:
    #         return valname
    
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
       
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Yout email must contain .com')
    #     else:
    #         return valemail
    
    #  Short Technique 
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
        
    #     if len(valname) < 10:
    #         raise forms.ValidationError('Enter at least 10 characters')
        
    #     if '.com' not in valemail:
    #         raise forms.ValidationError('Eamil must contain .com ')
    
    
class StudentForm(forms.Form):
    name = forms.CharField(label='Name', widget=forms.TextInput, validators=[validators.MinLengthValidator(10, message="Enter at least 10 character")])
    email = forms.EmailField(label='Email', widget=forms.EmailInput, validators=[validators.EmailValidator])
    age = forms.CharField(label='Age', widget=forms.NumberInput)
    file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf','png'], message="Provide PDF only")])
    