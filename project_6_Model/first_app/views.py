from django.shortcuts import render, redirect
from . import models
def home(request):
    student  = models.Student.objects.all()
    print(student)
    return render(request, 'home.html',{'data':student})


def deleteStudent(request,roll):
     delete_student  = models.Student.objects.get(pk = roll).delete()
     return redirect("homePage")

    
    
