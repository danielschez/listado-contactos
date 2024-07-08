from django.urls import path

from . import views

app_name = 'contacts'
urlpatterns = [
    path('search', views.ContactSearchListView.as_view(), name='search'),
    path('<pk>', views.ContactDetailView.as_view(), name='contact'), #id -> llave primaria
]