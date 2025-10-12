class BackgammonException(Exception):
    """Excepción base para el juego de Backgammon"""
    pass

class MovimientoInvalido(BackgammonException):
    """Se lanza cuando se intenta realizar un movimiento inválido"""
    pass

class SinMovimientos(BackgammonException):
    """Se lanza cuando no hay movimientos disponibles"""
    pass

class GameOver(BackgammonException):
    """Se lanza cuando el juego ha terminado"""
    pass
