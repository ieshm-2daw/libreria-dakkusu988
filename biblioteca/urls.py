# Archivo urls.py de biblioteca

from django.urls import path
from .views import listadoLibros, anadirLibros, detallesLibros, editarLibros, borrarLibros, listadoDisponibles, misLibros, prestarLibros, devolverLibros, listadoAlfabeticos, BuscarLibros

urlpatterns = [
    path('', listadoLibros.as_view(), name='listadoLibros'),
    path('anadir', anadirLibros.as_view(), name='anadirLibros'),
    path('detalles/<int:pk>', detallesLibros.as_view(), name='detallesLibros'),
    path('editar/<int:pk>', editarLibros.as_view(), name='editarLibros'),
    path('borrar/<int:pk>', borrarLibros.as_view(), name='borrarLibros'),
    path('disponibles', listadoDisponibles.as_view(), name='listadoDisponibles'),
    path('prestados', misLibros.as_view(), name='misLibros'),
    path('prestar/<int:pk>', prestarLibros.as_view(), name='prestarLibros'),
    path('devolver/<int:pk>', devolverLibros.as_view(), name='devolverLibros'),
    path('alfabeticamente', listadoAlfabeticos.as_view(), name='listadoAlfabeticos'),
    path('buscar/', BuscarLibros.as_view(), name='buscarLibros'),

]