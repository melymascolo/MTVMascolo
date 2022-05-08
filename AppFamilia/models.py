import email
from django.db import models

class Integrante(models.Model):
    nombre=models.CharField(max_length=60)
    edad=models.IntegerField()
    fechaNac=models.DateField()
    email=models.EmailField()
    profesion=models.CharField(max_length=60)