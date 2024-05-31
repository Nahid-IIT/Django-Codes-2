
from django.contrib import admin
from django.urls import path, include
from profiles.views import addProfile
urlpatterns = [
     path('add/', addProfile, name="addProfile")
]
