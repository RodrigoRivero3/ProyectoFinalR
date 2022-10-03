from django.contrib import messages
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from UserApp.forms import *
from django.contrib.auth.decorators import login_required
from UserApp.models import Avatar

@login_required
def upload_avatar(request):
    if request.method == 'POST':

        formulario = AvatarForm(request.POST, request.FILES)

        if formulario.is_valid():

            data = formulario.cleaned_data
            avatar = Avatar.objects.filter(user=data.get('usuario'))

            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = formulario.changed_data['imagen']
                avatar.save()
            else:
                avatar= Avatar(user=request.user, imagen=data.get('imagen') )
                avatar.save()
            messages.error(request, 'Avatar creado')
        else:
            messages.error(request, formulario.errors) 
        return redirect('AppGameInicio')


    
    contexto = {

        'form': AvatarForm(),
        'nombre_form': 'Crear'
}
    return render(request,'Usuarios/login.html', contexto)

@login_required
def editar_usuario(request):
    usuario = request.user
    
    if request.method == 'POST':

        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            usuario.username = data.get('username')
            usuario.email = data.get('email')

            usuario.save()


            messages.info(request, 'Tu usuario fue registrado')

        else:
            messages.info(request, 'Tu usuario no se registro')

        return redirect('AppGameInicio')
    
    
    contexto = {

        #'form': UserCreationForm(),
        'form': UserRegisterForm
        (initial={
            'username': usuario.username,
            'email': usuario.email
        }),
        'nombre_form': 'registro'
        


    }
    return render(request, 'Usuarios/login.html', contexto)


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data


            usuario = data.get('username')
            contrasenia = data.get('password')

            user = authenticate(username=usuario,password=contrasenia)

            if user:
                login(request, user)
                messages.info(request,'Inicio de sesion Correcto!!')

            else:
                messages.info(request, 'Fallo el inicio de sesion!!')
    
        else:
            messages.info(request, 'Inicio de sesion FALLO!!')

        return redirect('AppGameInicio')


    contexto = {

        'form': AuthenticationForm(),
        
        'nombre_form': 'Login'

    }
    return render(request,'Usuarios/login.html', contexto)


def register(request):
    if request.method == 'POST':

        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            form.save()


            messages.info(request, 'Tu usuario fue registrado')

        else:
            messages.info(request, 'Tu usuario no se registro')

        return redirect('AppGameInicio')

    contexto = {

        #'form': UserCreationForm(),
        'form': UserRegisterForm(),
        'nombre_form': 'Registro'
        


    }
    return render(request, 'Usuarios/login.html', contexto)