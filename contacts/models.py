from django.db import models

from datetime import datetime

now = datetime.now()
BIRTH_YEAR_CHOICES = [i for i in range(1950, now.year+1)]

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    apellidoPaterno = models.CharField(max_length=100)                            
    apellidoMaterno = models.CharField(max_length=100)
    fechaNacimiento = models.DateField(null=True)
    alias = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    emailAdicionales = models.CharField(max_length=200)
    telefono = models.CharField(max_length=100)
    telefonoAdicional = models.CharField(max_length=200)
    direccion = models.CharField(max_length=100)
    direccionAdicional = models.CharField(max_length=200)
    foto = models.ImageField(null=True, upload_to='{% static/images/%}')
    create_at = models.DateTimeField(auto_now_add=True)
    