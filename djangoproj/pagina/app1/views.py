from django.shortcuts import render
from django.http import HttpResponse
def hola(request):
    return HttpResponse("Le rasco el chile</h1>")

# Create your views here.
