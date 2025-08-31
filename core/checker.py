class Checker():
    def __init__(self, ficha, posicion):
        self.__checker__ = ficha
        self.__posicion__ = posicion #Para saber donde esta cada ficha individualmente

    def get_ficha(self):
        return self.__checker__
    
    def get_movimiento(self):
        return self.__posicion__ #Para saber donde esta cada ficha individualmente

    def en_banco(self):
        if self.__posicion__ == "Banco":
            return True
        return False
    
    def ficha_afuera(self):
        return self.__posicion__ == "Ficha afuera"
    
    def __str__(self):
        return (f"La ficha {self.__checker__}, se encuentra en la posicion: {self.__posicion__}")
