from django.shortcuts import render
from django.shortcuts import redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

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

################################################################################################
def register_contacts(request):
    if request.method == 'POST':

        # Obtener el número total de emails adicionales enviados por el usuario
        total_email = request.POST.get('total_email')  # Suponiendo que esto sea un número o una lista
        email_adicionales = []

        # Si total_email es un número
        if total_email.isdigit():
            total_email = int(total_email)
            for i in range(total_email):
                email_adicional = request.POST.get(f'extra_email_{i+1}')  # Usando i+1 si los nombres de los campos son extra_email_1, extra_email_2, etc.
                if email_adicional:
                    email_adicionales.append(email_adicional)
    ######################################################################################################
        total_telefono = request.POST.get('total_tel') 
        telefono_adicionales = []

        if total_telefono.isdigit():
            total_telefono = int(total_telefono)
            for i in range(total_telefono):
                telefono_adicional = request.POST.get(f'extra_tel_{i+1}')  # Usando i+1 si los nombres de los campos son extra_tel_1, extra_tel_2, etc.
                if telefono_adicional:
                    telefono_adicionales.append(telefono_adicional)
                    #print(telefono_adicionales)
    ######################################################################################################
        total_direccion = request.POST.get('total_dir')
        direccion_adicionales = []

        if total_direccion.isdigit():
            total_direccion = int(total_direccion)
            for i in range(total_direccion):
                direccion_adicional = request.POST.get(f'extra_dir_{i+1}')  # Usando i+1 si los nombres de los campos son extra_dir_1, extra_dir_2, etc.
                if direccion_adicional:
                    direccion_adicionales.append(direccion_adicional)
                    #print(direccion_adicionales)
     ######################################################################################################

       
    #if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        apellidoPaterno = request.POST.get('apellidoPaterno')
        apellidoMaterno = request.POST.get('apellidoMaterno')
        fechaNacimiento = request.POST.get('fechaNacimiento')
        alias = request.POST.get('alias')
        email = request.POST.get('email')
        #emailAdicionales = request.POST.get('emailAdicionales')
        telefono = request.POST.get('telefono')
        #telefonoAdicional = request.POST.get('telefonoAdicional')
        direccion = request.POST.get('direccion')
        #direccionAdicional = request.POST.get('direccionAdicional')
        foto = request.FILES.get('foto')

        # Validar los datos
        errors = []
        if not nombre:
            errors.append("El nombre es requerido.")
        if not apellidoPaterno:
            errors.append("El apellido paterno es requerido.")
        if not apellidoMaterno:
            errors.append("El apellido materno es requerido.")
        if not fechaNacimiento:
            errors.append("La fecha de nacimiento es requerida.")
        if not alias:
            errors.append("El alias es requerido.")
        if not email:
            errors.append("El email es requerido.")
        else:
            try:
                validate_email(email)
            except ValidationError:
                errors.append("El email no es válido.")
        #Validación adicional para emailAdicionales si es proporcionado
        # if email_adicionales:
        #     try:
        #         validate_email(email_adicionales)
        #     except ValidationError:
        #         errors.append("El email adicional no es válido.")

        if not telefono:
            errors.append("El teléfono es requerido.")
        if not direccion:
            errors.append("La dirección es requerida.")
        
        # Si no hay errores, guardar los datos
        if not errors:
            contact = Contacto(
                nombre=nombre,
                apellidoPaterno=apellidoPaterno,
                apellidoMaterno=apellidoMaterno,
                fechaNacimiento=fechaNacimiento,
                alias=alias,
                email=email,
                emailAdicionales=email_adicionales,
                telefono=telefono,
                telefonoAdicional=telefono_adicionales,
                direccion=direccion,
                direccionAdicional=direccion_adicionales,
                foto=foto
            )
            contact.save()
            return redirect('success')  # Redirigir a otra vista después de guardar

        return render(request, 'register.html', {
            'title': 'Registro de Contactos',
            'errors': errors,
            'data': request.POST
        })
    else:
        return render(request, 'register.html', {
            'title': 'Registro de Contactos',
        })
    

def register_success(request):
    return render(request, 'success.html', {
        'title': 'Registro Exitoso'
    })