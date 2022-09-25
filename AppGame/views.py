
from django.views.generic import ListView
import django
from django.contrib import messages

from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from AppGame.forms import  *
from django.contrib.auth.mixins import LoginRequiredMixin 
from AppGame.models import Jugador, Consola, Juegos


def editar_jugador(request,apodo):
    jugador_editar = Jugador.objects.get(apodo=apodo)

    if request.method == 'POST':
        mi_formulario = JugadorFormulario(request.POST)

        if mi_formulario.is_valid():

            data = mi_formulario.cleaned_data
            
            jugador_editar.nombre = data.get('nombre').title()
            jugador_editar.apodo = data.get('apodo')
            jugador_editar.apellido = data.get('apellido')
            jugador_editar.edad = data.get('edad')
            try:
                jugador_editar.save()
            except django.db.utils.IntegrityError:
                messages.error(request, "apodo ya existe")
            
            
            return redirect('AppGameJugadorFormulario') 

    
    
    contexto = {

        'form': JugadorFormulario(initial={
            'nombre':jugador_editar.nombre,
            'apodo': jugador_editar.apodo,
            'apellido': jugador_editar.apellido,
            'edad': jugador_editar.edad
            })
    }
    return render(request, 'AppGame/jugador_formulario.html' , contexto)

def eliminar_apodo(request,apodo ):
    apodo_eliminar = Jugador.objects.get(apodo=apodo)
    apodo_eliminar.delete()

    messages.info(request,f'El apodo {apodo_eliminar} fue eliminado')

    return redirect('AppGameJugador')




def busqueda_categoria_post(request):
    categoria = request.GET.get('categoria')

    juegos = Juegos.objects.filter(categoria__icontains=categoria)
    contexto = {
        'juegos': juegos

    }
    return render(request, 'AppGame/juegos_filtrados.html' , contexto)

def busqueda_categoria(request):
    contexto = {

        'form': BusquedaCategoriaFormulario(),
    
    }

    return render(request ,'AppGame/busqueda_categoria.html', contexto)

def juegos_formulario(request):


    if request.method == 'POST':
        mi_juego = JuegosFormulario(request.POST)

        if mi_juego.is_valid():

            data = mi_juego.cleaned_data

            juego1 = Juegos(nombre=data.get('nombre'), categoria=data.get('categoria'),fecha_salida=data.get('fecha_salida') )
            juego1.save()

            return redirect('AppGameJuegosFormulario') 
    
    juegos = Juegos.objects.all()

    
    
    contexto = {
        'form': JuegosFormulario(),
        'juegos': juegos

    }
    return render(request, 'AppGame/juegos_formulario.html' , contexto)



def busqueda_modelo_post(request):
    modelo = request.GET.get('modelo')

    consolas = Consola.objects.filter(modelo__icontains=modelo)
    contexto = {
        'consolas': consolas

    }
    return render(request, 'AppGame/consolas_filtrada.html' , contexto)

def busqueda_modelo(request):
    contexto = {

        'form': BusquedaModeloFormulario(),
    
    }

    return render(request ,'AppGame/busqueda_modelo.html', contexto)

def consola_formulario(request):


    if request.method == 'POST':
        mi_consola = ConsolaFormulario(request.POST)

        if mi_consola.is_valid():

            data = mi_consola.cleaned_data

            consola1 = Consola(marca=data.get('marca'), modelo=data.get('modelo'))
            consola1.save()

            return redirect('AppGameConsolaFormulario') 
    
    consolas = Consola.objects.all()

    
    
    contexto = {
        'form': ConsolaFormulario(),
        'consolas': consolas

    }
    return render(request, 'AppGame/consola_formulario.html' , contexto)




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
    contexto = {
        'form': JugadorFormulario(),
        

    }
    return render(request, 'AppGame/jugador_formulario.html' , contexto)

class JugadorList(LoginRequiredMixin,ListView):
    model = Jugador
    template_name = 'AppGame/jugador.html'
    



#def jugador(request):
 #   jugadores = Jugador.objects.all()

  #  contexto = { 'jugadores':jugadores }
    
  #  return render(request, 'AppGame/jugador.html', contexto)

@login_required
def consola(request):
    consolas = Consola.objects.all()
    
    contexto = {
        'consolas': consolas

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

