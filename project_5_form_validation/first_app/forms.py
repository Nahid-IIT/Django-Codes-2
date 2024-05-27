from django import forms
# widgets == filed to html input 

class ContacForm(forms.Form):
     name = forms.CharField(label="User Name", initial='Nahid', help_text='Enter your full Name', required=False, disabled=False,widget=forms.Textarea(attrs={'id':'text-area', 'class': 'class-1 class-2','placeholder':'Enter your full Name'}))
     # file = forms.FileField()
     # img = forms.ImageField()
     # email = forms.EmailField(label="User Email ")
     # age = forms.IntegerField(label = "Enter Age")
     age = forms.CharField(widget=forms.NumberInput)
     weight = forms.FloatField()
     balance = forms.DecimalField()
     check = forms.BooleanField()
     birthdate = forms.DateField(widget=forms.DateInput(attrs = {'type':'date'}))
     appoinment =  forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
     CHOISE = [('S', 'Small'), ('M', 'Medium'), ('L', 'Large')]
     size = forms.ChoiceField(choices=CHOISE, widget=forms.RadioSelect)
     MEAL = [('P','Peperoni'), ('M','Mashroom'), ('B', 'Beef')]
     pizza = forms.MultipleChoiceField(choices = MEAL, widget=forms.CheckboxSelectMultiple)
     