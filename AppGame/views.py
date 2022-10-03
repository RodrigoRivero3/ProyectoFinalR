
from doctest import ELLIPSIS_MARKER
from django.views.generic import ListView
import django
from django.contrib import messages
from django.urls.base import reverse_lazy
from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from AppGame.forms import  *
from django.contrib.auth.mixins import LoginRequiredMixin 
from AppGame.models import Jugador, Juegos, Consola
from django.core.paginator import Paginator
from django.views.generic import UpdateView

def acerca_mio(request):
    return render(request,'AppGame/acerca_mio.html')


@login_required
def ver_consola(request,modelo ):
    consola = Consola.objects.get(modelo=modelo)
    
    contexto = {'modelo':consola}
   

    messages.info(request,f'Viendo {consola.titulo} ',contexto)

    return render(request,'AppGame/detalle_consola.html')


@login_required
def ver_juego(request,categoria ):
    juego_ver = Juegos.objects.get(categoria=categoria)
    
    contexto = {'categoria':juego_ver}
   

    messages.info(request,f'Viendo {juego_ver.titulo_posteo} ',contexto)

    return render(request,'AppGame/detalle_juegos.html')


@login_required
def editar_juego(request, categoria):
    jugador_e = Juegos.objects.get(categoria=categoria)
    


    if request.method == 'POST':
        mi_formular = JuegosFormulario(request.POST,request.FILES)

        if mi_formular.is_valid():
            data = mi_formular.cleaned_data
           
            
            jugador_e.juego= data.get('juego')
            jugador_e.apellido = data.get('apellido')
            jugador_e.apodo= data.get('apodo')
            jugador_e.titulo_posteo= data.get('titulo_posteo')
            jugador_e.subtitulo_posteo=data.get('subtitulo_posteo')
            jugador_e.contenido_juego=data.get('contenido_juego')
            jugador_e.imagen_juego=data.get('imagen_juego')
           
            jugador_e.save()
           
            titulo_posteo = data.get('titulo_posteo')
            

            messages.success(request,f'Se creo {titulo_posteo} correctamente')

            return redirect('AppGameJuegos')
        else:
            messages.error(request, mi_formular.errors)    
    contexto={
        'form' : JuegosFormulario(
            initial={ 
                'juego':jugador_e.juego,
                'categoria': jugador_e.categoria,
                
                'titulo_posteo':jugador_e.titulo_posteo,
                'subtitulo_posteo':jugador_e.subtitulo_posteo,
                'contenido_juego':jugador_e.contenido_juego,
                'imagen_juego': jugador_e.imagen_juego,
                'autor': jugador_e.autor
            }
        )
    }



    return render(request, 'AppGame/juegos_formulario.html', contexto) 


@login_required
def editar_consola(request, modelo):
    jugador_e = Consola.objects.get(modelo=modelo)
    


    if request.method == 'POST':
        mi_formular = ConsolaFormulario(request.POST,request.FILES)

        if mi_formular.is_valid():
            data = mi_formular.cleaned_data
           
            
            
            jugador_e.marca= data.get('marca'),
            jugador_e.modelo = data.get('modelo'),
            jugador_e.titulo= data.get('titulo'),
            jugador_e.subtitulo=data.get('subtitulo'),
            jugador_e.contenido=data.get('contenido'),
            jugador_e.imagen_consola=data.get('imagen_consola')
            jugador_e.save()
           
            titulo = data.get('titulo')
            

            messages.success(request,f'Se creo {titulo} correctamente')

            return redirect('AppGameConsola')
        else:
            messages.error(request, mi_formular.errors)    
    contexto={
        'form' : ConsolaFormulario(
            initial={ 
                'marca':jugador_e.marca,
                'modelo': jugador_e.modelo,
                
                'titulo':jugador_e.titulo,
                'subtitulo':jugador_e.subtitulo,
                'contenido':jugador_e.contenido,
                'imagen_consola': jugador_e.imagen_consola,
                'autor': jugador_e.autor
            }
        )
    }



    return render(request, 'AppGame/consola_formulario.html', contexto)


