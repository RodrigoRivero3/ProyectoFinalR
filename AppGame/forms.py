
from django import forms

class JugadorFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    apodo = forms.CharField(max_length=30)


class BusquedaApodoFormulario(forms.Form):
    apodo = forms.CharField()