from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    return HttpResponse("This is second_app contact page")
