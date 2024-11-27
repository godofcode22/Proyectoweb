from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static
def hola(request):

    return HttpResponse("<h1>Hello world!</h1>")

def about(request):
    imagen_url = static('descarga.jpeg')
    print(imagen_url)
    html=(f"""
        <h1>About</h1>
        <img src="{imagen_url}" alt="Ejemplo de Imagen" style="width: 300px;">
    """)
    return HttpResponse(html)
# Create your views here.

