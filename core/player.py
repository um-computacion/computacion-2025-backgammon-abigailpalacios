class Player:
    def __init__(self, nombre, ficha):
        self.__nombre__ = nombre
        self.__ficha__ = ficha

    def get_nombre(self):
        return self.__nombre__
    
    def get_ficha(self):
        return self.__ficha__

    def __str__(self):
        return f"Jugador: {self.__nombre__}, Ficha: {self.__ficha__}"