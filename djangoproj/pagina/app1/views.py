from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static
def hola(request):

    return HttpResponse("<h1>Hello world!</h1>")

def about(request):
    imagen_url = static('sour.jpeg')
    
    print(imagen_url)
    html=(f"""
        <center>
        <h1><font color='c209d8'>I KNOW YOU GET DEJA VU!</font></h1>
        <img src="{imagen_url}" alt="Ejemplo de Imagen" style="width: 300px; height:300px">
        </center>
    """)
    return HttpResponse(html)
# Create your views here.

