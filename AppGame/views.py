

from django.shortcuts import render , redirect

from AppGame.forms import  *

from AppGame.models import Jugador, Consola, Juegos 


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
    
    jugadores = Jugador.objects.all()

    
    
    contexto = {
        'form': JugadorFormulario(),
        'jugadores': jugadores

    }
    return render(request, 'AppGame/jugador_formulario.html' , contexto)




def jugador(request):
    jugador1 = Jugador(nombre='Rodrigo',apellido = 'Rivero',
                            edad= 31, apodo= 'FenRoh')
    
    
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

