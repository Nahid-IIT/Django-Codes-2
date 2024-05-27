from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='homePage'),
    path('about/', views.about, name='aboutPage'),
    path('form/', views.form, name='formPage'),
    path('djangoForm/', views.djangoForm, name='djangoForm'),
    path('studentForm/', views.studentForm, name='studentForm'),
    path('passwordMatching/', views.passwordMatching, name='passwordMatching'),
    
    
]
