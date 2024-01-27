from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path(route = 'admin/', view = admin.site.urls),
    path(route= '',  view = home, name = "home"),
    path(route= 'login/', view = login, name = "login"),
    path(route= 'signup/', view = signup, name = "signup"),
    path(route= 'modify_task', view = modify_task, name = "modify_task"),
    path(route= 'delete', view = delete_task, name = "delete_task"),
    path(route= 'search', view = search, name = "search"),
]
