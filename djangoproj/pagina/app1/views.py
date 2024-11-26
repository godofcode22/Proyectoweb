from django.shortcuts import render
from django.http import HttpResponse
def hola(request):
    return HttpResponse("Hello world!")
def about(request):
    return HttpResponse("<h1>About</h1>")

# Create your views here.
