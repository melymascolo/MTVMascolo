from django.shortcuts import render
from .models import Integrante
from django.template import Context, Template
from django.http import HttpResponse
from django.template import loader

def integrante(self):
    integrante = Integrante(nombre="Roxana", edad=59, fechaNac="1964-07-24", email="roxana_2407@gmail.com", profesion="Ama de casa")
    integrante.save()
    diccionario = {"familiar":integrante}

    plantilla = loader.get_template('familiar.html')
    texto = plantilla.render(diccionario)
    return HttpResponse(texto)