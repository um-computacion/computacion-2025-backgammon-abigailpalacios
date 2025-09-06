import unittest
from core.backgammongame import Backgammongame
from core.player import Player
from core.board import Board
from core.checker import Checker
from core.dice import Dice

class TestBackgammon(unittest.TestCase):
    
    def test_init(self):
        game = Backgammongame("Tincho", "Mar")
        self.assertEqual(game.get_player1().get_nombre(), "Tincho" )
        self.assertEqual(game.get_player2().get_nombre(), "Mar")
        self.assertEqual(game.get_player1().get_ficha(), "Blancas")
        self.assertEqual(game.get_player2().get_ficha(), "Negras")
        self.assertEqual(game.get_banco(), {"Blancas": 0, "Negras":0})
        self.assertIsInstance(game.get_board(), Board)

    def test_turno(self):
        game = Backgammongame("Franco", "Martin")
        self.assertEqual(game.__turno__, game.__player1__) #Verificamos que el primer turno es el del jugador 1

    def test_cambiar_turno(self):
        game = Backgammongame("Franco", "Martin")
        self.assertEqual(game.get_turno().get_nombre(), "Franco")
        game.definir_turno()
        self.assertEqual(game.get_turno().get_nombre(), "Martin") #Cambiamos de turno (de jugador 1 a jugador 2)
        game.definir_turno()
        self.assertEqual(game.get_turno().get_nombre(), "Franco") #Volvemos a cambiar de turno (de jugador 2 a jugador 1)

    def test_cambiar_turno_invalido(self):
        game = Backgammongame("Franco", "Martin")
        self.assertNotEqual(game.get_turno().get_nombre(), "Martin") #El primer turno no puede ser del segundo jugador
        self.assertEqual(game.get_turno().get_nombre(), "Franco")

    def test_tirar_dados(self):
        game = Backgammongame("Franco", "Martin")
        self.assertTrue(all(1 <= x <= 6 for x in game.tirar_dados())) #verificamos la tirada de dados sea correcta