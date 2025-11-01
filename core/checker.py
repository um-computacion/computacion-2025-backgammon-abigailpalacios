"""
Módulo Checker
Define la clase Checker que representa una ficha individual del juego.
"""


class Checker:
    """
    Representa una ficha individual, rastreando su color
    y su posición actual en el tablero.
    """

    def __init__(self, ficha, posicion):
        """
        Inicializa una nueva ficha (checker).

        Args:
            ficha (str): El color de la ficha ("Blancas" o "Negras").
            posicion (int o str): El punto del tablero (0-23) o "Banco", "Ficha afuera".
        """
        self.__checker__ = ficha
        self.__posicion__ = posicion

    def get_ficha(self):
        """Devuelve el color de la ficha."""
        return self.__checker__

    def get_movimiento(self):
        """Devuelve la posición actual de la ficha."""
        return self.__posicion__

    def en_banco(self):
        """Devuelve True si la ficha está en el banco, sino False."""
        return self.__posicion__ == "Banco"

    def ficha_afuera(self):
        """Devuelve True si la ficha está fuera del juego, sino False."""
        return self.__posicion__ == "Ficha afuera"

    def __str__(self):
        """Devuelve una representación en string de la ficha."""
        return f"La ficha {self.__checker__}, se encuentra en la posicion: {self.__posicion__}"
