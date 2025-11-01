"""Modulo que gestiona el tablero de Backgammon."""


class Board:
    """Clase que representa el tablero del juego."""

    def __init__(self):
        """Inicializa el tablero vacio."""
        self.__tablero__ = [None] * 24
        self.__banco__ = {"Blancas": 0, "Negras": 0}

    def inicializar(self):
        """Coloca las fichas en sus posiciones iniciales."""
        self.__tablero__[0] = ["Blancas"] * 2
        self.__tablero__[11] = ["Blancas"] * 5
        self.__tablero__[16] = ["Blancas"] * 3
        self.__tablero__[18] = ["Blancas"] * 5

        self.__tablero__[5] = ["Negras"] * 5
        self.__tablero__[7] = ["Negras"] * 3
        self.__tablero__[12] = ["Negras"] * 5
        self.__tablero__[23] = ["Negras"] * 2

    def banco(self):
        """Inicializa el banco para fichas comidas."""
        return self.__banco__

    def mostrar_tablero(self):
        """Retorna el estado actual del tablero."""
        return self.__tablero__

    def validar_movimiento(self, pos_destino, pos_origen, ficha):
        """Valida si un movimiento es permitido."""
        pos_origen = int(pos_origen)
        pos_destino = int(pos_destino)
        if pos_destino < 0 or pos_destino > 23 or pos_origen < 0 or pos_origen > 23:
            raise ValueError("Posicion de destino invalida")
        if not self.__tablero__[pos_origen]:
            raise ValueError("No hay fichas en el lugar de origen")
        if ficha == "Blancas" and pos_destino <= pos_origen:
            raise ValueError("Movimiento invalido para fichas blancas")
        if ficha == "Negras" and pos_destino >= pos_origen:
            raise ValueError("Movimiento invalido para fichas negras")
        if (
            self.__tablero__[pos_destino] is not None
            and len(self.__tablero__[pos_destino]) >= 2
            and self.__tablero__[pos_destino][0] != ficha
        ):
            raise ValueError("Movimiento invalido, posicion ocupada por oponente")

    def ficha_comida(self, ficha, pos_destino):
        """Verifica y ejecuta la captura de una ficha."""
        if self.__tablero__[pos_destino] is None:
            return False
        if (
            len(self.__tablero__[pos_destino]) == 1
            and self.__tablero__[pos_destino][0] != ficha
        ):
            oponente = self.__tablero__[pos_destino][0]
            self.__tablero__[pos_destino] = [ficha]
            self.__banco__[oponente] += 1
            return True
        if len(self.__tablero__[pos_destino]) >= 2:
            return False
        return False

    def devolver_ficha_comida(self, ficha, pos_destino):
        """Reingresa una ficha del banco al tablero."""
        if self.__banco__[ficha] <= 0:
            raise ValueError("No hay fichas en el banco")
        
        if self.__tablero__[pos_destino] is None:
            self.__tablero__[pos_destino] = [ficha]
            self.__banco__[ficha] -= 1
        elif self.__tablero__[pos_destino][0] == ficha:
            self.__tablero__[pos_destino].append(ficha)
            self.__banco__[ficha] -= 1
        elif (
            len(self.__tablero__[pos_destino]) == 1
            and self.__tablero__[pos_destino][0] != ficha
        ):
            oponente = self.__tablero__[pos_destino][0]
            self.__tablero__[pos_destino] = [ficha]
            self.__banco__[ficha] -= 1
            self.__banco__[oponente] += 1

    def mover_ficha(self, pos_origen, pos_destino, ficha):
        """Ejecuta el movimiento de una ficha."""
        self.validar_movimiento(pos_destino, pos_origen, ficha)
        if not self.ficha_comida(ficha, pos_destino):
            if self.__tablero__[pos_destino] is None:
                self.__tablero__[pos_destino] = [ficha]
            else:
                self.__tablero__[pos_destino].append(ficha)
        self.__tablero__[pos_origen].pop()
        if not self.__tablero__[pos_origen]:
            self.__tablero__[pos_origen] = None

    def sin_fichas(self, ficha):
        """Verifica si no quedan fichas de un color en el tablero."""
        for casilla in self.__tablero__:
            if casilla is not None and ficha in casilla:
                return False
        return True
