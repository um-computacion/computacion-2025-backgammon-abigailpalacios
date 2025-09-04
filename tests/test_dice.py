import unittest
from core.dice import Dice
from unittest.mock import patch

class TestDice(unittest.TestCase):
    
    def test_dado_nuevo(self):
        dado = Dice()
        self.assertEqual(dado.get_movimiento(), [])

    def test_tirar_dado(self):
        dado = Dice()
        dado.tirar()
        self.assertTrue(all(1 <= x <= 6 for x in dado.get_movimiento()))

    def test_dado_doble(self):
        dado = Dice()
        dado.tirar()
        dado.__dice1__ = dado.__dice2__ 
        dado.__dice1__ = 1
        self.assertEqual(dado.get_movimiento(), [1, 1, 1, 1])
    
    @patch('random.randint', side_effect=[5, 2])
    def test_tirada_simple(self, mock_randint):
        dado = Dice()
        dado.tirar()
        mov = dado.get_movimiento()
        self.assertEqual(len(mov), 2)
        self.assertEqual(mov[0], 5)
        self.assertEqual(mov[1], 2)
        self.assertTrue(mock_randint.called)
        self.assertEqual(mock_randint.call_count, 2)

    @patch('random.randint', return_value=1)
    def test_tirada_doble(self, mock_randint):
        dado = Dice()
        dado.tirar()
        mov = dado.get_movimiento()
        self.assertEqual(len(mov), 4)
        self.assertEqual(mov, [1, 1, 1, 1])
        self.assertTrue(mock_randint.called)
        self.assertEqual(mock_randint.call_count, 2)

    @patch('random.randint', side_effect=Exception("error!!"))
    def test_error_en_randint(self, mock_randint):
        dado = Dice()
        try:
            dado.tirar()
        except Exception as e:
            self.assertEqual(str(e), "error!!")
        self.assertTrue(mock_randint.called)
        self.assertEqual(mock_randint.call_count, 1)

    def test_dado_doble(self):
        dado = Dice()
        dado.tirar()
        dado.__dice1__ = 1
        dado.__dice2__ = 1
        dado.__movimiento__ = [1,1,1,1]
        self.assertNotEqual(dado.get_movimiento(), [2, 2, 2, 2])
    
    
if __name__ == '__main__':
    unittest.main()