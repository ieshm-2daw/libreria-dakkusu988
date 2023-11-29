from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Libro
from django.urls import reverse, reverse_lazy

class listadoLibros(ListView):
    model = Libro
    template_name = 'biblioteca/listadoLibros.html'

class anadirLibros(CreateView):
    model = Libro
    fields = ['titulo', 'autores', 'editorial', 'fecha_publicacion', 'genero', 'ISBN', 'disponibilidad', 'portada']
    template_name = "biblioteca/anadirLibros.html"

    # Puedes redirigir a una vista específica usando reverse
    def get_success_url(self):
        return reverse('listadoLibros')

class detallesLibros(DetailView):
    model = Libro
    template_name = 'biblioteca/detallesLibros.html'

class editarLibros(UpdateView):
    model = Libro
    fields = ['titulo', 'autores', 'editorial', 'fecha_publicacion', 'genero', 'ISBN', 'disponibilidad', 'portada']
    template_name = "biblioteca/editarLibros.html"

    def get_success_url(self):
        return reverse('listadoLibros')

class borrarLibros(DeleteView):
    model = Libro
    template_name = 'biblioteca/borrarLibros.html'
    # Puedes redirigir a una vista específica usando reverse_lazy
    success_url = reverse_lazy("listadoLibros")

    # Mensaje de éxito al borrar
    def get_success_message(self):
        return "El libro ha sido eliminado exitosamente"