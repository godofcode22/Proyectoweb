from app1 import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
 
 path("",views.hola),
 path("about/",views.about)
]

