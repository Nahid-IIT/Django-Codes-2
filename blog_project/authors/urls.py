
from django.contrib import admin
from django.urls import path, include
from authors.views import addAuthor
urlpatterns = [
     path('add/', addAuthor, name ="addAuthor"),
]
