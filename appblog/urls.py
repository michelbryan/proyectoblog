from django.urls import URLPattern, path
from appblog.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('usuarios/', usuarios, name="Usuarios"),
    path('publicaciones/', publicaciones, name="Publicaciones"),
    path('comentarios/', comentarios),
    path('usuarioformulario/', usuarioformulario, name='Usuario'),
    path('buscarusuario/', buscarUsuario, name='BusquedaUsuario'),
]