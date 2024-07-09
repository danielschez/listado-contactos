from django.db import models

from datetime import datetime

# now = datetime.now()
# BIRTH_YEAR_CHOICES = [i for i in range(1950, now.year+1)]

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    apellidoPaterno = models.CharField(max_length=100)                            
    apellidoMaterno = models.CharField(max_length=100)
    fechaNacimiento = models.DateField(null=True)
    alias = models.CharField(max_length=100)
    email = models.EmailField(blank=False)
    emailAdicionales = models.CharField(max_length=200)
    telefono = models.CharField(max_length=10)
    telefonoAdicional = models.CharField(max_length=200)
    direccion = models.CharField(max_length=100)
    direccionAdicional = models.CharField(max_length=200)
    foto = models.ImageField(upload_to='contacts/', null=False, blank=False)
    create_at = models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return self.nombre

    def get_email_adicionales_list(self):
        # Dividir la cadena emailAdicionales en una lista de correos electrónicos
        if self.emailAdicionales:
            # Limpiar la cadena eliminando corchetes y comillas
            email_adicionales_cleaned = self.emailAdicionales.replace("[", "").replace("]", "").replace("'", "")
            emails = [email.strip() for email in email_adicionales_cleaned.split(',') if email.strip()]
            return emails
        return []
    
    def get_telefono_adicionales_list(self):
        # Dividir la cadena emailAdicionales en una lista de correos electrónicos
        if self.telefonoAdicional:
            # Limpiar la cadena eliminando corchetes y comillas
            telefono_adicionales_cleaned = self.telefonoAdicional.replace("[", "").replace("]", "").replace("'", "")
            telefono = [telefono.strip() for telefono in telefono_adicionales_cleaned.split(',') if telefono.strip()]
            return telefono
        return []
    
    def get_direccion_adicional_list(self):
        # Dividir la cadena direccionAdicional en una lista de direcciones
        if self.direccionAdicional:
            # Limpiar la cadena eliminando corchetes y comillas
            direccion_adicionales_cleaned = self.direccionAdicional.replace("[", "").replace("]", "").replace("'", "")
            direcciones = [direccion.strip() for direccion in direccion_adicionales_cleaned.split(',') if direccion.strip()]
            return direcciones
        return []


