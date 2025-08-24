class Player:
    def __init__(self, nombre, ficha):
        self.__nombre__ = nombre
        self.__ficha__ = ficha

    def __str__(self):
        return f"Jugador: {self.__nombre__}, Ficha: {self.__ficha__}"