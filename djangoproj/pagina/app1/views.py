from django.shortcuts import render
from django.http import HttpResponse
def hola(request):
    return HttpResponse("Hello world!</h1>")

# Create your views here.

