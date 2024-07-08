from typing import Any
from django.shortcuts import render, redirect

from django.db.models import Q

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
    
