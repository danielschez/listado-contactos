from django.urls import path
from .views import ContactListView, ContactDetailView, ContactSearchListView, ContactUpdateView, ContactDeleteView

app_name = 'contacts'
urlpatterns = [
    path('search/', ContactSearchListView.as_view(), name='search'),
    path('<int:pk>/', ContactDetailView.as_view(), name='contact'),  # Aquí agregué int: para especificar que pk es un entero
    path('<int:pk>/update/', ContactUpdateView.as_view(), name='contact-update'),
    path('', ContactListView.as_view(), name='contact-list'),
    path('<int:pk>/delete/', ContactDeleteView.as_view(), name='contact-delete'),
]