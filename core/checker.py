
class Checker():
    def __init__(self, ficha, posicion):
        """
        Inicializa una ficha.
        Args:
            ficha (str): El color de la ficha ("Blancas" o "Negras").
            posicion (int o str): El punto del tablero (0-23) o "Banco", "Ficha afuera".
        """
        self.__checker__ = ficha
        self.__posicion__ = posicion #Para saber donde esta cada ficha individualmente

    def get_ficha(self):
        """Devuelve el color de la ficha."""
        return self.__checker__
    
    def get_movimiento(self):
        """Devuelve la posición actual de la ficha."""
        return self.__posicion__ #Para saber donde esta cada ficha individualmente

    def en_banco(self):
        """Devuelve True si la ficha está en el banco, sino False."""
        if self.__posicion__ == "Banco":
            return True
        return False
    
    def ficha_afuera(self):
        """Devuelve True si la ficha está fuera del juego, sino False."""
        return self.__posicion__ == "Ficha afuera"
    
    def __str__(self):
        """Devuelve una representación en string de la ficha."""
        return (f"La ficha {self.__checker__}, se encuentra en la posicion: {self.__posicion__}")