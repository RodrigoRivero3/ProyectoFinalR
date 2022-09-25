from django.test import TestCase
from AppGame.models import Jugador

class GameTest(TestCase):

    def setUp(self):
        Jugador.objects.create(nombre='rodrigo', apodo='FenRoh')
        Jugador.objects.create(nombre='rodri', apodo='FenR')

    def test_animal_can_speak(self):
        p1 = Jugador.objects.get(apodo='FenRoh')
        p2 = Jugador.objects.get(apodo='FenR')
        self.assertEqual(p1.nombre,'rodrigo')
        self.assertEqual(p2.nombre,'rodri')


# FALTO PRUEBAS PARA VISTAS , LE SAQUE FOTO