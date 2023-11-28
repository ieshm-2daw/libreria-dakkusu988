# Archivo urls.py de biblioteca

from django.urls import path
from .views import listadoLibros

urlpatterns = [
    path('', listadoLibros.as_view(), name='listadoLibros'),
]