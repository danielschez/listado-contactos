from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate 

from django.contrib.auth.models import User

from contacts.models import Contacto

from .forms import RegisterForm

def index(request):
    contactos = Contacto.objects.all()
    return render(request, 'index.html', {
        'message': 'Listados de contactos',
        'title': 'Catalogo de Contactos',
        'contactos': contactos,
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')
        else:
            messages.error(request, 'Usuario o Contraseña incorrecto')

    return render(request, 'users/login.html', {
        'title': 'Login' #context
    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión cerrada exitosamente')
    return redirect('login')

def register(request):
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
       
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('index')

    return render(request, 'users/register.html', {
        'form': form
    })