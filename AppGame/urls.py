from django.urls import path

from AppGame.views import *

urlpatterns = [
    path('', inicio , name= 'AppGameInicio'),
    path('jugador/', jugador, name='AppGameJugador'),
    path('consola/', consola, name= 'AppGameConsola'),
    path('juegos/',juegos, name='AppGameJuegos'),
    path('jugador_formulario/', jugador_formulario, name='AppGameJugadorFormulario'),
    path('busqueda_apodo/', busqueda_apodo, name='AppGameBusquedaJugadorApodo'),
    path('busqueda_apodo_post/', busqueda_apodo_post),
    path('consola_formulario/', consola_formulario , name='AppGameConsolaFormulario'),
    path('busqueda_modelo/', busqueda_modelo, name='AppGameBusquedaConsolaModelo'),
    path('busqueda_modelo_post/', busqueda_modelo_post),
    path('juegos_formulario/', juegos_formulario, name='AppGameJuegosFormulario'),
    path('busqueda_categoria/', busqueda_categoria, name='AppGameBusquedaJuegosCategoria'),
    path('busqueda_categoria_post/', busqueda_categoria_post)

    
]