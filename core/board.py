class Board:
    def __init__(self):
        self.__tablero__ = [None]*24 #Defino el tablero y sus posiciones
    
    def inicializar(self):
        #A continiacion coloco las fichas en su lugar inicial para poder comenzar la partida
        self.__tablero__[0] = ["Blancas"]*2
        self.__tablero__[11] = ["Blancas"]*5
        self.__tablero__[16] = ["Blancas"]*3
        self.__tablero__[18] = ["Blancas"] *5   

        self.__tablero__[5] = ["Negras"] * 5
        self.__tablero__[7] = ["Negras"] * 3
        self.__tablero__[12] = ["Negras"] *5
        self.__tablero__[23] = ["Negras"] * 2
