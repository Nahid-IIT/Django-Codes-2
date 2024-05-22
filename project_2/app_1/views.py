from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("This is home page")
    return render(request, 'app_1/home.html')
