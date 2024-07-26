from typing import Any
from django.shortcuts import render, redirect

from django.db.models import Q

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Contacto


class ContactListView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    queryset = Contacto.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listados de contactos'
        context['contactos'] = context['contacto_list']
        return context
    
class ContactDetailView(DetailView):
    model = Contacto
    template_name = 'contacts/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener la instancia del contacto actual
        contacto = self.get_object()

        # Obtener la lista de emails adicionales
        email_adicionales = contacto.get_email_adicionales_list()
        telefono_adicionales = contacto.get_telefono_adicionales_list()
        direccion_adicionales = contacto.get_direccion_adicional_list()
        
        # Asumimos que emailAdicionales es una cadena separada por comas
        # if contacto.emailAdicionales:
        #     email_adicionales = contacto.emailAdicionales.split(',')
        # else:
        #     email_adicionales = []

        # Añadir al contexto
        context['email_adicionales_count'] = len(email_adicionales)
        context['emailExtra'] = email_adicionales
        context['telefono_adicionales_count'] = len(telefono_adicionales)
        context['telefonoExtra'] = telefono_adicionales
        context['direccion_adicionales_count'] = len(direccion_adicionales)
        context['direccionExtra'] = direccion_adicionales
        context['title'] = 'Actualizar Informción'
        
        return context
    
class ContactSearchListView(ListView):
    template_name = 'contacts/search.html'

    def get_queryset(self):
        #SELECT * FROM CONTACTOS WHERE nombre like %valor%
        filters = Q(nombre__icontains=self.query()) | Q(apellidoPaterno__icontains=self.query()) | Q(apellidoMaterno__icontains=self.query())
        return Contacto.objects.filter(filters)
    
    def query(self):
        return self.request.GET.get('q')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] =context['contacto_list'].count()
        return context
    
###########################################################################################
class ContactUpdateView(UpdateView):
    model = Contacto
    template_name = 'contacts/contact.html'
    fields = ['nombre', 'apellidoPaterno', 'apellidoMaterno', 'fechaNacimiento', 'alias', 'email', 'telefono', 'direccion', 'foto']
    success_url = reverse_lazy('contacts:contact-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obtener la instancia del contacto actual
        contacto = self.get_object()

        # Obtener la lista de emails, teléfonos y direcciones adicionales
        email_adicionales = contacto.get_email_adicionales_list()
        telefono_adicionales = contacto.get_telefono_adicionales_list()
        direccion_adicionales = contacto.get_direccion_adicional_list()
        

        # Añadir al contexto
        context['email_adicionales_count'] = len(email_adicionales)
        context['emailExtra'] = email_adicionales
        context['telefono_adicionales_count'] = len(telefono_adicionales)
        context['telefonoExtra'] = telefono_adicionales
        context['direccion_adicionales_count'] = len(direccion_adicionales)
        context['direccionExtra'] = direccion_adicionales
        context['title'] = 'Actualizar Información'
        
        return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            # Guardar datos del formulario principal
            self.object = form.save()

            # Acceder a las variables del contexto
            # context = self.get_context_data(**kwargs)
            # email_adicionales = context.get('email_adicionales_count', [])
            # telefono_adicionales = context.get('telefono_adicionales_count', [])
            # direccion_adicional = context.get('direccion_adicionales_count', [])

            # Guardar emails adicionales
          
           

            # totalEma = request.POST.getlist('total_email')
            # email_adicionales = []
            # numero_entero = int(''.join(map(str, totalEma)))
            # contador = 0
            # while contador < numero_entero:
            #     contador += 1
            #     email_adicionales = request.POST.getlist(f'extra_email_{contador}')
            #     if email_adicionales:
            #         email_adicionales.append(email_adicionales)
            #         self.object.emailAdicionales = email_adicionales


            totalEma = request.POST.getlist('total_email')
            email_adicionales = []

            # Convertir la lista de totales a un solo número entero
            numero_entero = int(''.join(map(str, totalEma)))

            contador = 0
            while contador < numero_entero:
                contador += 1
                extra_email = request.POST.getlist(f'extra_email_{contador}')
                if extra_email:
                    # Agregar los emails adicionales a la lista email_adicionales
                    email_adicionales.extend(extra_email)  # Usamos extend para añadir los elementos a la lista

            # Guardar los emails adicionales en el objeto
            self.object.emailAdicionales = ','.join(email_adicionales)

############################################################################################

            totalTel = request.POST.getlist('total_tel')
            tel_adicionales = []

            # Convertir la lista de totales a un solo número entero
            numero_enteroTel = int(''.join(map(str, totalTel)))

            contadorTel = 0
            while contadorTel < numero_enteroTel:
                contadorTel += 1
                extra_tel = request.POST.getlist(f'telefono_{contadorTel}')
                if extra_tel:
                    # Agregar los emails adicionales a la lista email_adicionales
                    tel_adicionales.extend(extra_tel)  # Usamos extend para añadir los elementos a la lista

            # Guardar los emails adicionales en el objeto
            self.object.telefonoAdicional = ','.join(tel_adicionales)


###################################################################################################
            totalDir = request.POST.getlist('total_dir')
            dir_adicionales = []

            # Convertir la lista de totales a un solo número entero
            numero_enteroDir = int(''.join(map(str, totalDir)))

            contadorDir = 0
            while contadorDir < numero_enteroDir:
                contadorDir += 1
                extra_dir = request.POST.getlist(f'direccion_{contadorDir}')
                if extra_dir:
                    # Agregar los emails adicionales a la lista email_adicionales
                    dir_adicionales.extend(extra_dir)  # Usamos extend para añadir los elementos a la lista

            # Guardar los emails adicionales en el objeto
            self.object.direccionAdicional = ','.join(dir_adicionales)



            # Guardar teléfonos adicionales
            # telefono_adicionales = request.POST.getlist('telefono_1')
            # self.object.telefonoAdicional = telefono_adicionales

            # # Guardar direcciones adicionales
            # direccion_adicional = request.POST.getlist('direccion_1')
            # self.object.direccionAdicional = direccion_adicional

            self.object.save()

            return redirect(self.get_success_url())

        return self.form_invalid(form)

    
#################################################################################################
class ContactDeleteView(DeleteView):
    model = Contacto
    template_name = 'contact_confirm_delete.html'  # Cambié la plantilla a una más adecuada
    success_url = reverse_lazy('contacts:contact-list')  # Asegúrate de que el nombre de la URL coincida

    def get_queryset(self):
        # Personalizar el queryset si es necesario
        queryset = super().get_queryset()
        return queryset