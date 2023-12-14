from django import forms
from .models import Libro, Prestamo

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autores', 'editorial', 'fecha_publicacion', 'genero', 'ISBN', 'resumen', 'disponibilidad', 'portada']

class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['fecha_prestamo']  # Agrega los campos que necesites en tu formulario

    def __init__(self, *args, **kwargs):
        super(PrestamoForm, self).__init__(*args, **kwargs)