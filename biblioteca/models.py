from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    DNI = models.CharField(max_length=9, unique=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.DNI

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    sitio_web = models.URLField()  # Campo URL para el sitio web

    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    biografia = models.TextField(max_length=100)
    #foto = models.ImageField(upload_to='autores/', null=True, blank=True)  # Campo para cargar la foto de perfil

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField()
    genero = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=13)
    #resumen = models.ImageField(upload_to='portadas/', null=True, blank=True)

    DISPONIBILIDAD_VALORES = (
        ('disponible', 'Disponible'),
        ('prestado', 'Prestado'),
        ('proceso_prestamo', 'En proceso de préstamo'),)

    disponibilidad = models.CharField(max_length=50, choices=DISPONIBILIDAD_VALORES)
    portada = models.ImageField()  # Campo para cargar la portada del libro

    def __str__(self):
        return self.titulo

class Prestamo(models.Model):
    libro_prestado = models.ForeignKey(Libro, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(null=True, blank=True)
    usuario_prestador = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    ESTADO_VALORES = (
    ('prestado', 'Prestado'),
    ('devuelto', 'Devuelto'),)

    estado_prestamo = models.CharField(max_length=50, choices=ESTADO_VALORES, default="prestado")

    def __str__(self):
        return f'{self.libro_prestado.titulo} - {self.usuario_prestador.username}'
