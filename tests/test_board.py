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

    def test_variables_como_string(self):
        board = Board()
        board.inicializar()
        self.assertIsNone(board.validar_movimiento("13", "7", "Blancas"))

if __name__ == '__main__':
    unittest.main()