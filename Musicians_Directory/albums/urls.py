
from django.contrib import admin
from django.urls import path,include
from albums import views
urlpatterns = [
    path('addAlbum/', views.addAlbum, name="addAlbum"),
]
