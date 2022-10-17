from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length = 30)
    apellido = models.CharField(max_length = 30)
    telefono = models.CharField(max_length = 30)
    email = models.CharField(max_length = 50) #models.EmailField( null = False)
    
    def __str__(self):
        return f'{self.nombre}, {self.apellido}'