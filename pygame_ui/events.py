"""Modulo que maneja los eventos de la interfaz grafica."""

import pygame

from core.exceptions import BackgammonException, MovimientoInvalido


class EventHandler:
    """Clase que procesa todos los eventos del juego en pygame."""

    def __init__(self, juego, vista_tablero):
        """Inicializa el manejador de eventos."""
        self.juego = juego
        self.vista_tablero = vista_tablero
        self.dados_tirados = False
        self.origen_seleccionado = None
        self.movimientos_posibles = {}
        self.mensaje_ui = "¡Bienvenido! Tira los dados para comenzar."
        self.running = True

    def handle_events(self):
        """Procesa todos los eventos de pygame."""
        estado_juego = self.juego.estado_juego()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self._handle_mouse_click(event.pos, estado_juego)

        # Verificar fin de turno
        if self.dados_tirados and self.juego.turno_completo() and not estado_juego["ganador"]:
            self.juego.definir_turno()
            self.dados_tirados = False
            self.origen_seleccionado = None
            self.movimientos_posibles = {}
            self.mensaje_ui = f"Turno de {self.juego.get_turno().get_nombre()}. ¡Tira los dados!"

    def _handle_mouse_click(self, pos_clic, estado_juego):
        """Maneja los clics del mouse."""
        self.mensaje_ui = ""

        # Clic en botón de dados
        if self.vista_tablero.rect_boton_dados.collidepoint(pos_clic):
            self._handle_dice_button(estado_juego)

        # Clic en el tablero para mover fichas
        elif self.dados_tirados and not estado_juego["ganador"]:
            self._handle_board_click(pos_clic, estado_juego)

    def _handle_dice_button(self, estado_juego):
        """Maneja el clic en el boton de tirar dados."""
        if not self.dados_tirados and not estado_juego["ganador"]:
            try:
                self.juego.tirar_dados()
                self.dados_tirados = True
                if not self.juego.mov_posible():
                    self.mensaje_ui = "No hay movimientos. Pasa el turno."
                else:
                    self.mensaje_ui = f"Mueve {estado_juego['ficha actual']}"
            except Exception as e:
                self.mensaje_ui = f"Error: {e}"
        elif estado_juego["ganador"]:
            self.mensaje_ui = f"Juego terminado. Ganador: {estado_juego['ganador']}"
        else:
            self.mensaje_ui = "Ya tiraste. Pasa el turno cuando termines."

        self.origen_seleccionado = None
        self.movimientos_posibles = {}

    def _handle_board_click(self, pos_clic, estado_juego):
        """Maneja el clic en el tablero."""
        pos_logica = self.vista_tablero.convertir_clic_a_posicion(pos_clic)

        if pos_logica is None:
            self.origen_seleccionado = None
            self.movimientos_posibles = {}
            self.mensaje_ui = "Clic fuera del tablero."
            return

        if self.origen_seleccionado is None:
            self._handle_select_origin(pos_logica, estado_juego)
        else:
            self._handle_move_to_destination(pos_logica, estado_juego)

    def _handle_select_origin(self, pos_logica, estado_juego):
        """Maneja la seleccion del origen del movimiento."""
        if pos_logica == "banco" and estado_juego["estado"] == "reingreso":
            self.origen_seleccionado = "banco"
            self.movimientos_posibles = self.juego.reingreso_posible()
            self.mensaje_ui = "Banco seleccionado. Elige destino."

        elif pos_logica == "retiro":
            self.mensaje_ui = "Esta es la zona para sacar fichas."

        elif isinstance(pos_logica, int):
            if (
                estado_juego["tablero"][pos_logica]
                and estado_juego["tablero"][pos_logica][0] == estado_juego["ficha actual"]
            ):
                self.origen_seleccionado = pos_logica
                todos_movimientos = self.juego.movimientos_posibles()
                self.movimientos_posibles = {pos_logica: todos_movimientos.get(pos_logica, [])}
                self.mensaje_ui = f"Posición {pos_logica+1} seleccionada. Elige destino."
            else:
                self.mensaje_ui = "No hay fichas tuyas en esa posición."

    def _handle_move_to_destination(self, destino, estado_juego):
        """Maneja el movimiento a la posicion de destino."""
        try:
            if self.origen_seleccionado == "banco":
                self._handle_reingreso(destino, estado_juego)

            elif destino == "retiro":
                self._handle_retiro()

            elif isinstance(destino, int) and isinstance(self.origen_seleccionado, int):
                self.juego.mover_ficha(self.origen_seleccionado, destino)
                self.mensaje_ui = f"Movido de {self.origen_seleccionado+1} a {destino+1}"

            else:
                raise MovimientoInvalido("Movimiento no reconocido")

        except (BackgammonException, ValueError) as e:
            self.mensaje_ui = f"Error: {e}"

        self.origen_seleccionado = None
        self.movimientos_posibles = {}

    def _handle_reingreso(self, destino, estado_juego):
        """Maneja el reingreso de fichas desde el banco."""
        if isinstance(destino, int):
            ficha = estado_juego["ficha actual"]
            dado_necesario = -1
            if ficha == "Blancas":
                dado_necesario = destino + 1
            else:
                dado_necesario = 24 - destino

            self.juego.reingresar_ficha(dado_necesario)
            self.mensaje_ui = f"Ficha reingresada en {destino+1}"
        else:
            raise MovimientoInvalido("Destino inválido para reingresar")

    def _handle_retiro(self):
        """Maneja el retiro de fichas del tablero."""
        if isinstance(self.origen_seleccionado, int):
            self.juego.retirar_ficha(self.origen_seleccionado)
            self.mensaje_ui = f"Ficha retirada desde {self.origen_seleccionado+1}"
        else:
            raise MovimientoInvalido("Origen inválido para retirar")

    def get_state(self):
        """Retorna el estado actual del manejador de eventos."""
        return {
            "origen_seleccionado": self.origen_seleccionado,
            "movimientos_posibles": self.movimientos_posibles,
            "mensaje_ui": self.mensaje_ui,
            "running": self.running,
        }
