from atexit import register
from django import views
from django.urls import URLPattern, path
from applogin.views import *
from django.contrib.auth.views import LogoutView





urlpatterns = [
path('actualizar_usuario/', actualizar_usuario, name = 'EditarUsuario'),
path('login/', login_request, name = 'login'),
path('register/', register_request, name='Register'),
path('logout/', LogoutView.as_view(template_name="applogin/logout.html"), name="Logout")
]