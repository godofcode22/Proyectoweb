from django.shortcuts import render
from django.http import HttpResponse

def hola(request):
    contenido_html = """
    <div style="text-align: center; margin-top: 20px;">
        <!-- Botón -->
        <button style="padding: 10px 20px; font-size: 16px; background-color: blue; color: white; border: none; border-radius: 5px; cursor: pointer;">
            Haz clic aquí
        </button>
        
        <!-- Espaciado -->
        <div style="margin-top: 20px;"></div>
        
        <!-- Imagen -->
<img src="/static/images/imagen.png" alt="Imagen local" 
        style="border: 2px solid black; border-radius: 50px; width: 300px; height: auto;">
        <p>.A mi me vale verga</p> 
    </div>
    """
    return HttpResponse(contenido_html)

