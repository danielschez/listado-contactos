from typing import Any
from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Contacto

class ContactListView(ListView):
    template_name = 'index.html'
    queryset = Contacto.objects.all().order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Listados de contactos'
        context['contactos'] = context['contacto_list']
        return context
    
class ContactDetailView(DetailView): #id ->pk
    model = Contacto
    template_name = 'contacts/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print (context)
        return context