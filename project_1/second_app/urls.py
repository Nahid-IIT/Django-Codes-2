from django.urls import path
from  . import views
urlpatterns = [
    path('contact_me/', views.contact)
]