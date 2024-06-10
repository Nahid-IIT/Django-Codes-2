
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('album/', include('albums.urls')),
    path('musician/', include('musicians.urls')),
    # path('edit/<int:id>', views.edit, name="edit"),
    path('edit/<int:id>', views.Edit.as_view(), name="edit"),
    # path('delete/<int:id>', views.delete, name="delete"),
    path('delete/<int:id>', views.DeleteView.as_view(), name="delete"),
    # path('editAlbum/<int:id>', views.editAlbum, name="editAlbum"),
    path('editAlbum/<int:id>', views.EditAlbum.as_view(), name="editAlbum"),
    # path('deleteAlbum/<int:id>', views.deleteAlbum, name="deleteAlbum")
    path('deleteAlbum/<int:id>', views.DeleteAlbum.as_view(), name="deleteAlbum")

]
