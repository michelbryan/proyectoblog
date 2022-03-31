from unittest.util import _MAX_LENGTH
from django import forms

class UsuarioFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    id = forms.IntegerField()