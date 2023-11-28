from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from .models import Libro

class listadoLibros(ListView):
    model = Libro
    template_name = 'biblioteca/listadoLibros.html'