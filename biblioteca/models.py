from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    DNI = models.CharField(max_length=9)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.DNI

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    sitio_web = models.URLField()  # Cambiado a un campo URL para el sitio web

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField(max_length=100)
    foto = models.ImageField(upload_to='')  # Campo para cargar la foto de perfil

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    DISPONIBILIDAD_VALORES = (
        ('disponible', 'Disponible'),
        ('prestado', 'Prestado'),
        ('proceso_prestamo', 'En proceso de préstamo'),
    )

    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=13)
    resumen = models.TextField(upload_to='')
    disponibilidad = models.CharField(max_length=20, valor=DISPONIBILIDAD_VALORES)
    portada = models.ImageField()  # Campo para cargar la portada del libro

    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    ESTADO_VALORES = (
        ('prestado', 'Prestado'),
        ('devuelto', 'Devuelto'),
    )

    libro_prestado = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
    usuario_prestador = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado_prestamo = models.CharField(max_length=20, valor=ESTADO_VALORES)

    def __str__(self):
        return f'{self.libro_prestado.titulo} - {self.usuario_prestador.username}'
