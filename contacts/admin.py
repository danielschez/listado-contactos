from django.contrib import admin

from .models import Contacto

class ContactAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidoPaterno', 'apellidoMaterno', 'telefono', 'email')
    search_fields = ('nombre', 'apellidoPaterno', 'apellidoMaterno', 'telefono', 'email')

admin.site.register(Contacto, ContactAdmin)
