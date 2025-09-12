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

    def test_get_dados(self):
        game = Backgammongame("Franco", "Martin")
        game.tirar_dados() 
        self.assertTrue(game.get_dados(),all(1 <= x <= 6 for x in game.tirar_dados()))

    def test_usar_dado(self):
        game = Backgammongame("Mar", "Abril")
        game.__dice__.__movimiento__ = [6, 4]
        game.usar_dados(6)
        self.assertEqual(game.dados_restantes(), [4])

    def test_usar_dado_invalido(self):
        game = Backgammongame("Mar", "Abril")
        game.__dice__.__movimiento__ = [6, 4]
        game.usar_dados(6)
        self.assertNotEqual(game.dados_restantes(), [6,4])

    def test_usar_dado_invalido_excepcion(self):
        game = Backgammongame("Mar", "Abril")
        game.__dice__.__movimiento__ = [6, 4]
        with self.assertRaises(ValueError):
            game.usar_dados(3)
    
    def test_get_ficha(self):
        game = Backgammongame("Mar", "Abril")
        self.assertEqual(game.get_ficha(), "Blancas")  
        game.definir_turno()
        self.assertEqual(game.get_ficha(), "Negras")  

    def test_mover_ficha(self):
        game = Backgammongame("Mar", "Abril")
        game.get_board().inicializar()
        game.__dice__.__movimiento__ = [3, 6]
        game.mover_ficha(0, 3)
        self.assertEqual(game.dados_restantes(), [6])  
        self.assertEqual(game.get_board().mostrar_tablero()[3], ["Blancas"])
        self.assertEqual(game.get_board().mostrar_tablero()[0], ["Blancas"])

    def test_ficha_en_banco(self):
        game = Backgammongame("Mar", "Franco")
        game.get_banco()["Blancas"] = 1
        game.__dice__.__movimiento__ = [2, 6]
        with self.assertRaises(ValueError):
            game.mover_ficha(0, 2) 

    def test_sin_dados(self):
        game = Backgammongame("Mar", "Abril")
        game.get_board().inicializar()
        game.__dice__.__movimiento__ = [3]
        game.mover_ficha(0, 3)
        with self.assertRaises(ValueError):
            game.mover_ficha(3,7)

    def test_mover_ficha_blanca(self):
        game = Backgammongame ("Mar", "Franco")
        game.__dice__.__movimiento__ = [2, 5]
        game.mover_ficha(0, 2)
        self.assertEqual(game.dados_restantes(), [5])
        self.assertEqual(game.get_board().mostrar_tablero()[0], ["Blancas"])
        self.assertEqual(game.get_board().mostrar_tablero()[2], ["Blancas"])

    def test_mover_ficha_negra(self):
        game = Backgammongame("Mar", "Franco")
        game.definir_turno() 
        game.__dice__.__movimiento__ = [2, 6]  
        game.mover_ficha(7, 5)  
        self.assertEqual(game.dados_restantes(), [6])
        self.assertEqual(game.get_board().mostrar_tablero()[5], ["Negras"] * 6)
        self.assertEqual(game.get_board().mostrar_tablero()[7], ["Negras"] * 2)

    def test_pasos_blancas(self):
        game = Backgammongame("Mar", "Franco")
        game.__dice__.__movimiento__ = [2, 5]  
        game.mover_ficha(0, 2) 
        with self.assertRaises(ValueError):
            game.mover_ficha(2,0)

    def test_pasos_negras(self):
        game = Backgammongame("Mar", "Franco")
        game.definir_turno() 
        game.__dice__.__movimiento__ = [2, 6]  
        game.mover_ficha(7,5) 
        with self.assertRaises(ValueError):
            game.mover_ficha(5,7)

    def test_reingresar_ficha_blanca(self):
        game = Backgammongame("Mar", "Franco")
        game.get_banco()["Blancas"] = 1
        game.__dice__.__movimiento__ = [2, 5]  
        game.reingresar_ficha(2)
        self.assertEqual(game.dados_restantes(), [5])
        self.assertEqual(game.get_board().mostrar_tablero()[1], ["Blancas"])
        self.assertEqual(game.get_banco()["Blancas"], 0)

    def test_ingresar_ficha_invalido(self):
        game = Backgammongame("Mar", "Franco")
        game.get_banco()["Blancas"] = 1
        game.__dice__.__movimiento__ = [2, 5]  
        with self.assertRaises(ValueError):
            game.reingresar_ficha(11)

    def test_reingresar_ficha_negra(self):
        game = Backgammongame("Mar", "Franco")
        game.definir_turno() 
        game.get_banco()["Negras"] = 1
        game.__dice__.__movimiento__ = [2, 5]  
        game.reingresar_ficha(2)
        self.assertEqual(game.dados_restantes(), [5])
        self.assertEqual(game.get_board().mostrar_tablero()[22], ["Negras"])
        self.assertEqual(game.get_banco()["Negras"], 0)