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
