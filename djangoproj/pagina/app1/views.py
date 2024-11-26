from django.shortcuts import render
from django.http import HttpResponse
def hola(request):
    return HttpResponse("<h1>Hello world!</h1>")

def about(request):
    return HttpResponse("about")
# Create your views here.

