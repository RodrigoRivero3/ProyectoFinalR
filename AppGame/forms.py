
from django import forms

class JugadorFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    apodo = forms.CharField(max_length=30)


class BusquedaApodoFormulario(forms.Form):
    apodo = forms.CharField(max_length=30)

class ConsolaFormulario(forms.Form):
    marca = forms.CharField(max_length=40)
    modelo = forms.CharField(max_length=30)
    
class BusquedaModeloFormulario(forms.Form):
    modelo = forms.CharField(max_length=30)    


class JuegosFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    categoria = forms.CharField(max_length=30)
    fecha_salida = forms.DateField()

class BusquedaCategoriaFormulario(forms.Form):
    categoria = forms.CharField(max_length=30)