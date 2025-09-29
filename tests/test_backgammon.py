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

    def test_ganador_blncas(self):
        game = Backgammongame("Mar", "Franco")
        game.get_board().__tablero__ = [None] * 24  
        self.assertEqual(game.ganador(), "Mar")  

    def test_ganador_negras(self):
        game = Backgammongame("Mar", "Franco")
        game.get_board().__tablero__[5] = None
        game.get_board().__tablero__[7] = None
        game.get_board().__tablero__[12] = None  
        game.get_board().__tablero__[23] = None    
        self.assertEqual(game.ganador(), "Franco")  

    def test_no_hay_ganador(self):
        game = Backgammongame("Mar", "Franco")
        self.assertIsNone(game.ganador(), "Blancas")

    def test_posiciones_finales_blancas(self):
        game = Backgammongame("Mar", "Franco")
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[19] = ["Blancas"] * 2
        game.get_board().__tablero__[20] = ["Blancas"] * 2
        game.get_board().__tablero__[21] = ["Blancas"] * 7
        game.get_board().__tablero__[22] = ["Blancas"] * 4
        self.assertTrue(game.posiciones_finales())

    def test_posiciones_finales_blancas_false(self):
        game = Backgammongame("Mar", "Franco")
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[5] = ["Blancas"] * 2
        game.get_board().__tablero__[20] = ["Blancas"] * 2
        game.get_board().__tablero__[21] = ["Blancas"] * 7
        game.get_board().__tablero__[22] = ["Blancas"] * 4
        self.assertFalse(game.posiciones_finales())

    def test_posiciones_finales_negras(self):
        game = Backgammongame("Mar", "Franco")
        game.get_board().__tablero__ = [None] * 24
        game.definir_turno()
        game.get_board().__tablero__[5] = ["Negras"] * 2
        game.get_board().__tablero__[4] = ["Negras"] * 2
        game.get_board().__tablero__[3] = ["Negras"] * 7
        game.get_board().__tablero__[2] = ["Negras"] * 4
        self.assertTrue(game.posiciones_finales())

    def test_posiciones_finales_negras_false(self):
        game = Backgammongame("Mar", "Franco")
        game.get_board().__tablero__ = [None] * 24
        game.definir_turno()
        game.get_board().__tablero__[15] = ["Negras"] * 2
        game.get_board().__tablero__[4] = ["Negras"] * 2
        game.get_board().__tablero__[3] = ["Negras"] * 7
        game.get_board().__tablero__[2] = ["Negras"] * 4
        self.assertFalse(game.posiciones_finales())

    def test_retirar_excepcion_banco(self):
        game = Backgammongame("Mar", "Franco")
        game.definir_turno()
        game.get_banco()["Negras"] = 2
        self.assertRaises(ValueError, game.retirar_ficha, 2)

    def test_retirar_excepcion_posicion_final(self):
        game = Backgammongame("Mar", "Franco")
        game.definir_turno()
        game.get_board().__tablero__[15] = ["Negras"] * 2
        game.get_board().__tablero__[4] = ["Negras"] * 2
        game.get_board().__tablero__[3] = ["Negras"] * 7
        game.get_board().__tablero__[2] = ["Negras"] * 4
        self.assertRaises(ValueError, game.retirar_ficha, 2)

    def test_excepcion_sin_dados(self):
        game = Backgammongame("Mar", "Franco")
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[23] = ["Blancas"] 
        self.assertRaises(ValueError, game.retirar_ficha, 23)


    def test_excepcion_sin_ficha(self):
        game = Backgammongame("Mar", "Franco")
        game.get_board().__tablero__ = [None] * 24
        game.__dice__.__movimiento__ = [2]
        self.assertRaises(ValueError, game.retirar_ficha, 22)

    def test_retirar_dado_exacto_blancas(self):
        game = Backgammongame("Mar", "Franco")
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[20] = ["Blancas"] 
        game.__dice__.__movimiento__ = [4]
        game.retirar_ficha(20)
        self.assertEqual(game.get_board().mostrar_tablero()[20], None)

    def test_retirar_dado_exacto_negras(self):
        game = Backgammongame("Mar", "Franco")
        game.definir_turno()
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[3] = ["Negras"] 
        game.__dice__.__movimiento__ = [4]
        game.retirar_ficha(3)
        self.assertEqual(game.get_board().mostrar_tablero()[3], None)

    def test_retirar_dado_mayor_blancas(self):
        game = Backgammongame("Mar", "Franco")
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[20] = ["Blancas"] 
        game.__dice__.__movimiento__ = [6]
        game.retirar_ficha(20)
        self.assertEqual(game.get_board().mostrar_tablero()[20], None)

    def test_retirar_dado_menor_blancas(self):
        game = Backgammongame("Mar", "Franco")
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[20] = ["Blancas"] 
        game.__dice__.__movimiento__ = [2]
        self.assertRaises(ValueError, game.retirar_ficha, 20)

    def test_retirar_dado_mayor_negras(self):
        game = Backgammongame("Mar", "Franco")
        game.definir_turno()
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[3] = ["Negras"] 
        game.__dice__.__movimiento__ = [6]
        game.retirar_ficha(3)
        self.assertEqual(game.get_board().mostrar_tablero()[3], None)

    def test_retirar_ficha_tablero_queda_con_fichas(self):
        game = Backgammongame("Mar", "Franco")
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[20] = ["Blancas", "Blancas"]
        game.__dice__.__movimiento__ = [4]
        game.retirar_ficha(20)
        self.assertEqual(game.get_board().mostrar_tablero()[20], ["Blancas"])
        self.assertEqual(len(game.get_board().mostrar_tablero()[20]), 1)

    def test_retirar_dado_menor_negras(self):
        game = Backgammongame("Mar", "Franco")
        game.definir_turno()
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[3] = ["Negras"] 
        game.__dice__.__movimiento__ = [2]
        self.assertRaises(ValueError, game.retirar_ficha, 3)

    def test_retirar_excepcion_ficha_mayor_blancas(self):
        game = Backgammongame("Mar", "Franco")
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[20] = ["Blancas"] 
        game.get_board().__tablero__[22] = ["Blancas"] 
        game.__dice__.__movimiento__ = [6]
        self.assertRaises(ValueError, game.retirar_ficha, 22)

    def test_etirar_excepcion_ficha_mayor_negras(self):
        game = Backgammongame("Mar", "Franco")
        game.definir_turno()
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[3] = ["Negras"] 
        game.get_board().__tablero__[1] = ["Negras"] 
        game.__dice__.__movimiento__ = [6]
        self.assertRaises(ValueError,game.retirar_ficha, 1)

    def test_if_limpia_casilla_ejecucion(self):
        game = Backgammongame("Mar", "Franco")
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[20] = ["Blancas"]
        game.__dice__.__movimiento__ = [4] 
        game.retirar_ficha(20)
        self.assertIsNone(game.get_board().mostrar_tablero()[20]) 
    
    def test_moviminto_posibles_sin_banco(self):
        game = Backgammongame("Mar", "Franco")
        game.banco = {"Blancas": 1, "Negras": 0}
        game.get_board().inicializar()
        game.__dice__.__movimiento__ = [0, 2]
        self.assertEqual(game.movimientos_posibles(), {})

    def test_moviminto_posibles_sin_dados(self):
        game = Backgammongame("Mar", "Franco")
        game.banco = {"Blancas": 0, "Negras": 0}
        game.get_board().inicializar()
        game.__dice__.__movimiento__ = []
        self.assertEqual(game.movimientos_posibles(), {})

    def test_movimiento_posible_blancas(self):
        game = Backgammongame("Mar", "Franco")
        game.banco = {"Blancas": 0, "Negras": 0}
        game.get_board().inicializar()
        game.__dice__.__movimiento__ = [3, 6]
        movimientos_pos = {
            0: [3, 6],
            11: [14, 17],
            16: [19, 22],
            18: [21]
        }
        self.assertEqual(game.movimientos_posibles(), movimientos_pos)

    def test_movimiento_posible_negras(self):
        game = Backgammongame("Mar", "Franco")
        game.definir_turno()
        game.banco = {"Blancas": 0, "Negras": 0}
        game.get_board().inicializar()
        game.__dice__.__movimiento__ = [3, 6]
        movimientos_pos = {
            5: [2],
            7: [4, 1],
            12: [9, 6],
            23: [20, 17]
        }
        self.assertEqual(game.movimientos_posibles(), movimientos_pos)

    def test_movimiento_posible_excepcion(self):
        game = Backgammongame("Mar", "Franco")
        game.get_board().__tablero__[5] = ["Blancas"]
        game.get_board().__tablero__[7] = ["Negras", "Negras"]
        game.__dice__.__movimiento__ = [2]
        movimientos = game.movimientos_posibles()
        self.assertNotIn(5, movimientos)

    def test_movimiento_posible_blancas_retiran(self):
        game = Backgammongame("Mar", "Franco")
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[19] = ["Blancas"] 
        game.__dice__.__movimiento__ = [5]
        movimientos_pos = {19: ["retirar"]}
        self.assertEqual(game.movimientos_posibles(), movimientos_pos)

    def test_movimiento_posible_negras_retiran(self):
        game = Backgammongame("Mar", "Franco")
        game.definir_turno()
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[4] = ["Negras"] 
        game.__dice__.__movimiento__ = [5]
        movimientos_pos = {4: ["retirar"]}
        self.assertEqual(game.movimientos_posibles(), movimientos_pos)

    def test_movimiento_invalido_blancas(self):
        game = Backgammongame("Mar", "Franco")
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[0] = ["Blancas"]
        game.get_board().__tablero__[5] = ["Negras", "Negras"]  
        game.__dice__.__movimiento__ = [5]
        movimientos = game.movimientos_posibles()
        self.assertEqual(movimientos, {}) 

    def test_movimiento_invalido_negras(self):
        game = Backgammongame("Mar", "Franco")
        game.definir_turno()
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[5] = ["Blancas", "Blancas"]
        game.get_board().__tablero__[10] = ["Negras"]  
        game.__dice__.__movimiento__ = [5]
        self.assertEqual( game.movimientos_posibles(), {}) 

    def test_ficha_invalida(self):
        game = Backgammongame("Mar", "Franco")
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[4] = ["Rosa"] 
        game.__dice__.__movimiento__ = [2]
        self.assertEqual(game.movimientos_posibles(), {})

    def test_movimiento_posible_blancas_con_fichas_lejanas(self):
        game = Backgammongame("Mar", "Franco")
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[19] = ["Blancas"] 
        game.get_board().__tablero__[22] = ["Blancas"] 
        game.__dice__.__movimiento__ = [6]
        self.assertEqual( game.movimientos_posibles(), {22: ["retirar"]})

    def test_movimiento_posible_negras_con_fichas_lejanas(self):
        game = Backgammongame("Mar", "Franco")
        game.definir_turno()
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[4] = ["Negras"]  
        game.get_board().__tablero__[1] = ["Negras"]  
        game.__dice__.__movimiento__ = [6]
        self.assertEqual( game.movimientos_posibles(), {1: ["retirar"]})

    def test_movimiento_posible_destino_limite_blancas(self):
        game = Backgammongame("Mar", "Franco")
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[21] = ["Blancas"]
        game.__dice__.__movimiento__ = [3]  
        game.get_board().__tablero__[19] = ["Blancas"] 
        posible = {19: [22], 21: ["retirar"]}
        self.assertEqual(game.movimientos_posibles(), posible)

    def test_banco_sin_fichas(self):
        game = Backgammongame("Mar", "Franco")
        game.banco = {"Blancas": 0, "Negras": 0}
        self.assertEqual(game.reingreso_posible(), {})

    def test_banco_sin_dados(self):
        game = Backgammongame("Mar", "Franco")
        game.__dice__.__movimiento__ = []
        self.assertEqual(game.reingreso_posible(), {})

    def test_movimiento_posible_blancas(self):
        game = Backgammongame("Mar", "Franco")
        game.banco = {"Blancas": 1, "Negras": 0}
        game.get_board().__tablero__ = [None] * 24
        game.__dice__.__movimiento__ = [3]
        self.assertEqual(game.reingreso_posible(), {"reingresa": [2]})

    def test_mov_pos_blancas(self):
        game = Backgammongame("Mar", "Franco")
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[22] = ["Blancas"]
        game.get_board().__tablero__[10] = ["Blancas"]
        game.__dice__.__movimiento__ = [3, 4]
        self.assertEqual(game.movimientos_posibles(), {10: [13, 14]})
        
    def test_negras_dados(self):
        game = Backgammongame("Mar", "Franco")
        game.definir_turno()
        game.banco = {"Blancas": 0, "Negras": 1}
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[23] = ["Blancas", "Blancas"]  
        game.get_board().__tablero__[22] = ["Blancas", "Blancas"]  
        game.__dice__.__movimiento__ = [1, 2]
        self.assertEqual(game.reingreso_posible(), {})

    def test_mov_blancas_sobre_blancas(self):
        game = Backgammongame("Mar", "Franco")
        game.banco = {"Blancas": 1, "Negras": 0}
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[2] = ["Blancas", "Blancas"]  
        game.__dice__.__movimiento__ = [3]
        self.assertEqual(game.reingreso_posible(), {"reingresa": [2]})

    def test_blanco_come_negro(self):
        game = Backgammongame("Mar", "Franco")
        game.banco = {"Blancas": 0, "Negras": 1}
        game.definir_turno()
        game.get_board().__tablero__ = [None] * 24
        game.get_board().__tablero__[21] = [ "Blancas"]
        game.__dice__.__movimiento__ = [3]
        self.assertEqual(game.reingreso_posible(), {"reingresa": [21]})

    def test_reingreso_sin_dados_disponibles(self):
        game = Backgammongame("Mar", "Franco")
        game.banco = {"Blancas": 1, "Negras": 0}
        game.__dice__.__movimiento__ = []
        resultado = game.reingreso_posible()
        self.assertEqual(resultado, {})

    def test_estado_juego(self):
        game = Backgammongame("Mar", "Franco")
        game.banco = {"Blancas": 0, "Negras": 0}
        game.get_board().inicializar() 
        game.__dice__.__movimiento__ = [2, 3]
        
        estado = {
            "estado": "en curso",
            "turno": "Mar",
            "jugador 1": "Mar",
            "jugador 2": "Franco",
            "ficha actual": "Blancas",
            "dados": [2, 3],
            "tablero": game.get_board().mostrar_tablero(),
            "banco": {"Blancas": 0, "Negras": 0},
            "movimientos posibles": game.movimientos_posibles(),
            "reingreso posible": {},
            "ganador": None
        }
        
        self.assertEqual(game.estado_juego(), estado)

    def test_estado_juego_ganado(self):
        game = Backgammongame("Mar", "Franco")
        game.banco = {"Blancas": 0, "Negras": 0}
        game.get_board().__tablero__ = [None] * 24 
        game.__dice__.__movimiento__ = [2, 3]
        
        estado = {
            "estado": "ganado",  
            "turno": "Mar",
            "jugador 1": "Mar",
            "jugador 2": "Franco",
            "ficha actual": "Blancas",
            "dados": [2, 3],
            "tablero": [None] * 24,
            "banco": {"Blancas": 0, "Negras": 0},
            "movimientos posibles": {},
            "reingreso posible": {},
            "ganador": "Mar"  
        }
        
        self.assertEqual(game.estado_juego(), estado)

    def test_estado_juego_banco(self):
        game = Backgammongame("Mar", "Franco")
        game.banco = {"Blancas": 1, "Negras": 0}
        game.get_board().inicializar() 
        game.__dice__.__movimiento__ = [2, 3]
        
        estado = {
            "estado": "reingreso",
            "turno": "Mar",
            "jugador 1": "Mar",
            "jugador 2": "Franco",
            "ficha actual": "Blancas",
            "dados": [2, 3],
            "tablero": game.get_board().mostrar_tablero(),
            "banco": {"Blancas": 1, "Negras": 0},
            "movimientos posibles": {},
            "reingreso posible": {"reingresa": [1, 2]},
            "ganador": None
        }
        
        self.assertEqual(game.estado_juego(), estado)

if __name__ == '__main__':
    unittest.main()