from unittest.util import _MAX_LENGTH
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    id = forms.IntegerField()


class UsuarioRegistroForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasenia 1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Contrasenia 2', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = { k: "" for k in fields}


