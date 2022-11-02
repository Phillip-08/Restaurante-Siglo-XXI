from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone

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

    def __str__(self):
        return self.nombre
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="producto", null=True)
    categoria = models.ForeignKey(categoria, on_delete=models.PROTECT)
   

    def __str__(self):
        return self.nombre

class Ingredientes(models.Model):
    nombre = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.nombre

class Registro(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    rut = models.IntegerField(null=False, blank=False, primary_key=True)
    nombre_usario = models.CharField(max_length=20, blank= False, null= False)
    comuna = models.CharField(max_length=20)
    telefono = models.IntegerField()
    email = models.EmailField()
    password =models.CharField(max_length=20, blank= False, null= False)
    creacion_usr = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-rut']

    def __str__(self):
        return self.nombre   