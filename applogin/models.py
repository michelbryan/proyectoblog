from django.db import models

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=20)
    id = models.IntegerField(primary_key=True)
    correo = models.EmailField(max_length=20)