@login_required
def eliminar_categoria(request, categoria):
    categoria_eliminar = Juegos.objects.get(categoria= categoria)
    categoria_eliminar.delete()

    messages.info(request,f'El modelo {categoria_eliminar} fue eliminado')

    return redirect('AppGameJuegos')


@login_required
def eliminar_modelo(request, modelo):
    modelo_eliminar = Consola.objects.get(modelo=modelo)
    modelo_eliminar.delete()

    messages.info(request,f'El modelo {modelo_eliminar} fue eliminado')

    return redirect('AppGameConsola')


@login_required
def editar_jugador(request,apodo):
    jugador_e = Jugador.objects.get(apodo=apodo)
    


    if request.method == 'POST':
        mi_formular = JugadorFormulario(request.POST,request.FILES)

        if mi_formular.is_valid():
            data = mi_formular.cleaned_data
           
            
            jugador_e.nombre= data.get('nombre')
            jugador_e.apellido = data.get('apellido')
            jugador_e.apodo= data.get('apodo')
            jugador_e.titulo_post= data.get('titulo_post')
            jugador_e.subtitulo_post=data.get('subtitulo_post')
            jugador_e.contenido_post=data.get('contenido_post')
            jugador_e.imagen_post=data.get('imagen_post')
           
            jugador_e.save()
           
            titulo_post = data.get('titulo_post')
            

            messages.success(request,f'Se creo {titulo_post} correctamente')

            return redirect('AppGameJugador')
        else:
            messages.error(request, mi_formular.errors)    
    contexto={
        'form' : JugadorFormulario(
            initial={ 
                'nombre':jugador_e.nombre,
                'apodo': jugador_e.apodo,
                'apellido': jugador_e.apellido,
                'titulo_post':jugador_e.titulo_post,
                'subtitulo_post':jugador_e.subtitulo_post,
                'contenido_post':jugador_e.contenido_post,
                'imagen_post': jugador_e.imagen_post,
                'autor': jugador_e.autor
            }
        )
    }



    return render(request, 'AppGame/jugador_formulario.html', contexto)
    

@login_required
def eliminar_apodo(request,apodo ):
    apodo_eliminar = Jugador.objects.get(apodo=apodo)
    apodo_eliminar.delete()

    messages.info(request,f'El apodo {apodo_eliminar} fue eliminado')

    return render(request,'AppGame/detalle_jugador.html')

@login_required
def ver_jugador(request,apodo ):
    jugador_ver= Jugador.objects.get(apodo=apodo)
    
    contexto = {'jugador_ver':jugador_ver}
   

    messages.info(request,f'Viendo {jugador_ver.titulo_post} ',contexto)

    return render(request,'AppGame/detalle_jugador.html')


def busqueda_categoria_post(request):

    categoria = request.GET.get('categoria')

    juegos = Juegos.objects.filter(categoria__icontains=categoria)
    contexto = {
        'juegos': juegos

    }
    return render(request, 'AppGame/juegos_filtrados.html' , contexto)


@login_required
def busqueda_categoria(request):
    contexto = {

        'form': BusquedaCategoriaFormulario(),
    
    }

    return render(request ,'AppGame/busqueda_categoria.html', contexto)


@login_required
def juegos_formulario(request):


    if request.method == 'POST':
        mi_formular = JuegosFormulario(request.POST,request.FILES)

        if mi_formular.is_valid():
            data = mi_formular.cleaned_data
            juego1 = Juegos(
                autor= request.user,
                juego= data.get('juego'),
                categoria = data.get('categoria'),
                titulo_posteo= data.get('titulo_posteo'),
                subtitulo_posteo=data.get('subtitulo_posteo'),
                contenido_juego=data.get('contenido_juego'),
                imagen_juego=data.get('imagen_juego')
                )
            juego1.save()
           
            titulo_posteo = data.get('titulo_posteo')
            

            messages.success(request,f'Se creo {titulo_posteo} correctamente')

            return redirect('AppGameJuegos')
        else:
            messages.error(request, mi_formular.errors)    
        
        
        
    mi_formular= JuegosFormulario()

        

    
    return render(request, 'AppGame/juegos_formulario.html' , {'form': mi_formular})


