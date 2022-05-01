from django.db import models


# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    id = models.IntegerField(primary_key=True)
    correo = models.EmailField(max_length=20)


class Publicaciones(models.Model):
    nombre_usuario = models.CharField(max_length=20)
    id_usuario = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=20)
    sub_titulo = models.CharField(max_length=50)
    posteo = models.CharField(max_length=150)
    
