from django.urls import path

from . import views

urlpatterns = [
    path('<pk>', views.ContactDetailView.as_view(), name='contact'), #id -> llave primaria
]