from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

opciones_consultas = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"]
]
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self) -> str:
        return self.nombre


class categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def _str_(self):
        return self.nombre
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    ingredientes = models.CharField(max_length=100)
    categoria = models.ForeignKey(categoria, on_delete=models.PROTECT)

    def _str_(self):
        return self.nombre

class Ingredientes(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def _str_(self):
        return self.nombre