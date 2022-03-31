from django.http import HttpResponse
from django.shortcuts import render

from appblog.models import Comentarios, Publicaciones, Usuario
from appblog.forms import UsuarioFormulario

# Create your views here.

def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "appblog/usuarios.html")

def publicaciones(request):
    publicaciones = Publicaciones.objects.all()
    return render(request, "appblog/publicaciones.html")

def comentarios(request):
    comentarios = Comentarios.objects.all()
    return render(request, "appblog/comentarios.html")

def inicio(request):
    dict_ctx = {"bienvenida": "Bienvenid@ a nuestro blog!"}
    return render(request, "appblog/index.html", dict_ctx)

def usuarioformulario(request):
    
    if request.method == "post":
        usuario = UsuarioFormulario(request.post)
        
        if usuario.is_valid:
            data = usuario.cleaned_data

            usuario_nuevo = Usuario(data['nombre'], data['id'])
            usuario_nuevo.save
        
        return render(request, 'appblog/index.html')
    else:
        usuario_form = UsuarioFormulario()

    
    return render(request, 'appblog/usuarioformulario.html', {"formulario": usuario_form })

def buscarUsuario(request):
    data = request.GET.get('usuario', "")
    error = ""
    

    if data:
        try:
            usuario = Usuario.objects.filter(id= data)
            return render(request, 'appblog/busquedaUsuario.html', {"usuario": usuario, "id": data})
        except Exception as axc:
            print(exec)
            error = "No existe ese usuario"    
    return render(request, 'appblog/busquedaUsuario.html')


