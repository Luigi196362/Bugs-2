from django.db import models

class Insecto(models.Model):
    nombre = models.TextField(blank=True)
    nomcientifico = models.TextField(blank=True)
    clase = models.TextField(blank=True)
    orden = models.TextField(blank=True)
    familia = models.TextField(blank=True)
    habitat = models.TextField(blank=True)
    dieta = models.TextField(blank=True)
    longitud = models.TextField(blank=True)
    color = models.TextField(blank=True)
    numalas = models.TextField(blank=True)

# Create your models here.
