import unittest
from core.board import Board

class TestBoard(unittest.TestCase):
    
    def test_veinticuatro_posiciones(self):
        board = Board()
        self.assertEqual(len(board.__tablero__),24)

    def test_posiciones_iniciales(self):
        board = Board()
        board.inicializar()
        self.assertEqual(board.__tablero__[0], ["Blancas"]*2)
        self.assertEqual(board.__tablero__[11], ["Blancas"]*5)
        self.assertEqual(board.__tablero__[16], ["Blancas"]*3)
        self.assertEqual(board.__tablero__[18], ["Blancas"]*5)
        self.assertEqual(board.__tablero__[5], ["Negras"]*5)
        self.assertEqual(board.__tablero__[7], ["Negras"]*3)
        self.assertEqual(board.__tablero__[12], ["Negras"]*5)
        self.assertEqual(board.__tablero__[23], ["Negras"]*2)

    def test_posiciones_vacias(self):
        board = Board()
        board.inicializar()
        self.assertEqual(board.__tablero__[1], None)
        self.assertEqual(board.__tablero__[2], None)
        self.assertEqual(board.__tablero__[3], None)
        self.assertEqual(board.__tablero__[4], None)
        self.assertEqual(board.__tablero__[6], None)
        self.assertEqual(board.__tablero__[8], None)
        self.assertEqual(board.__tablero__[9], None)
        self.assertEqual(board.__tablero__[10], None)
        self.assertEqual(board.__tablero__[13], None)
        self.assertEqual(board.__tablero__[14], None)
        self.assertEqual(board.__tablero__[15], None)
        self.assertEqual(board.__tablero__[17], None)
        self.assertEqual(board.__tablero__[19], None)
        self.assertEqual(board.__tablero__[20], None)
        self.assertEqual(board.__tablero__[21], None)
        self.assertEqual(board.__tablero__[22], None)

    def test_mostrar_tablero(self):
        board = Board()
        board.inicializar()
        self.assertEqual(board.mostrar_tablero(), board.__tablero__)

    def test_banco(self):
        board = Board()
        self.assertEqual(board.banco(), {"Blancas":0, "Negras":0})

    def test_validar_movimiento(self):
        board = Board()
        pos_destino = 13
        pos_origen = 7
        board.inicializar()
        resultado = board.validar_movimiento(pos_destino, pos_origen, "Blancas")
        self.assertIsNone(resultado)

    def test_movimiento_invalido_destino(self):
        board = Board()
        pos_destino = 26
        pos_origen = 6
        self.assertRaises(ValueError, board.validar_movimiento, pos_origen, pos_destino, "Blancas")

    def test_movimiento_invalido_origen(self):
        board = Board()
        pos_destino = 13
        pos_origen = -1
        self.assertRaises(ValueError, board.validar_movimiento,pos_destino, pos_origen, "Negras")

    def test_color_invalido(self):
        board = Board()
        pos_destino = 13
        pos_origen = 7
        self.assertRaises(ValueError, board.validar_movimiento, pos_destino, pos_origen, "Rojo")

    def test_validar_posicion_origen(self):
        board = Board()
        pos_destino = 13
        self.pos_origen = 6
        self.assertRaises(ValueError, board.validar_movimiento, self.pos_origen, pos_destino, "Negras")

    def test_posicion_ocupada(self):
        board = Board()
        board.inicializar()
        pos_origen = 0
        pos_destino = 7
        self.assertRaises(ValueError, board.validar_movimiento, pos_destino, pos_origen, "Negras")

    def test_validar_movimiento_blancas(self):
        board = Board()
        board.inicializar()
        pos_origen = 13
        pos_destino = 3
        self.assertRaises(ValueError, board.validar_movimiento, pos_destino, pos_origen, "Blancas")

    def test_validar_movimiento_negras(self):
        board = Board()
        board.inicializar()
        pos_origen = 13
        pos_destino = 3
        self.assertRaises(ValueError, board.validar_movimiento, pos_destino, pos_origen, "Negras") 

    def test_validar_orden_movimiento_blancas(self):
        board = Board()
        board.inicializar()
        self.assertRaises(ValueError, board.validar_movimiento, 11, 3, "Blancas") #las fichas blancas no pueden moverse hacia atras

    def test_validar_orden_movimiento_negras(self):
        board = Board()
        board.inicializar()
        self.assertRaises(ValueError, board.validar_movimiento, 12, 21, "Negras") #las fichas negras no pueden moverse hacia delante

    def test_variables_como_string(self):
        board = Board()
        board.inicializar()
        self.assertIsNone(board.validar_movimiento("13", "7", "Blancas"))

    def test_mover_destino_vacio_origen_vacio(self):
        board = Board()
        board.inicializar()
        board.mover_ficha(0,1, "Blancas")
        board.mover_ficha(0,1, "Blancas")
        self.assertEqual(board.__tablero__[0], None) #al sacar ambas fichas que habian en esta posicion, no queda vacia, queda en "None"
        self.assertEqual(board.__tablero__[1], ["Blancas", "Blancas"]) #se agregan dos fichas en esta posicion

    def test_mover_destino_vacio(self):
        board = Board()
        board.inicializar()
        board.mover_ficha(0,1, "Blancas")
        self.assertEqual(board.__tablero__[1], ["Blancas"]) #en la posicon 1 se agrega una ficha
        self.assertEqual(board.__tablero__[0], ["Blancas"])

    def test_mover_destino_ocupado(self):
        board = Board()
        board.inicializar()
        board.mover_ficha(0,11, "Blancas")
        self.assertEqual(board.__tablero__[11], ["Blancas"]*6) #en la posicion 11 se agrega una ficha blanca
        self.assertEqual(board.__tablero__[0], ["Blancas"])

    def test_origen_vacio(self):
        board = Board()
        board.inicializar()
        self.assertRaises(ValueError, board.mover_ficha, 1, 5, "Blancas") #no pueden moverse fichas de una posicion vacia

    def test_distancia_blancas(self):
        board = Board()
        self.assertEqual(board.distancia(5,15, "Blancas"),10)

    def test_distancia_negras(self):
        board = Board()
        self.assertEqual(board.distancia(15, 5, "Negras"),10)

    def test_distancia_invalida_blanca(self):
        board = Board()
        self.assertRaises(ValueError, board.validar_movimiento, 15, 5, "Blancas" )

    def test_distancia_invalida_negra(self):
        board = Board()
        self.assertRaises(ValueError, board.validar_movimiento, 5, 15, "Negras")

    def test_distancia_color_invalido(self):
        board = Board()
        self.assertRaises(ValueError, board.distancia, 5, 15, "Verde")

    def test_ficha_comida(self):
        board = Board()
        board.inicializar()
        board.banco()
        board.__tablero__[4] = ["Negras"]
        self.assertTrue(board.ficha_comida("Blanca", 4))
        self.assertEqual(board.__tablero__[4], ["Blanca"])
        self.assertEqual(board.__banco__["Negras"], 1)

    def test_ficha_no_comida(self):
        board = Board()
        board.inicializar()
        board.banco()
        board.__tablero__[4] = ["Negras", "Negras"]
        self.assertFalse(board.ficha_comida("Blanca", 4))
        self.assertEqual(board.__tablero__[4], ["Negras", "Negras"])
        self.assertEqual(board.__banco__["Negras"], 0)

    def test_posicion_vacia(self):
        board = Board()
        board.inicializar()
        board.banco()
        board.__tablero__[4] = None
        self.assertFalse(board.ficha_comida("Blanca", 4))

    def test_devolver_ficha(self):
        board = Board()
        board.inicializar()
        board.banco()
        board.__banco__["Blancas"] = 2
        board.devolver_ficha_comida("Blancas")
        self.assertEqual(board.__banco__["Blancas"], 1)

    def test_devolver_ficha_banco_vacio(self):
        board = Board()
        board.inicializar()
        board.banco()
        board.__banco__["Negras"] = 0
        self.assertRaises(ValueError, board.devolver_ficha_comida, "Negras")

if __name__ == '__main__':
    unittest.main()