# Archivo urls.py de biblioteca

from django.urls import path
from .views import listadoLibros, añadirLibros, detallesLibros, editarLibros, borrarLibros

urlpatterns = [
    path('', listadoLibros.as_view(), name='listadoLibros'),
    path('añadir', añadirLibros.as_view(), name='añadirLibros'),
    path('detalles/<int:pk>', detallesLibros.as_view(), name='detallesLibros'),
    path('editar/<int:pk>', editarLibros.as_view(), name='editarLibros'),
    path('borrar/<int:pk>', borrarLibros.as_view(), name='borrarLibros'),
]