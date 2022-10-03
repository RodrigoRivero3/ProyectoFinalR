
from dataclasses import fields
from django import forms

from django.utils import timezone
from django.contrib.auth.models import User

from AppGame.models import Juegos, Jugador,Consola


class JugadorFormulario(forms.ModelForm):
   class Meta:
    model = Jugador
    fields= (
        'nombre','apellido',
        'apodo','titulo_post',
        'subtitulo_post','contenido_post',
        'imagen_post'
    )
    
    
    


class BusquedaApodoFormulario(forms.Form):
    apodo = forms.CharField(max_length=30)

class ConsolaFormulario(forms.ModelForm):
   class Meta:
    model = Consola
    fields = (
        'marca','modelo', 'titulo',
        'subtitulo','contenido',
        'imagen_consola'
    )

class BusquedaModeloFormulario(forms.Form):
    modelo = forms.CharField(max_length=30)    


class JuegosFormulario(forms.ModelForm):
    class Meta:
        model= Juegos
        fields= (
            'juego','categoria',
            'titulo_posteo','subtitulo_posteo',
            'contenido_juego','imagen_juego'
        )
class BusquedaCategoriaFormulario(forms.Form):
    categoria = forms.CharField(max_length=30)