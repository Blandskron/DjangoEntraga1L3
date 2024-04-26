from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import AutorForm, ArticuloForm
from .models import Articulo

def crearAutor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/home/")
    else:
        form = AutorForm()
    return render(request, "home.html", {"form": form})

def crearArticulo(request):
    if request.method == "POST":
        form = ArticuloForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/articulo/")
    else:
        form = ArticuloForm()
    return render(request, "orm/articulo.html", {"form": form})


def ver_articulos(request):
    articulos = Articulo.objects.all()
    return render(request, 'orm/ver_articulos.html', {'articulos': articulos})
