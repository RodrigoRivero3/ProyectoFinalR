from django.db import models
from django.db import models

class Jugador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    apodo = models.CharField(max_length=30, unique=True)


class Consola(models.Model):
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=30)
    
    


class Juegos(models.Model):
    nombre = models.CharField(max_length=50)
    categoria = models.CharField(max_length=30)
    fecha_salida = models.DateField()



