# Archivo urls.py de biblioteca

from django.urls import path
from .views import listadoLibros, anadirLibros, detallesLibros, editarLibros, borrarLibros, prestarLibros

urlpatterns = [
    path('', listadoLibros.as_view(), name='listadoLibros'),
    path('anadir', anadirLibros.as_view(), name='anadirLibros'),
    path('detalles/<int:pk>', detallesLibros.as_view(), name='detallesLibros'),
    path('editar/<int:pk>', editarLibros.as_view(), name='editarLibros'),
    path('borrar/<int:pk>', borrarLibros.as_view(), name='borrarLibros'),
    path('prestar/<int:pk>', prestarLibros.as_view(), name='prestarLibros')
]