from django.shortcuts import render, redirect
from appblog.models import Usuario
from applogin.forms import UsuarioEdit
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from applogin.forms import UsuarioRegistroForm, UsuarioEdit, UsuarioFormulario
# Create your views here.

def actualizar_usuario(request):
    
    usuario = request.user

    if request.method == "POST":
        formulario = UsuarioEdit(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.last_name = data["last_name"]
            usuario.first_name = data["first_name"]

            usuario.save()

            return redirect("Inicio")
        else:
            formulario = UsuarioEdit(initial={"email": usuario.email})  
            return render(request,  "applogin/editar_usuario.html", {"form": formulario, "errors": ["Datos invalidos"]})

    else:
        formulario = UsuarioEdit(initial={"email": usuario.email})  
        return render(request,  "applogin/editar_usuario.html", {"form": formulario})

def login_request(request):

    if request.method == "POST":

        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            nombre_usuario = data.get("username")
            contrasenia = data.get("password")

            usuario = authenticate(username=nombre_usuario, password=contrasenia)

            if usuario is not None:
                login(request, usuario)
                
                dict_ctx = {"bienvenida": "Bienvenid@ a nuestro blog!", "user": usuario}
                return render(request, "appblog/index.html", dict_ctx)
            else:
                dict_ctx = {"bienvenida": "Bienvenid@ a nuestro blog!", "user": usuario, "errors": ["El usuario no existe"] }
                return render(request, "appblog/index.html", dict_ctx)
        else:
            dict_ctx = {"bienvenida": "Bienvenid@ a nuestro blog!", "user": "anonymous", "errors": ["Revise los datos indicados en el form"] }
            return render(request, "appblog/index.html", dict_ctx)
    else:
        form = AuthenticationForm()
        return render(request, "applogin/login.html", {"form": form})

def register_request(request):

    if request.method == "POST":

        form = UsuarioRegistroForm(request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            print(usuario)
            form.save()
            return redirect("inicio")
        else:
            dict_ctx = {"bienvenida": "Bienvenid@ a nuestro blog!", "user": "anonymous", "errors": ["No paso las validaciones"] }
            return redirect(request, "appblog/index.html", dict_ctx)
    else:
        form = UsuarioRegistroForm()
        return render(request, "applogin/register.html", {"form": form})

def usuarioformulario(request):
    
    if request.method == "post":
        usuario = UsuarioFormulario(request.post)
        print(usuario)
        
        if usuario.is_valid:
            data = usuario.cleaned_data

            usuario_nuevo = Usuario(data['nombre'], data['id'])
            usuario_nuevo.save()
        
        return render(request, 'appblog/index.html')
    else:
        usuario_form = UsuarioFormulario()

    
    return render(request, 'appblog/usuarioformulario.html', {"formulario": usuario_form })


