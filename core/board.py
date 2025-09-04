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
        

    def validar_movimiento(self, pos_destino, pos_origen, ficha):  #Validamos los movimientos que puede hacer cada jugador
        pos_origen= int(pos_origen)
        pos_destino = int(pos_destino)
        if pos_destino <0 or pos_destino > 23 or pos_origen < 0 or pos_origen > 23: #la posicion de origen y destino deben estar entre 0 y 23
            raise ValueError("Posicion de destino invalida")
        elif not self.__tablero__[pos_origen]:  #Debe haber un error si en la posicion de origen no hay ninguna ficha
            raise ValueError("No hay fichas en el lugar de origen")
        elif ficha == "Blancas" and pos_destino <= pos_origen:  #Las fichas blancas pueden moverse hacia delante (de 0 a 23)
            raise ValueError("Movimiento invalido para fichas blancas")
        elif ficha == "Negras" and pos_destino >= pos_origen: #Las fichas negras pueden moverse hacia atras (de 23 a 0)
            raise ValueError("Movimiento invalido para fichas negras")
        elif self.__tablero__[pos_destino]  is not None and len(self.__tablero__[pos_destino]) >= 2 and self.__tablero__[pos_destino][0] != ficha: 
        #comparamos que en la posicion a donde se mueve no esta vacia, que la cantidad de fichas es 2 o mas y que las fichas sean distintas para corroborar que no se puede mover ahi
            raise ValueError("Movimiento invalido, posicion ocupada por oponente") 
    
        
    def ficha_comida(self, ficha, pos_destino):
        if self.__tablero__[pos_destino] == None:
            return False
        if len(self.__tablero__[pos_destino]) == 1 and self.__tablero__[pos_destino][0] != ficha: #comparo que sea solo una la ficha que se encuentra en esa posicion y que las fichas sean distintas
            oponente = self.__tablero__[pos_destino][0] 
            self.__tablero__[pos_destino] = [ficha] #agrego la ficha que comio a la posicion
            self.__banco__[oponente] += 1  #agrego la ficha comida al banc0
            return True
        if len(self.__tablero__[pos_destino]) >=2 :
            return False
        return False
        
    def devolver_ficha_comida(self, ficha, pos_destino):
        if self.__banco__[ficha] <= 0: #si en el banco no hay fichas, no se puede devolver ninguna ficha
            raise ValueError("No hay fichas en el banco")
        else:
            if self.__tablero__[pos_destino] == None:
                self.__tablero__[pos_destino] = [ficha] #si luego que ingreso al banco, quiere volver al tablero
                self.__banco__[ficha] -= 1 
            elif self.__tablero__[pos_destino][0] == ficha: 
                self.__tablero__[pos_destino].append(ficha)
                self.__banco__[ficha] -= 1 
            elif len(self.__tablero__[pos_destino]) == 1 and self.__tablero__[pos_destino][0] != ficha:
                oponente = self.__tablero__[pos_destino][0] #la ficha que se encuentra en esta posicion es la del "oponente" 
                self.__tablero__[pos_destino] = [ficha]        # reemplazamos la del oponente en dicha posicion por la nueva
                self.__banco__[ficha] -= 1                      # baja el banco de la ficha nueva
                self.__banco__[oponente] += 1                   # aumenta el banco del oponente
        
        
    def mover_ficha(self, pos_origen, pos_destino, ficha):
        self.validar_movimiento(pos_destino, pos_origen, ficha)
        if not self.ficha_comida(ficha, pos_destino):
            if self.__tablero__[pos_destino] is None : #Si la posicion de la ficha esta vacia y no se ha comido/no se puede comer ninguna ficha, agrego la ficha
                self.__tablero__[pos_destino] = [ficha]
            else:
                self.__tablero__[pos_destino].append(ficha) #si hay fichas, agrego otra a la lista
        self.__tablero__[pos_origen].pop() #Luego de cualquier movimiento, debo remover la ficha de la posicion
        if not self.__tablero__[pos_origen]: #Si la lista queda vacia, la pongo en None
            self.__tablero__[pos_origen] = None

    
    def sin_fichas(self, ficha):  #evaluamos si en el tablero no quedan mas fichas
        for casilla in self.__tablero__:
            if casilla is not None and ficha in casilla:
                return False
        return True
