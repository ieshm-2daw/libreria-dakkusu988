from django.contrib import admin
from .models import Usuario, Libro, Editorial, Autor, Prestamo

admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Editorial)
admin.site.register(Autor)
admin.site.register(Prestamo)