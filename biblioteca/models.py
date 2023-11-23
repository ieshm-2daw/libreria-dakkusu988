from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser

""" Referencia por si me hace falta algo
class Biblioteca(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    rating = models.IntegerField(validators = [MinValueValidator(0), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
"""

class Usuario(AbstractUser):
    DNI = models.CharField(max_length=9)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField(validators = [MinValueValidator(0)])

    def __str__(self):
        return self.dni
    
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=9)
    fecha_publicacion = models.CharField(max_length=50)
    genero = models.IntegerField(validators = [MinValueValidator(0)])
    ISBN = models.IntegerField(validators = [MinValueValidator(0)])
    resumen = models.IntegerField(validators = [MinValueValidator(0)])
    disponibilidad = models.IntegerField(validators = [MinValueValidator(0)]) # (posibles valores: disponible, prestado, en proceso de préstamo)
    portada = models.ImageField(validators = [MinValueValidator(0)])

    def __str__(self):
        return self.titulo