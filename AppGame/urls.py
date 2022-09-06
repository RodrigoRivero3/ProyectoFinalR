from django.urls import path

from AppGame.views import *

urlpatterns = [
    path('', inicio , name= 'AppGameInicio'),
    path('jugador/', jugador, name='AppGameJugador'),
    path('consola/', consola, name= 'AppGameConsola'),
    path('juegos/',juegos, name='AppGameJuegos'),
    path('jugador_formulario/', jugador_formulario, name='AppGameJugadorFormulario'),
    path('busqueda_apodo/', busqueda_apodo, name='AppGameBusquedaJugadorApodo'),
    path('busqueda_apodo_post/', busqueda_apodo_post, name='AppGameBusquedaJugadorApodoPost')
]