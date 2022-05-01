from django.http import HttpResponse
from django.shortcuts import render, redirect

from appblog.models import Publicaciones, Usuario
from appblog.forms import UsuarioFormulario

from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "appblog/usuarios.html", {"usuario": usuarios, "title": "Usuario", "pege": "Usuario"})

def publicaciones(request):
    publicaciones = Publicaciones.objects.all()
    return render(request, "appblog/publicaciones.html")


def inicio(request):
    dict_ctx = {"bienvenida": "Bienvenid@ a nuestro blog!"}
    return render(request, "appblog/index.html", dict_ctx)

def buscarUsuario(request):
    data = request.GET.get('usuario', "")
    error = ""
    

    if data:
        try:
            usuario = Usuario.objects.get(id = data)
            return render(request, 'appblog/busquedaUsuario.html', {"usuario": usuario, "id": data})
        except Exception as axc:
            print(exec)
            error = "No existe ese usuario"    
    return render(request, 'appblog/busquedaUsuario.html', {"error": error})

def acercaDeMi(request):
    return render(request, "appblog/acercademi.html")

class PublicacionLista(ListView):

    model = Publicaciones
    template_name = "appblog/publicaciones_list.html"

class PublicacionDetalle(DetailView):

    model = Publicaciones
    template_name = "appblog/publicaciones_detalle.html"

class PublicacionCrear(CreateView):

    model = Publicaciones
    success_url = "/appblog/publicacion/list"
    fields = ['titulo', 'posteo']

class PublicacionActualizar(UpdateView):

    model = Publicaciones
    success_url = "/appblog/publicacion/list"
    fields = ['titulo', 'posteo']


class PublicacionBorrar(DeleteView):

    model = Publicaciones
    success_url = "/appcoder/publicacion/list"

