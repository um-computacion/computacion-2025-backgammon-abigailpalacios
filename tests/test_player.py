import unittest
from core.player import Player

class TestPlayer(unittest.TestCase):
    def test_crear_player1(self):
        player = Player("Mar","Blancas")
        self.assertEqual(player.__nombre__, "Mar")
        self.assertEqual(player.__ficha__, "Blancas")

    def test_crear_player2(self):
        player = Player("Tincho", "Negras")
        self.assertEqual(player.__nombre__, "Tincho")
        self.assertEqual(player.__ficha__, "Negras")

    def test_str(self):
        player = Player("Franco", "Blancas")
        self.assertEqual(str(player), "Jugador: Franco, Ficha: Blancas")

    def test_dos_jugadores(self):
        player1 = Player("Mar", "Blancas")
        player2 = Player("Tincho", "Negras")
        self.assertEqual(str(player1),"Jugador: Mar, Ficha: Blancas")
        self.assertEqual(str(player2), "Jugador: Tincho, Ficha: Negras")

if __name__ == '__main__':
    unittest.main()