"""Interfaz de linea de comandos para el juego Backgammon."""

from core.backgammongame import Backgammongame
from core.exceptions import BackgammonException, MovimientoInvalido
from core.player import Player


def imprimir_tablero(tablero_lista, banco):
    """Dibuja el estado del tablero en la consola de forma legible."""
    print("\n" + "=" * 52)
    print(" ESTADO DEL TABLERO ".center(52, "="))
    print("=" * 52)
    print(" 13 14 15 16 17 18   ||   19 20 21 22 23 24 (Indices: 12-23)")
    print("----------------------------------------------------")
    linea_superior = ""
    for i in range(12, 24):
        if i == 18:
            linea_superior += "  ||  "

        casilla = tablero_lista[i]
        if casilla is None:
            linea_superior += " .  "
        elif casilla[0] == "Blancas":
            linea_superior += f" B{len(casilla):<1} "  # B1, B2, etc.
        else:
            linea_superior += f" N{len(casilla):<1} "  # N1, N2, etc.
    print(linea_superior)

    print("\n" + "=" * 19 + " BARRA / BANCO " + "=" * 19)
    blancas_banco = banco.get("Blancas", 0)
    negras_banco = banco.get("Negras", 0)
    print(f" Blancas [Comidas]: {blancas_banco} | Negras [Comidas]: {negras_banco}")
    print("=" * 52 + "\n")
    
    linea_inferior = ""
    for i in range(11, -1, -1):
        if i == 5:
            linea_inferior += "  ||  "

        casilla = tablero_lista[i]
        if casilla is None:
            linea_inferior += " .  "
        elif casilla[0] == "Blancas":
            linea_inferior += f" B{len(casilla):<1} "
        else:
            linea_inferior += f" N{len(casilla):<1} "
    print(linea_inferior)
    print("----------------------------------------------------")
    print(" 12 11 10  9  8  7   ||    6  5  4  3  2  1 (Indices: 11-0)")
    print("=" * 52 + "\n")


def main():
    """Funcion principal que ejecuta el juego en CLI."""
    print("=" * 50)
    print("Bienvenido al juego 'Backgammons'!")
    print("=" * 50)

    name_player1 = input("Ingrese nombre del Jugador 1: ")
    name_player2 = input("Ingrese nombre del Jugador 2: ")
    player1 = Player(name_player1, "Blancas")
    player2 = Player(name_player2, "Negras")
    game = Backgammongame(player1, player2)

    try:
        while not game.game_over():
            player = game.get_turno()
            print(f"{'='*30}")
            print(f"Turno de {player.get_nombre()} ({player.get_ficha()})")
            _ = game.tirar_dados()
            print(f"Dados: {game.get_dados()}")
            imprimir_tablero(game.get_board().mostrar_tablero(), game.get_banco())

            if not game.movimientos_posibles():
                print("No hay movimientos posibles con los dados actuales")
                game.definir_turno()
                continue

            while game.dados_restantes():
                try:
                    print(f"Turno de {player.get_nombre()} ({player.get_ficha()})")
                    print(f"Dados disponibles: {game.get_dados()}")
                    print("1. Mover ficha")
                    print("2. Rendirse")
                    print("3. Salir del juego")

                    opcion = int(input("Ingrese una opcion: "))

                    if opcion == 1:
                        movimientos = game.movimientos_posibles()
                        if not movimientos:
                            print("No hay movimientos posibles")
                            break

                        print("Movimientos posibles:")
                        for origen, destinos in movimientos.items():
                            destinos_formateados = [
                                d + 1 if d != "retirar" else "SACAR" for d in destinos
                            ]
                            print(f" Desde posicion {origen + 1}: → {destinos_formateados}")
                        
                        origen = int(input("Mover ficha desde (1-24): ")) - 1

                        if origen < 0 or origen > 23:
                            print("Posicion invalida. Debe estar entre 1 y 24")
                            continue

                        if origen not in movimientos:
                            print("No hay movimientos posibles desde esa posicion")
                            continue

                        destinos_validos = movimientos[origen]
                        if "retirar" in destinos_validos:
                            accion = input(
                                "¿Desea mover a una posicion (M) o sacar ficha (S)? "
                            ).upper()
                            if accion == "S":
                                game.retirar_ficha(origen)
                                print(f"Ficha sacada desde posicion {origen + 1}")
                                imprimir_tablero(
                                    game.get_board().mostrar_tablero(), game.get_banco()
                                )
                                continue

                        destino = int(input("Hasta (1-24): ")) - 1

                        if destino < 0 or destino > 23:
                            print("Posicion invalida. Debe estar entre 1 y 24")
                            continue

                        if destino not in destinos_validos:
                            destinos_mostrar = [
                                d + 1 for d in destinos_validos if d != "retirar"
                            ]
                            print(f"Destino invalido. Solo puede mover a: {destinos_mostrar}")
                            continue

                        game.mover_ficha(origen, destino)
                        print(f"Ficha movida de {origen + 1} a {destino + 1}")

                        imprimir_tablero(game.get_board().mostrar_tablero(), game.get_banco())

                    elif opcion == 2:
                        print(f"{player.get_nombre()} se ha rendido")
                        print("¡Gracias por jugar!")
                        return

                    elif opcion == 3:
                        print("Juego finalizado por el usuario")
                        print("¡Hasta luego!")
                        return

                    else:
                        print("Opcion invalida. Intente nuevamente.")
                        continue

                    if game.game_over():
                        print("¡El juego ha terminado!")
                        winner = game.ganador()
                        if winner:
                            print(f"Ganador: {winner}")
                        return

                except MovimientoInvalido as e:
                    print(f"Movimiento invalido: {e}")
                except ValueError:
                    print("Entrada invalida.")
                except BackgammonException as e:
                    print(f"Error del juego: {e}")

            game.definir_turno()

        print("¡Juego terminado!")

    except Exception as e:
        print(f"Error inesperado: {e}")


if __name__ == "__main__":
    main()
