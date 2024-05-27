from django.shortcuts import render
from .forms import ContacForm
from .studentForm import StudentForm
from .passwordMatching import PasswordMatching
def home(request):
    return render(request, 'home.html')


def about(request):
    if request.method =='POST':
        name = request.POST.get('userName')
        email = request.POST.get('email')
        select  = request.POST.get('select')
        return render(request, 'about.html', {'name': name , 'email': email,'select':select})
    else:
        return render(request,'about.html')

def form(request):
        return render(request,'form.html')

def djangoForm(request):
    if request.method=='POST':
        form=ContacForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # img = form.cleaned_data['img']
            
            # # to save files 
            # with open('./first_app/upload/' +file.name ,'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            
            # # to save image     
            # with open('./first_app/Media/images/' +img.name ,'wb+') as destination:
            #     for chunk in img.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
            # return render(request,'djangoForm.html', {'form': form})
    else:
        form = ContacForm()
    return render(request,'djangoForm.html', {'form': form})


def studentForm(request):
    if request.method=="POST":
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = StudentForm()
    return render(request, 'studentForm.html', {'form':form})
    
def passwordMatching(request):
    if request.method == 'POST':
        form = PasswordMatching(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = PasswordMatching()
    return render(request, 'passwordMatching.html', {'form': form})
        