
from django.contrib import admin
from django.urls import path,include
from musicians import views
urlpatterns = [
    # path('addMusician/', views.addMusician, name = "addMusician"),
    path('addMusician/', views.AddMusician.as_view(), name = "addMusician"),
]
