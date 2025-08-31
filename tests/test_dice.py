import unittest
from core.dice import Dice

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
        dado.__dice1__ = 1
        dado.__dice2__ = 1
        dado.__movimiento__ = [1,1,1,1]
        self.assertEqual(dado.get_movimiento(), [1, 1, 1, 1])
    
    
if __name__ == '__main__':
    unittest.main()