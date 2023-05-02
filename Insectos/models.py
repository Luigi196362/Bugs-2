from django.db import models

class Insecto(models.Model):
    nombre = models.TextField(default='',blank=False)
    nomcientifico = models.TextField(default='',blank=False)
    clase = models.TextField(default='',blank=False)
    orden = models.TextField(default='',blank=False)
    familia = models.TextField(default='',blank=False)
    habitat = models.TextField(default='',blank=False)
    dieta = models.TextField(default='',blank=False)
    longitud = models.TextField(default='',blank=False)
    color = models.TextField(default='',blank=False)
    numalas = models.TextField(default='',blank=False)

# Create your models here.
