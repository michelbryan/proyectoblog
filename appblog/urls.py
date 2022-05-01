from django.urls import URLPattern, path, re_path
from appblog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('usuarios/', usuarios, name='Usuarios'),
    path('publicaciones/', publicaciones, name='Publicaciones'),
    path('about/', acercaDeMi, name="acercaDeMi"),
    path('buscarusuario/', buscarUsuario, name='BusquedaUsuario'),
    re_path("publicacion/list", PublicacionLista.as_view(), name="publicacion_list"),
    re_path("publicacion/nuevo/", PublicacionCrear.as_view(), name="publicacion_create"),
    re_path("publicacion/detalle/<pk>/", PublicacionDetalle.as_view(), name="publicacion_detail"),
    re_path("publicacion/editar/<pk>/", PublicacionActualizar.as_view(), name="publicacion_update"),
    re_path("publicacion/borrar/<pk>/", PublicacionBorrar.as_view(), name="publicacion_delete"),
]
