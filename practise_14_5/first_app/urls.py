from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('form_1/',views.form_1, name="form_1" ),
]
