from click import password_option
from django.test import TestCase
from AppGame.models import *


class GameTest(TestCase):

    def setUp(self):
        Jugador.objects.create(nombre='rodrigo', apodo='FenRoh')
        Jugador.objects.create(nombre='rodri', apodo='FenR')

    def test_jugador(self):
        p1 = Jugador.objects.get(apodo='FenRoh')
        p2 = Jugador.objects.get(apodo='FenR')
        self.assertEqual(p1.nombre,'rodrigo')
        self.assertEqual(p2.nombre,'rodri')


class ConsolaTest(TestCase):
    def setUp(self):
        Consola.objects.create(marca='playstation', modelo='ps5')
        Consola.objects.create(marca='playsn', modelo='ps3')

    def test_consola(self):
        c1 = Consola.objects.get(modelo='ps5')
        c2 = Consola.objects.get(modelo='ps3')
        self.assertEqual(c1.marca,'playstation')
        self.assertEqual(c2.marca,'playsn')

class JuegosTest(TestCase):
    def setUp(self):
        Juegos.objects.create(juego='resident', categoria='accion')
        Juegos.objects.create(juego='resi', categoria='acc')

    def test_consola(self):
        j1 = Juegos.objects.get(categoria='accion')
        j2 = Juegos.objects.get(categoria='acc')
        self.assertEqual(j1.juego,'resident')
        self.assertEqual(j2.juego,'resi')



