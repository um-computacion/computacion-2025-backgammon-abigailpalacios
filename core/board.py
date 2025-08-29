class Board:
    def __init__(self):
        self.__tablero__ = [None]*24   #Defino el tablero y sus posiciones
    
    def inicializar(self):  #A continiacion coloco las fichas en su lugar inicial para poder comenzar la partida
        self.__tablero__[0] = ["Blancas"]*2
        self.__tablero__[11] = ["Blancas"]*5
        self.__tablero__[16] = ["Blancas"]*3
        self.__tablero__[18] = ["Blancas"] *5   
       
        self.__tablero__[5] = ["Negras"] * 5
        self.__tablero__[7] = ["Negras"] * 3
        self.__tablero__[12] = ["Negras"] *5
        self.__tablero__[23] = ["Negras"] * 2

    def banco(self):    #Inicializamos el banco para las fichas comidas
        self.__banco__ = {"Blancas": 0, "Negras":0}
        return self.__banco__
    
    def mostrar_tablero(self):
        return self.__tablero__
    
    def distancia(self, pos_origen, pos_destino,ficha): #determina si el movimiento que se quiere hacer es valido (que avance resptectivamente)
        if ficha == "Blancas":
            return pos_destino - pos_origen
        if ficha == "Negras":
            return pos_origen - pos_destino
        else:
            raise ValueError("Ficha invalida")
        

    def validar_movimiento(self, pos_destino, pos_origen, ficha):  #Validamos los movimientos que puede hacer cada jugador
        pos_origen= int(pos_origen)
        pos_destino = int(pos_destino)
        if pos_destino <0 or pos_destino > 23 or pos_origen < 0 or pos_origen > 23: #la posicion de origen y destino deben estar entre 0 y 23
            raise ValueError("Posicion de destino invalida")
        if not self.__tablero__[pos_origen]:  #Debe haber un error si en la posicion de origen no hay ninguna ficha
            raise ValueError("No hay fichas en el lugar de origen")
        if ficha == "Blancas" and pos_destino <= pos_origen:  #Las fichas blancas pueden moverse hacia delante (de 0 a 23)
            raise ValueError("Movimiento invalido para fichas blancas")
        if ficha == "Negras" and pos_destino >= pos_origen: #Las fichas negras pueden moverse hacia atras (de 23 a 0)
            raise ValueError("Movimiento invalido para fichas negras")
        if self.distancia(pos_origen, pos_destino, ficha) <= 0:
            raise ValueError("Movimiento invalido")
        
    def ficha_comida(self, ficha, pos_destino):
        if self.__tablero__[pos_destino] == None:
            return False
        if len(self.__tablero__[pos_destino]) == 1 and self.__tablero__[pos_destino][0] != ficha: #comparo que sea solo una la ficha que se encuentra en esa posicion y que las fichas sean distintas
            oponente = self.__tablero__[pos_destino][0] 
            self.__tablero__[pos_destino] = [ficha] #agrego la ficha que comio a la posicion
            self.__banco__[oponente] += 1  #agrego la ficha comida al banc0
            return True
        
    def devolver_ficha_comida(self, ficha):
        if self.__banco__[ficha] <= 0: #si en el banco no hay fichas, no se puede devolver ninguna ficha
            raise ValueError("No hay fichas en el banco")
        if self.__banco__[ficha] >0:
            self.__banco__[ficha] -= 1 #restamos una ficha del banco
            return
        
    def mover_ficha(self, pos_origen, pos_destino, ficha):
        self.validar_movimiento(pos_destino, pos_origen, ficha)
        if self.__tablero__[pos_destino] is None: #Si la posicion de la ficha esta vacia, agrego la ficha
            self.__tablero__[pos_destino] = [ficha]
        else:
            self.__tablero__[pos_destino].append(ficha) #si hay fichas, agrego otra a la lista
        
        self.__tablero__[pos_origen].pop() #Luego de cualquier movimiento, debo remover la ficha de la posicion
        
        if not self.__tablero__[pos_origen]: #Si la lista queda vacia, la pongo en None
            self.__tablero__[pos_origen] = None
