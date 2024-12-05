from django.shortcuts import render
from django.http import HttpResponse
from django.templatetags.static import static
def hola(request):
    HttpResponse="hello world"
    return(HttpResponse)
def about(request):
    imagen_url = static('sour.jpeg')
    css_url = static('style.css')  # URL del archivo CSS
    favicon_url = static('logo.png')
    musica_url=static('musica.mp3')
    html = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Sour</title>
        <link rel="icon" href="{favicon_url}" type="image/x-icon">
        <!-- Botón para reproducir música -->
        <div style="margin-top: 20px;">
          <button onclick="playMusic()">Reproducir música</button>
        </div>
        <link rel="stylesheet" href="{css_url}">
    </head>
    <body style="text-align: center;">  <!-- Usamos text-align: center en lugar de <center> -->
        <h1>I KNOW YOU GET DEJA VU!</h1>
        <img src="{imagen_url}" alt="Ejemplo de Imagen">
    </body>
    <footer style="font-family: 'Sour Gummy', sans-serif; color:#c209d8; font-size: 1.5em; text-align: center;">
        <p>
            &copy; 2024 Rentadora de trajes Mérida, @Olivia Rodrigo. Todos los derechos reservados.
            <small>La información proporcionada es solo con fines ilustrativos.</small>
        </p>
    </footer>
    <audio id="background-audio" loop>
        <source src="{musica_url}" type="audio/mpeg">
        Tu navegador no soporta el elemento de audio.
     </audio>

     <!-- Script para reproducir la música -->
     <script>
        function playMusic() {{
            var audio = document.getElementById('background-audio');
            audio.currentTime = 40;
            audio.play();
        }}
     </script>
    </html>"""
    
    return HttpResponse(html)


