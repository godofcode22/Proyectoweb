from app1 import views
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
 path("admin/",admin.site.urls),
 path("",views.hola),
 path("about/",views.about)
]
