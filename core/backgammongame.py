"""Modulo principal del juego de Backgammon."""

from core.board import Board
from core.dice import Dice
from core.player import Player


class Backgammongame:
    """Clase que orquesta el juego completo de Backgammon."""

    def __init__(self, player1, player2):
        """Inicializa el juego con dos jugadores."""
        self.__player1__ = Player(player1, "Blancas")
        self.__player2__ = Player(player2, "Negras")
        self.__board__ = Board()
        self.__dice__ = Dice()
        self.__turno__ = self.__player1__
        self.__board__.inicializar()
        self.banco = self.__board__.banco()

    # Getters basicos

    def get_player1(self):
        """Retorna el jugador 1."""
        return self.__player1__

    def get_player2(self):
        """Retorna el jugador 2."""
        return self.__player2__

    def get_ficha(self):
        """Retorna el color de ficha del jugador actual."""
        return self.__turno__.get_ficha()

    def get_board(self):
        """Retorna el tablero del juego."""
        return self.__board__

    def get_banco(self):
        """Retorna el banco de fichas comidas."""
        return self.banco

    def definir_turno(self):
        """Cambia el turno al siguiente jugador."""
        if (
            self.__turno__ == self.__player1__
        ):  # si el turno es del jugador 1, cambiamos al segundo jugador
            self.__turno__ = self.__player2__
        else:
            self.__turno__ = (
                self.__player1__
            )  # si el turno es del jugador 2, cambiamos al jugador 1
        self.__dice__ = (
            Dice()
        )  # inicializamos los dados para que el jugador que tiene el siguiente turno empieze con una lista nueva

    def get_turno(self):
        """Retorna el jugador que tiene el turno actual."""
        return self.__turno__

    def tirar_dados(self):
        """Tira los dados y retorna los valores."""
        self.__dice__.tirar()
        return self.__dice__.get_movimiento()

    def get_dados(self):
        """Retorna los valores actuales de los dados."""
        return self.__dice__.get_movimiento()

    def dados_restantes(self):
        """Retorna lista de movimientos de dados disponibles."""
        return list(
            self.__dice__.get_movimiento()
        )  # Creamos una lista para guardar los movimientos disponibles del dado

    def usar_dados(self, valido):
        """Marca un dado como usado."""
        movimiento = (
            self.__dice__.get_movimiento()
        )  # verificamos que el dado  tenga valores para poder mover las fichas
        if valido in movimiento:
            movimiento.remove(
                valido
            )  # remueve el valor usado (por ejemplo, si tiro los dados y me devuelve 4,5 y uso el 4, no me deje volver a usar el 4)
        else:
            raise ValueError("Ese valor de dado no está disponible")

    def mover_ficha(self, origen, destino):
        """Mueve una ficha de origen a destino."""
        ficha = self.get_ficha()
        origen = int(origen)
        destino = int(destino)
        if self.banco[ficha] > 0:  # Si tengo fichas en el banco, no puedo mover las fichas
            raise ValueError("Retirar fichas en el banco antes de continuar")
        if not self.dados_restantes():  # Si no tengo movimientos del dado disponibles, no puedo mover
            raise ValueError("No tiene movimientos disponibles")
        if ficha == "Blancas":  # Si la ficha es blanca, su movimiento es de la posicion 1 a la 24
            pasos = destino - origen
        else:  # si la ficha es negra, su movimiento es de la posicion 24 a la 1
            pasos = origen - destino

        if pasos not in self.get_dados():
            raise ValueError(
                "Ese valor de dado no está disponible"
            )  # Si la ficha no puede moverse esa cantidad de pasos, no se mueve

        self.__board__.validar_movimiento(
            destino, origen, ficha
        )  # Validamos movimientos ya hechos en la clase tablero
        self.__board__.mover_ficha(origen, destino, ficha)  # Movemos la ficha en el tablero
        self.usar_dados(
            pasos
        )  # Al usar el dado, removemos ese valos de la lista de movimientos disponibles

    def reingresar_ficha(self, dado):
        """Reingresa una ficha del banco al tablero."""
        ficha = self.get_ficha()
        if dado not in self.get_dados():
            raise ValueError(
                "Ese valor de dado no está disponible para reingresar"
            )  # El movimiento no es valido para el jugador
        if ficha == "Blancas":
            destino = dado - 1  # Si la ficha es blanca, entra de la posicion 1 al 6
        else:
            destino = 24 - dado  # Si la ficha es negra, entra de la posicion 24 al 19
        self.__board__.devolver_ficha_comida(ficha, destino)
        self.usar_dados(dado)

    def ganador(self):
        """Verifica si hay un ganador y lo retorna."""
        if self.__board__.sin_fichas(self.__player1__.get_ficha()):
            return self.__player1__.get_nombre()
        if self.__board__.sin_fichas(self.__player2__.get_ficha()):
            return self.__player2__.get_nombre()
        return None

    def posiciones_finales(self):
        """Verifica si todas las fichas estan en el cuadrante final."""
        ficha = self.get_ficha()
        tablero = self.__board__.mostrar_tablero()
        if ficha == "Blancas":
            for pos in range(0, 18):
                if tablero[pos] and ficha in tablero[pos]:
                    return False  # Si una ficha se encuentra en las posiciones [0, 17] de las fichas blancas, no se puede validar el sacar una ficha
            return True

        for pos in range(6, 24):
            if tablero[pos] and ficha in tablero[pos]:
                return False  # Si una ficha se encuentra en las posiciones [6, 23] de las fichas negras, no se puede validar el sacar una ficha
        return True

    def retirar_ficha(self, pos_origen):
        """Retira una ficha del tablero."""
        ficha = self.get_ficha()
        tablero = self.__board__.mostrar_tablero()
        dados = self.get_dados()

        if self.banco[ficha] > 0:
            raise ValueError("Retirar fichas en el banco antes de continuar")

        if self.posiciones_finales() is False:
            raise ValueError("Todas las fichas deben estar en el ultimo cuadrante para retirar")

        if not dados:
            raise ValueError("Movimiento de dado no disponible")

        if tablero[pos_origen] is None or ficha not in tablero[pos_origen]:
            raise ValueError("No hay fichas disponibles para retirar")

        # Calcular la distancia necesaria para sacar la ficha
        if ficha == "Blancas":
            # Blancas sacan desde posiciones 18-23 (necesitan llegar a 24)
            distancia = 24 - pos_origen
            posiciones_mas_lejanas = range(18, pos_origen)
        else:
            # Negras sacan desde posiciones 0-5 (necesitan llegar a -1)
            distancia = pos_origen + 1
            posiciones_mas_lejanas = range(pos_origen + 1, 6)

        # Caso 1: Si el dado coincide exactamente con la distancia
        if distancia in dados:
            tablero[pos_origen].pop()
            self.usar_dados(distancia)
            if not tablero[pos_origen]:
                tablero[pos_origen] = None
            return

        # Caso 2: Usar un dado mayor si no hay fichas más lejanas
        # Verificar si hay fichaas mas lejanas
        hay_fichas_mas_lejanas = any(
            tablero[i] and ficha in tablero[i] for i in posiciones_mas_lejanas
        )

        if hay_fichas_mas_lejanas:
            raise ValueError("No se puede retirar: hay fichas más lejanas")

        # Buscar el primer dado mayor a la distancia
        dado_usado = None
        for d in sorted(dados):  # Ordenar para usar el menor posible
            if d > distancia:
                dado_usado = d
                break

        if dado_usado is None:
            raise ValueError("El dado no permite retirar esta ficha")

        # Retirar la ficha usando el dado mayor
        tablero[pos_origen].pop()
        self.usar_dados(dado_usado)
        if not tablero[pos_origen]:
            tablero[pos_origen] = None

    def movimientos_posibles(self):
        """Calcula todos los movimientos posibles para el turno actual."""
        ficha = self.get_ficha()
        tablero = self.__board__.mostrar_tablero()
        dados = self.get_dados()
        movimientos = {}

        if self.banco[ficha] > 0 or not dados:
            return movimientos

        for origen in range(24):
            if tablero[origen] and ficha in tablero[origen]:
                destinos = self._calcular_destinos(origen, ficha, dados, tablero)
                if destinos:
                    movimientos[origen] = destinos
        return movimientos

    def _calcular_destinos(self, origen, ficha, dados, tablero):
        """Calcula los destinos posibles para una ficha desde una posición."""
        destinos = []
        for dado in dados:
            destino = origen + dado if ficha == "Blancas" else origen - dado
            if self._es_movimiento_valido(destino, origen, ficha, tablero):
                destinos.append(destino)
            elif self._puede_retirar(destino, origen, ficha, tablero):
                destinos.append("retirar")
        return destinos

    def _es_movimiento_valido(self, destino, origen, ficha, tablero):
        """Verifica si un movimiento es válido."""
        if 0 <= destino <= 23:
            try:
                self.__board__.validar_movimiento(destino, origen, ficha)
                return True
            except ValueError:
                return False
        return False

    def _puede_retirar(self, destino, origen, ficha, tablero):
        """Verifica si una ficha puede ser retirada."""
        if ficha == "Blancas" and destino > 23 and self.posiciones_finales():
            return all(
                not tablero[pos] or ficha not in tablero[pos]
                for pos in range(origen + 1, 24)
            )
        if ficha == "Negras" and destino < 0 and self.posiciones_finales():
            return all(
                not tablero[pos] or ficha not in tablero[pos]
                for pos in range(0, origen)
            )
        return False

    def reingreso_posible(self):
        """Calcula las posiciones validas para reingresar desde el banco."""
        ficha = self.get_ficha()
        tablero = self.__board__.mostrar_tablero()
        dados = self.get_dados()
        reingresar = {}
        if (
            self.banco[ficha] == 0
        ):  # Si no hay fichas en el banco no se realiza ningun movimiento correspondiente al banco
            return reingresar
        if not dados:  # si no tiene movimientos con el dado, el diccionario queda vacio
            return reingresar
        des_pos = []

        for dado in dados:
            if ficha == "Blancas":
                destino = dado - 1
            else:
                destino = 24 - dado

            if tablero[destino] is None:
                des_pos.append(destino)
            elif tablero[destino] and tablero[destino][0] == ficha:
                des_pos.append(destino)
            elif tablero[destino] and len(tablero[destino]) == 1 and tablero[destino][0] != ficha:
                des_pos.append(destino)
        if des_pos:
            reingresar["reingresa"] = des_pos

        return reingresar

    def estado_juego(self):
        """Retorna un diccionario con el estado completo del juego."""
        if self.ganador():
            estado = "ganado"

        elif self.banco[self.get_ficha()] > 0:
            estado = "reingreso"

        else:
            estado = "en curso"

        return {
            "estado": estado,
            "turno": self.get_turno().get_nombre(),
            "jugador 1": self.get_player1().get_nombre(),
            "jugador 2": self.get_player2().get_nombre(),
            "ficha actual": self.get_ficha(),
            "dados": self.get_dados(),
            "tablero": self.get_board().mostrar_tablero(),
            "banco": self.get_banco(),
            "movimientos posibles": self.movimientos_posibles(),
            "reingreso posible": self.reingreso_posible(),
            "ganador": self.ganador(),
        }

    def mov_posible(self):
        """Verifica si hay movimientos posibles."""
        ficha = self.get_ficha()
        if self.banco[ficha] > 0:
            return bool(self.reingreso_posible())
        return bool(self.movimientos_posibles())

    def turno_completo(self):
        """Verifica si el turno actual esta completo."""
        if not self.get_dados() or not self.mov_posible():
            return True
        return False

    def game_over(self):
        """Verifica si el juego ha terminado."""
        return self.ganador() is not None

    def mostrar_tablero(self):
        """Muestra el tablero de forma visual."""
        tablero = self.__board__.mostrar_tablero()
        banco = self.banco

        resultado = "\n" + "=" * 50 + "\n"
        resultado += " 13 14 15 16 17 18 || 19 20 21 22 23 24\n"
        resultado += "-" * 50 + "\n"

        linea_sup = ""
        for i in range(12, 24):
            if i == 18:
                linea_sup += " || "
            if tablero[i] is None:
                linea_sup += " .  "
            elif tablero[i][0] == "Blancas":
                linea_sup += f" B{len(tablero[i])} "
            else:
                linea_sup += f" N{len(tablero[i])} "
        resultado += linea_sup + "\n"

        resultado += f"\nBANCO: Blancas[{banco.get('Blancas', 0)}] Negras[{banco.get('Negras', 0)}]\n\n"

        linea_inf = ""
        for i in range(11, -1, -1):
            if i == 5:
                linea_inf += " || "
            if tablero[i] is None:
                linea_inf += " .  "
            elif tablero[i][0] == "Blancas":
                linea_inf += f" B{len(tablero[i])} "
            else:
                linea_inf += f" N{len(tablero[i])} "
        resultado += linea_inf + "\n"

        resultado += "-" * 50 + "\n"
        resultado += " 12 11 10  9  8  7 ||  6  5  4  3  2  1\n"
        resultado += "=" * 50 + "\n"

        return resultado