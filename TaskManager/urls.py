from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(route = 'admin/', view = admin.site.urls),
    path(route = '', view = include("tasks.urls")),
]
