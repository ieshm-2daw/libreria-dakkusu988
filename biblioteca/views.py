from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View
from .models import Libro, Prestamo
from django.urls import reverse, reverse_lazy
from typing import Any
from datetime import date

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

        context["prestamos_prestados"] = Prestamo.objects.all() #filter(usuario_prestador=self.request.user, estado_prestamo="prestado")
        context["prestamos_devueltos"] = Prestamo.objects.all() #.filter(usuario_prestador=self.request.user, estado_prestamo="devuelto")

        return context

#4. BOTON PRESTAR LIBRO
class prestarLibros(View):
    template_name = "biblioteca/prestarLibros.html"

    def get(self, request, pk):
        # Manejar solicitudes GET para mostrar un mensaje de error
        return render(request, self.template_name, {"error_message": "No se puede acceder a esta página."})

    def post(self, request, pk):
        libro = get_object_or_404(Libro, pk=pk)

        # Verificar si el libro ya está prestado
        if Prestamo.objects.filter(libro_prestado=libro, estado_prestamo='prestado').exists():
            return redirect('misLibros')
        
        # Crear un nuevo registro de préstamo con la fecha actual por defecto
        Prestamo.objects.create(
            libro_prestado=libro,
            usuario_prestador=request.user,
            fecha_prestamo=date.today(),
            estado_prestamo='prestado'
        )

        libro.disponibilidad = 'prestado'
        libro.save()

        return redirect('misLibros')

#5. BOTON DEVOLVER LIBRO PRESTADO
class devolverLibros(View):
    def get(self, request, pk):
        prestamo = get_object_or_404(Prestamo, pk=pk)
        return render(request, 'biblioteca/devolverLibros.html', {'prestamo': prestamo})

    def post(self, request, pk):
        prestamo = get_object_or_404(Prestamo, pk=pk)
        
        if prestamo.libro_prestado.disponibilidad == 'prestado':
            prestamo.estado_prestamo = 'devuelto'
            prestamo.fecha_devolucion = date.today()
            prestamo.save()

            libro_prestado = prestamo.libro_prestado
            libro_prestado.disponibilidad = 'disponible'
            libro_prestado.save()

            return redirect('misLibros')

        return redirect('misLibros')
    
#6. LISTA ALFABETICA POR TITULO
class listadoAlfabeticos(ListView):
    model = Libro
    template_name = 'biblioteca/listadoAlfabeticos.html'

    def get_queryset(self):
        return Libro.objects.order_by('titulo')