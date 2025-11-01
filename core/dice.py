"""Modulo que maneja los dados del juego."""
import random

class Dice:
    """Clase que representa los dados del juego."""

    def __init__(self):
        """Inicializa los dados."""
        self.__dado1__ = 0
        self.__dado2__ = 0
        self.__movimiento__ = []

    def tirar(self):
        """Tira los dados y genera los movimientos disponibles."""
        self.__dado1__ = random.randint(1, 6)
        self.__dado2__ = random.randint(1, 6)
        if self.__dado1__ != self.__dado2__:
            self.__movimiento__ = [self.__dado1__, self.__dado2__]
        else:
            self.__movimiento__ = [self.__dado1__] * 4

    def get_movimiento(self):
        """Retorna la lista de movimientos disponibles."""
        return self.__movimiento__
