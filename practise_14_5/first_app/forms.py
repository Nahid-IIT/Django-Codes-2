from django import forms
import datetime
class Form_1(forms.Form):
    name = forms.CharField()
    content  = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField(label="Enter your Email")
    agree = forms.BooleanField()
    date = forms.DateField(widget=forms.NumberInput(attrs={'type':'date'}))
    birth_year = ['1990', '1991', '1980', '2004']
    birthdate = forms.DateField(widget=forms.SelectDateWidget(years=birth_year))
    # vaule = forms.DecimalField(label="Decimal Value", widget=forms.DecimalField(attrs={'placeholder':"enter decimal value"}))
    first_name = forms.CharField(initial="Nahid")
    day = forms.DateField(initial=datetime.date.today)
    color = [
        ('s',"S"),
        ('m',"M"),
        ('l',"L"),
        ('xl',"XL"),
        ('xxl',"XXL")
    ]
    
    Size  = forms.ChoiceField(choices=color)
    Size_radio = forms.ChoiceField(widget=forms.RadioSelect, choices=color)
    Multiple  = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=color)