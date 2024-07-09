from django import forms

from django.contrib.auth.models import User

#FORM CONTACTS
from datetime import datetime

now = datetime.now()
BIRTH_YEAR_CHOICES = [i for i in range(1950, now.year+1)]

class RegisterForm(forms.Form):
    username = forms.CharField(required=True, max_length=50,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'id': 'username'
                                }))
    email = forms.EmailField(required=True,
                                widget=forms.EmailInput(attrs={
                                   'class': 'form-control',
                                   'id': 'email',
                                   'placeholder': 'email@example.com'
                                }))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-control'
                                }))

    password2 = forms.CharField(label='Confirmar Password',
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                     'class': 'form-control'
                                }))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuentra en uso')

        return email

#Clean method is used to validate if one field depents on another

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'El password no coincide')

    def save(self):
        return User.objects.create_user(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password')
        )


############################################################################################


class RegistrationForm(forms.Form):
    nombre = forms.CharField(label='Nombre', required=True, max_length=100, min_length=4,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'nombre'}))
    apellidoPaterno = forms.CharField(label='Apellido Paterno', required=True, max_length=100, min_length=4,
                                     widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'apellidoPaterno'}))
    apellidoMaterno = forms.CharField(label='Apellido Materno', max_length=100,
                                       widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'apellidoMaterno'}))

    fechaNacimiento = forms.DateField(label='Fecha de Nacimiento',
        widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES, attrs={'class': 'form-control', 'id': 'fechaNacimiento'}))

    alias = forms.CharField(label='Alias', max_length=50, required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'alias'}))
    email = forms.EmailField(label='Correo', required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email'}))
    telefono = forms.CharField(label='Telefono', max_length=10, required=True,  # Make required
                               widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'telefono'}))
    direccion = forms.CharField(label='Dirección', max_length=200, required=True,  # Make required
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'direccion'}))
    foto = forms.ImageField(label='Foto', required=False,  # Make optional
                             widget=forms.FileInput(attrs={'class': 'form-control', 'id': 'foto'}))
