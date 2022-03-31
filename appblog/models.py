from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    id = models.IntegerField(primary_key=True)

class Publicaciones(models.Model):
    nombre_usuario = models.CharField(max_length=20)
    id_usuario = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=20)
    posteo = models.CharField(max_length=150)

class Comentarios(models.Model):
    nombre_usuario = models.CharField(max_length=20)
    id_usuario = models.IntegerField(primary_key=True)
    posteo = models.CharField(max_length=150)
