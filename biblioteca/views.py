from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Libro, Prestamo
from django.urls import reverse, reverse_lazy
from typing import Any

# 1. LIBROS (CRUD)
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
    
#2. DISPONIBLES

class listadoDisponibles(ListView):
    model = Libro
    template_name = 'biblioteca/listadoDisponibles.html'

    def get_queryset(self):
        queryset = Libro.objects.filter(disponibilidad='disponible')
        return queryset


#3. MIS LIBROS (PRESTADOS Y DEVUELTOS [HISTORIAL])

class misLibros(ListView):
    model = Prestamo
    template_name = 'biblioteca/misLibros.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context["prestamos_prestados"] = Prestamo.objects.filter(usuario_prestador=self.request.user, estado_prestamo="prestado")
        context["prestamos_devueltos"] = Prestamo.objects.filter(usuario_prestador=self.request.user, estado_prestamo="devuelto")

        return context

#4. BOTON DEVOLVER LIBRO PRESTADO

#def devolver_libro(request, pk):
#    libro_prestado = get_object_or_404(Libro, pk= pk, disponibilidad= "prestado")
#    prestamo = Prestamo.objects.filter(libro= libro_prestado, usuario= request.user, estado= "prestado").first()
#
#    if request.method == "POST":
#        prestamo.estado = "devuelto"
#        prestamo.