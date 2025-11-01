"""Modulo que representa a los jugadores."""


class Player:
    """Clase que representa un jugador del juego."""

    def __init__(self, nombre, ficha):
        """Inicializa un jugador con nombre y color de ficha."""
        self.__nombre__ = nombre
        self.__ficha__ = ficha

    def get_nombre(self):
        """Retorna el nombre del jugador."""
        return self.__nombre__

    def get_ficha(self):
        """Retorna el color de ficha del jugador."""
        return self.__ficha__

    def __str__(self):
        """Retorna representacion en texto del jugador."""
        return f"Jugador: {self.__nombre__}, Ficha: {self.__ficha__}"
