from django.urls import path
from task import views
urlpatterns = [
    path('add/',views.addTask, name = "addTask")
]
