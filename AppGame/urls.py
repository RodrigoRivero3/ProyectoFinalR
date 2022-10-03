from django.urls import path

from AppGame.views import *

urlpatterns = [
    path('', inicio , name= 'AppGameInicio'),
    path('jugador/', jugador, name='AppGameJugador'),
    path('consola/', consola, name= 'AppGameConsola'),
    path('juegos/',juego, name='AppGameJuegos'),
    path('jugador_formulario/', jugador_formulario, name='AppGameJugadorFormulario'),
    path('busqueda_apodo/', busqueda_apodo, name='AppGameBusquedaJugadorApodo'),
    path('busqueda_apodo_post/', busqueda_apodo_post),
    path('consola_formulario/', consola_formulario , name='AppGameConsolaFormulario'),
    path('busqueda_modelo/', busqueda_modelo, name='AppGameBusquedaConsolaModelo'),
    path('busqueda_modelo_post/', busqueda_modelo_post),
    path('juegos_formulario/', juegos_formulario, name='AppGameJuegosFormulario'),
    path('busqueda_categoria/', busqueda_categoria, name='AppGameBusquedaJuegosCategoria'),
    path('busqueda_categoria_post/', busqueda_categoria_post),
    path('eliminar_apodo/<str:apodo>', eliminar_apodo, name='AppGameEliminarApodo'),
    path('editar_jugador/<str:apodo>', editar_jugador, name='AppGameEditarJugador'),
    path('eliminar_modelo/<str:modelo>', eliminar_modelo, name='AppGameEliminarModelo'),
    path('eliminar_categoria/<str:categoria>', eliminar_categoria, name='AppGameEliminarCategoria'),
    path('editar_consola/<str:modelo>', editar_consola, name='AppGameEditarConsola'),
    path('editar_juego/<str:categoria>', editar_juego, name='AppGameEditarJuegos'),
    path('ver_jugador/<str:apodo>', ver_jugador, name='AppGameVerJugador'),
    path('ver_juego/<str:categoria>', ver_juego, name='AppGameVerJuego'),
    path('ver_consola/<str:modelo>', ver_consola, name='AppGameVerConsola'),
    path('acerca_mio/', acerca_mio, name= 'AppGameAcercaMio')
    
    ]