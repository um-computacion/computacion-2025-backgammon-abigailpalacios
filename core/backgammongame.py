from core.player import Player
from core.board import Board
from core.checker import Checker
from core.dice import Dice


class Backgammongame():
    def __init__(self, player1, player2):
        self.__player1__ = Player(player1, "Blancas")
        self.__player2__ = Player(player2, "Negras")
        self.__board__ = Board()
        self.__dice__ = Dice()
        self.__turno__ = self.__player1__
        self.__board__.inicializar()
        self.banco = self.__board__.banco()

    #Getters basicos

    def get_player1(self):
        return self.__player1__

    def get_player2(self):
        return self.__player2__

    
    def get_board(self):
        return self.__board__ 
    
    def get_banco(self):
        return self.banco

    def definir_turno(self):
        if self.__turno__ == self.__player1__:  #si el turno es del jugador 1, cambiamos al segundo jugador
            self.__turno__ = self.__player2__
        else:
            self.__turno__ = self.__player1__  #si el turno es del jugador 2, cambiamos al jugador 1
        self.__dice__ = Dice()     #inicializamos los dados para que el jugador que tiene el siguiente turno empieze con una lista nueva  

    def get_turno(self): 
            return self.__turno__

    def tirar_dados(self):
        self.__dice__.tirar()
        return self.__dice__.get_movimiento()
    
    def get_dados(self):
        return self.__dice__.get_movimiento()
    
    def dados_restantes(self):
        return list(self.__dice__.get_movimiento())
    
    def usar_dados(self, valido):
        movimiento = self.__dice__.get_movimiento() #verificamos que el dado  tenga valores para poder mover las fichas       
        if valido in movimiento:                                
            movimiento.remove(valido)     #remueve el valor usado, (por ejemplo, si tiro los dados y me devuelve 4,5 y uso el 4, no me deje volver a usar el 4)                      
        else:
            raise ValueError("Ese valor de dado no está disponible")
        
    