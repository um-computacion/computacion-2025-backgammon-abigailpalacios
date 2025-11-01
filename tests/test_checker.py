import unittest
from core.checker import Checker

class TestChecker(unittest.TestCase):

    def test_get_ficha(self):
        checker = Checker("Negras", 5)
        self.assertEqual(checker.get_ficha(), "Negras")

    def test_get_movimiento(self):
        checker = Checker("Blancas", 4)
        self.assertEqual(checker.get_movimiento(), 4)

    def test_en_banco(self):
        checker = Checker("Negras", 6)
        self.assertFalse(checker.en_banco(), "Banco")

    def test_no_esta_en_banco(self):
        checker = Checker("Blancas", "Banco")
        self.assertTrue(checker.en_banco(), "Banco")

    def test_ficha_afuera(self):
        checker = Checker("Blancas", "Ficha afuera")
        self.assertTrue(checker.ficha_afuera(), "Ficha afuera")

    def test_ficha_adentro(self):
        checker = Checker("Blancas", 7)
        self.assertFalse(checker.ficha_afuera(), "Ficha afuera")

    def test_str(self):
        checker = Checker("Blanca", 20)
        self.assertEqual(str(checker), "La ficha Blanca, se encuentra en la posicion: 20")
