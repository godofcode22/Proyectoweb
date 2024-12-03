from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static
def hola(request):

    return HttpResponse("<h1>Hello world!</h1>")

def about(request):
    imagen_url = static('sour.jpeg')
    css_url = static('style.css')  # URL del archivo CSS
    favicon_url=static('logo.png')

    html = f"""
     <!DOCTYPE html>
     <html lang="es">
     <head>
     <meta charset="UTF-8">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <title>Sour</title>
     <link rel="icon" href="{favicon_url}" type="image/x-icon">
     <!-- Aquí conectamos el CSS -->
     <link rel="stylesheet" href="{css_url}">
     </head>
     <body>
     <center>
        <h1>I KNOW YOU GET DEJA VU!</h1>
        <img src="{imagen_url}" alt="Ejemplo de Imagen">
     </center>
     </body>
     </html>"""
    return HttpResponse(html)
# Create your views here.

