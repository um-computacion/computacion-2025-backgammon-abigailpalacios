"""Modulo de excepciones personalizadas del juego."""


class BackgammonException(Exception):
    """Excepcion base para errores del juego."""


class MovimientoInvalido(BackgammonException):
    """Excepcion para movimientos no permitidos."""


class SinMovimientos(BackgammonException):
    """Excepcion cuando no hay movimientos disponibles."""


class GameOver(BackgammonException):
    """Excepcion cuando el juego ha terminado."""
