from .player import Player
from .board import Board
from .checker import Checker
from .dice import Dice


class Backgammongame():
    def __init__(self, player1, player2):
        self.__player1__ = Player(player1, "Blancas")
        self.__player2__ = Player(player2, "Negras")
        self.__board__ = Board()
        self.__dice__ = Dice()
        self.__turno__ = self.__player1__
        self.__board__.inicializar()
        self.banco = self.__board__.banco()

    def get_player1(self):
        return self.__player1__

    def get_player2(self):
        return self.__player2__

    
    def get_board(self):
        return self.__board__ 
    
    def get_banco(self):
        return self.banco

    def definir_turno(self):
        if self.__turno__ == self.__player1__: 
            self.__turno__ = self.__player2__
        else:
            self.__turno__ = self.__player1__

    def get_turno(self): 
            return self.__turno__

    def tirar_dados(self):
        self.__dice__.tirar()
        return self.__dice__.get_movimiento()
    