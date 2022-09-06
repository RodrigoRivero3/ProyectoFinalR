
from django.shortcuts import render , redirect

from AppGame.forms import  JugadorFormulario , BusquedaApodoFormulario

from AppGame.models import Jugador, Consola, Juegos 


def busqueda_apodo_post(request):
    apodo = request.GET.get('apodo')

    jugadores = Jugador.objects.filter(apodo__icontains=apodo)
    contexto = {
        'jugadores': jugadores

    }
    return render(request, 'AppGame/jugador_filtrado.html' , contexto)




def busqueda_apodo(request):
    contexto = {

        'form': BusquedaApodoFormulario(),
    
    }

    return render(request ,'AppGame/busqueda_apodo.html', contexto)




def jugador_formulario(request):


    if request.method == 'POST':
        mi_formulario = JugadorFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data

            jugador1 = Jugador(nombre=data.get('nombre'), apellido=data.get('apellido'),
            edad=data.get('edad'),apodo=data.get('apodo'))
            jugador1.save()

            return redirect('AppGameJugadorFormulario') 
    
    jugadores = Jugador.objects.all()

    
    
    contexto = {
        'form': JugadorFormulario(),
        'jugadores': jugadores

    }
    return render(request, 'AppGame/jugador_formulario.html' , contexto)




def jugador(request):
    jugador1 = Jugador(nombre='Rodrigo',apellido = 'Rivero',
                            edad= 31, apodo= 'S')
    
    contexto = {
        'jugador':jugador1

    }
    return render(request, 'AppGame/jugador.html', contexto)


def consola(request):
    consola_1 = Consola(marca='playstation',modelo='ps5')
    consola_1.save()
    contexto = {
        'consola':consola_1

    }
    return render(request, 'AppGame/consola.html', contexto)


def juegos(request):
    juego_1 = Juegos(nombre='Resident_evil',categoria='accion',fecha_salida='2019-04-10')
    juego_1.save()
    contexto = {
        'juegos':juego_1

    }
    return render(request, 'AppGame/juegos.html', contexto)

def inicio(request):
    return render(request,'index.html')

