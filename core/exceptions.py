"""Modulo de excepciones personalizadas del juego."""


class BackgammonException(Exception):
    """Excepcion base para errores del juego."""


class MovimientoInvalido(BackgammonException):
    """Excepcion para movimientos no permitidos."""


class SinMovimientos(BackgammonException):
    """Excepcion cuando no hay movimientos disponibles."""


class JuegoTerminado(BackgammonException):
    """Excepcion cuando el juego ha terminado."""


class EntradaInvalida(BackgammonException):
    """Excepcion para entradas invalidas del usuario."""


class SacarFichaInvalido(BackgammonException):
    """Excepcion para intentos invalidos de sacar una ficha."""


class Rendicion(BackgammonException):
    """Excepcion para indicar que un jugador se ha rendido."""


class ReingresoInvalido(BackgammonException):
    """Excepcion para intentos invalidos de reingresar una ficha."""
