import random

class Dice:
    def __init__(self):
        self.__dice1__ = 0
        self.__dice2__ = 0
        self.__movimiento__ = []

    def tirar(self):
        self.__dice1__ = random.randint(1,6)
        self.__dice2__ = random.randint(1,6)
        if self.__dice1__ != self.__dice2__:
            self.__movimiento__ = [self.__dice1__,  self.__dice2__]
        else:
            self.__movimiento__ = [self.__dice1__, self.__dice1__, self.__dice1__, self.__dice2__]
        
    def get_movimiento(self):
        return self.__movimiento__