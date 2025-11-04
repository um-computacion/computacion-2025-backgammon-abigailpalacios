"""Interfaz de línea de comandos para el juego Backgammon."""

from core.backgammongame import Backgammongame
from core.exceptions import (
    BackgammonException, MovimientoInvalido, EntradaInvalida, SacarFichaInvalido,
    JuegoTerminado, Rendicion
)
from core.player import Player


def pedir_int(mensaje: str) -> int:
    """Solicita un número entero al usuario."""
    try:
        return int(input(mensaje))
    except ValueError as exc:
        raise EntradaInvalida("Debe ingresar un número entero") from exc


def main():
    """Bucle principal del juego."""
    print("Bienvenido al juego Backgammon\n")

    while True:
        try:
            nombre1 = input("Jugador 1 (Blancas): ")
            nombre2 = input("Jugador 2 (Negras): ")
            print("Inicializando el juego...")  # Mensaje de depuración
            juego = Backgammongame(nombre1, nombre2)
            print("Juego inicializado correctamente.")  # Mensaje de depuración
            break
        except BackgammonException as e:
            print(f"\nError: {e}\nIntente nuevamente.\n")
        except Exception as e:
            print(f"\nError inesperado: {e}\nIntente nuevamente.\n")  # Captura de errores inesperados

    while not juego.game_over():
        try:
            jugador = juego.get_turno()
            print(f"\nTurno de {jugador.get_nombre()} ({jugador.get_ficha()})")
            tirada = juego.tirar_dados()
            print(f"Tirada: {tirada}")  # Mensaje de depuración

            while juego.dados_restantes():
                try:
                    print(juego.mostrar_tablero())
                    print(f"Dados restantes: {juego.get_dados()}")
                    _manejar_opciones(juego, jugador)
                except (EntradaInvalida, MovimientoInvalido, SacarFichaInvalido) as e:
                    print(f"Error: {e}")
                except Rendicion:
                    print(f"\n{jugador.get_nombre()} se ha rendido")
                    return
                except JuegoTerminado:
                    print("\nJuego finalizado")
                    return
                except BackgammonException as e:
                    print(f"Error: {e}")
                except Exception as e:
                    print(f"Error inesperado: {e}")  # Captura de errores inesperados

            juego.definir_turno()

        except Exception as e:
            print(f"Error inesperado en el bucle principal: {e}")  # Captura de errores inesperados

    print("\nJuego terminado")


def _manejar_opciones(juego, jugador):
    """Maneja las opciones del jugador en su turno."""
    print("\nOpciones:\n1. Mover ficha\n2. Rendirse\n3. Salir")
    opcion = pedir_int("Seleccione una opcion: ")

    if opcion == 1:
        _manejar_movimiento(juego, jugador)
    elif opcion == 2:
        raise Rendicion
    elif opcion == 3:
        raise JuegoTerminado
    else:
        raise EntradaInvalida("Opcion no valida")


def _manejar_movimiento(juego, jugador):
    """Maneja el movimiento de fichas."""
    try:
        fichas_banco = juego.get_banco().get(jugador.get_ficha(), 0)
        if fichas_banco > 0:
            destino = pedir_int("Reingresar en posicion (1-24): ")
            dado = abs(destino - (1 if jugador.get_ficha() == "Blancas" else 24))
            if dado not in juego.get_dados():
                print(f"Error: El dado con valor {dado} no está disponible.")
                return
            juego.reingresar_ficha(dado)
            print(f"Ficha reingresada en {destino}")
        else:
            origen = pedir_int("Desde (1-24): ")
            destino = pedir_int("Hasta (1-24, -1=sacar): ")
            if destino == -1:
                juego.retirar_ficha(origen - 1)
                print(f"Ficha sacada desde {origen}")
            else:
                dado = abs(destino - origen)
                if dado not in juego.get_dados():
                    print(f"Error: El dado con valor {dado} no está disponible.")
                    return
                juego.mover_ficha(origen - 1, destino - 1)
                print(f"Movido de {origen} a {destino}")
    except Exception as e:
        print(f"Error inesperado al manejar movimiento: {e}")  # Captura de errores inesperados


if __name__ == "__main__":
    main()

