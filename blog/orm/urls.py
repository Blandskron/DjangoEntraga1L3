from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.crearAutor, name='home'),
    path('articulo/', views.crearArticulo, name='articulo'),
    path('ver_articulos/', views.ver_articulos, name='ver_articulos'),
]
