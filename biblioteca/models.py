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
    dni = models.CharField(max_length=9)
    direccion = models.CharField(max_length=50)
    telefono = models.IntegerField(validators = [MinValueValidator(0)])

    def __str__(self):
        return self.dni