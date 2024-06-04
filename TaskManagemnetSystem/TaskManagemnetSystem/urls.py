from django.contrib import admin
from django.urls import path, include
from .views import home,showTask,deleteTask,editTask
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('showTask/', showTask, name="showTask"),
    path('editTask/<int:id>', editTask, name="editTask"),
    path('deleteTask/<int:id>', deleteTask, name="deleteTask"),
    path('task/', include('task.urls')),
    path('category/', include('category.urls')),
]