def busqueda_modelo_post(request):
    modelo = request.GET.get('modelo')

    consolas = Consola.objects.filter(modelo__icontains=modelo)
    contexto = {
        'consolas': consolas

    }
    return render(request, 'AppGame/consolas_filtrada.html' , contexto)


@login_required
def busqueda_modelo(request):
    contexto = {

        'form': BusquedaModeloFormulario(),
    
    }

    return render(request ,'AppGame/busqueda_modelo.html', contexto)


@login_required
def consola_formulario(request):
    if request.method == 'POST':
        mi_formula = ConsolaFormulario(request.POST,request.FILES)

        if mi_formula.is_valid():
            data = mi_formula.cleaned_data
            consola1 = Consola(
                autor= request.user,
                modelo=data.get('modelo'),
                marca= data.get('marca'),
                titulo= data.get('titulo'),
                subtitulo=data.get('subtitulo'),
                contenido=data.get('contenido'),
                imagen_consola=data.get('imagen_consola')
                )
            consola1.save()
           
            titulo = data.get('titulo')
            

            messages.success(request,f'Se creo {titulo} correctamente')

            return redirect('AppGameConsola')
        else:
            messages.error(request, mi_formula.errors)    
        
        
        
    mi_formula= ConsolaFormulario()

        

    
    return render(request, 'AppGame/consola_formulario.html' , {'form': mi_formula})


def busqueda_apodo_post(request):
    apodo = request.GET.get('apodo')

    jugadores = Jugador.objects.filter(apodo__icontains=apodo)
    contexto = {
        'jugadores': jugadores

    }
    return render(request, 'AppGame/jugador_filtrado.html' , contexto)


@login_required
def busqueda_apodo(request):
    contexto = {

        'form': BusquedaApodoFormulario(),
    
    }

    return render(request ,'AppGame/busqueda_apodo.html', contexto)


@login_required  
def jugador_formulario(request):


    if request.method == 'POST':
        mi_formular = JugadorFormulario(request.POST,request.FILES)

        if mi_formular.is_valid():
            data = mi_formular.cleaned_data
            jugador1 = Jugador(
                autor= request.user,
                nombre= data.get('nombre'),
                apellido = data.get('apellido'),
                apodo= data.get('apodo'),
                titulo_post= data.get('titulo_post'),
                subtitulo_post=data.get('subtitulo_post'),
                contenido_post=data.get('contenido_post'),
                imagen_post=data.get('imagen_post')
                )
            jugador1.save()
           
            titulo_post = data.get('titulo_post')
            

            messages.success(request,f'Se creo {titulo_post} correctamente')

            return redirect('AppGameJugador')
        else:
            messages.error(request, mi_formular.errors)    
        
        
        
    mi_formular= JugadorFormulario()

        

    
    return render(request, 'AppGame/jugador_formulario.html' , {'form': mi_formular})
    

def consola(request):
    consola_listado = Consola.objects.all()
    paginator= Paginator(consola_listado, 2)
    pagina = request.GET.get('page') or 1
    consola = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, consola.paginator.num_pages +1 )
    
    return render(request,'AppGame/consola.html',{'consola':consola,'paginas':paginas,'pagina_actual':pagina_actual})
    

def juego(request):
    juego_listado = Juegos.objects.all()
    paginator= Paginator(juego_listado, 2)
    pagina = request.GET.get('page') or 1
    juego = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, juego.paginator.num_pages +1 )
    
    return render(request,'AppGame/juegos.html',{'juego':juego,'paginas':paginas,'pagina_actual':pagina_actual})


def jugador(request):
    jugador_listado = Jugador.objects.all()
    paginator= Paginator(jugador_listado, 2)
    pagina = request.GET.get('page') or 1
    jugador = paginator.get_page(pagina)
    pagina_actual = int(pagina)
    paginas = range(1, jugador.paginator.num_pages +1 )
    
    return render(request,'AppGame/jugador.html',{'jugador':jugador,'paginas':paginas,'pagina_actual':pagina_actual})


def inicio(request):
    return render(request,'index.html')

