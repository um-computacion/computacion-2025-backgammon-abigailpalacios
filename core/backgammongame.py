from core.player import Player
from core.board import Board
from core.checker import Checker
from core.dice import Dice


class Backgammongame():
    def __init__(self, player1, player2):
        self.__player1__ = Player(player1, "Blancas")
        self.__player2__ = Player(player2, "Negras")
        self.__board__ = Board()
        self.__dice__ = Dice()
        self.__turno__ = self.__player1__
        self.__board__.inicializar()
        self.banco = self.__board__.banco()

    #Getters basicos

    def get_player1(self):
        return self.__player1__

    def get_player2(self):
        return self.__player2__

    def get_ficha(self):
        return self.__turno__.get_ficha() 

    def get_board(self):
        return self.__board__ 
    
    def get_banco(self):
        return self.banco

    def definir_turno(self):
        if self.__turno__ == self.__player1__:  #si el turno es del jugador 1, cambiamos al segundo jugador
            self.__turno__ = self.__player2__
        else:
            self.__turno__ = self.__player1__  #si el turno es del jugador 2, cambiamos al jugador 1
        self.__dice__ = Dice()     #inicializamos los dados para que el jugador que tiene el siguiente turno empieze con una lista nueva  

    def get_turno(self): 
            return self.__turno__

    def tirar_dados(self):
        self.__dice__.tirar()
        return self.__dice__.get_movimiento()
    
    def get_dados(self):
        return self.__dice__.get_movimiento()
    
    def dados_restantes(self):
        return list(self.__dice__.get_movimiento()) #Creamos una lista para guardar los movimientos disponibles del dado
    
    def usar_dados(self, valido):
        movimiento = self.__dice__.get_movimiento() #verificamos que el dado  tenga valores para poder mover las fichas       
        if valido in movimiento:                                
            movimiento.remove(valido)     #remueve el valor usado (por ejemplo, si tiro los dados y me devuelve 4,5 y uso el 4, no me deje volver a usar el 4)                      
        else:
            raise ValueError("Ese valor de dado no está disponible")
        
    def mover_ficha(self, pos_origen, pos_destino):
        ficha = self.get_ficha()
        pos_origen = int(pos_origen)
        pos_destino = int(pos_destino)
        if self.banco[ficha] > 0: #Si tengo fichas en el banco, no puedo mover las fichas
            raise ValueError("Retirar fichas en el banco antes de continuar")
        if self.dados_restantes() == []:  #Si no tengo movimientos del dado disponibles, no puedo mover
            raise ValueError("No tiene movimientos disponibles")
        if ficha == "Blancas":  #Si la ficha es blanca, su movimiento es de la posicion 1 a la 24
            pasos = pos_destino - pos_origen    
        else : #si la ficha es negra, su movimiento es de la posicion 24 a la 1
            pasos = pos_origen - pos_destino
            
        if pasos not in self.get_dados():
            raise ValueError("Ese valor de dado no está disponible") #Si la ficha no puede moverse esa cantidad de pasos, no se mueve
        
        self.__board__.validar_movimiento(pos_destino, pos_origen, ficha) #Validamos movimientos ya hechos en la clase tablero 
        self.__board__.mover_ficha(pos_origen, pos_destino, ficha) #Movemos la ficha en el tablero
        self.usar_dados(pasos) #Al usar el dado, removemos ese valos de la lista de movimientos disponibles
            
    def reingresar_ficha(self, dado):
        ficha = self.get_ficha()
        if dado not in self.get_dados():
                raise ValueError("Ese valor de dado no está disponible para reingresar")  #El movimiento no es valido para el jugador
        if ficha == "Blancas": 
                destino = dado - 1 #Si la ficha es blanca, entra de la posicion 1 al 6
        else: 
                destino = 24 - dado  #Si la ficha es negra, entra de la posicion 24 al 19
        self.__board__.devolver_ficha_comida(ficha, destino)
        self.usar_dados(dado)

    def ganador(self):
        if self.__board__.sin_fichas(self.__player1__.get_ficha()):  #para ganar, no debe de haber fichas en el tablero de dicho jugador
            return self.__player1__.get_nombre()
        elif self.__board__.sin_fichas(self.__player2__.get_ficha()):
            return self.__player2__.get_nombre()
        else:
            return None
        
    def posiciones_finales(self):
        ficha = self.get_ficha()
        tablero = self.__board__.mostrar_tablero()
        if ficha == "Blancas":
            for pos in range(0, 18):
                if tablero[pos] and ficha in tablero[pos]:
                    return False    #Si una ficha se encuentra en las posiciones [0, 17] de las fichas blancas, no se puede validar el sacar una ficha
            return True
        else:
            for pos in range(6, 24):
                if tablero[pos] and ficha in tablero[pos]:
                    return False     #Si una ficha se encuentra en las posiciones [6, 23] de las fichas negras, no se puede validar el sacar una ficha
            return True
        
    def retirar_ficha(self, pos_origen):
        ficha = self.get_ficha()
        tablero = self.__board__.mostrar_tablero()
        if self.banco[ficha] > 0: #Si tengo fichas en el banco, no puedo mover las fichas
            raise ValueError("Retirar fichas en el banco antes de continuar")
        if self.posiciones_finales() is False: # Si todas las fichas no se encuentran en las posiciones finales, no se pueden retirar fichas
            raise ValueError("Todas las fichas deben estar en el ultimo cuadrante para retirar")
        if self.dados_restantes() == []: #Si no hay dados para usar, no se puede mover
            raise ValueError("Movimiento de dado no disponible")
        if tablero[pos_origen] is None or ficha not in tablero[pos_origen]: #Si no se encuentra fichas en la posicion de origen o la ficha a mover no esta en la posicion, no se puede retirar
            raise ValueError("No hay fichas disponibles para retirar")
        if ficha == "Blancas":
            distancia = 24 - pos_origen
            distancia_lejana = range(pos_origen + 1, 24)
        else:
            distancia = pos_origen + 1
            distancia_lejana = range(0, pos_origen)
        dados = self.get_dados()
        if distancia == dados:
            tablero[pos_origen].remove(ficha)
            if not tablero[pos_origen]:
                tablero[pos_origen] = None
            self.usar_dados(distancia)
            return