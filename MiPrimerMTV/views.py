from django.http import HttpResponse
from django.template import Template, Context

def saludo(resquest):
    return HttpResponse("Conociendo a mi familia")

def bienvenido(request):
    html = open("C:/Users/Melany/Desktop/Entrega/MiPrimerMTV/MiPrimerMTV/templates/bienvenido.html")
    plantilla = Template(html.read())

    html.close()
    contexto = Context()
    texto = plantilla.render(contexto)
    return HttpResponse(texto)


