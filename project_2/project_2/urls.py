
from django.contrib import admin
from django.urls import path,include
from project_2 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_1/', include('app_1.urls')),
    path('', views.index)
]
