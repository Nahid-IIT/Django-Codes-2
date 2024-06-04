
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('album/', include('albums.urls')),
    path('musician/', include('musicians.urls')),
    path('edit/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('editAlbum/<int:id>', views.editAlbum, name="editAlbum"),
    path('deleteAlbum/<int:id>', views.deleteAlbum, name="deleteAlbum")

]
