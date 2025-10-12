from core.backgammongame import Backgammongame
from core.player import Player
from core.board import Board
from core.dice import Dice
from core.exceptions import BackgammonException, MovimientoInvalido, SinMovimientos, GameOver

def main():
    
    print("=" * 50)
    print("Bienvenido al juego 'Backgammon'!")
    print("=" * 50)

    name_player1 = input("Ingrese nombre del Jugador 1: ")
    name_player2 = input("Ingrese nombre del Jugador 2: ")
    player1 = Player(name_player1, "Blancas")
    player2 = Player(name_player2, "Negras")
    game = Backgammongame(player1, player2)

    board = Backgammongame.get_board(game)

    while not Backgammongame.game_over(game):
        player = Backgammongame.get_turno(game)
        print(f"{'='*30}")
        print(f"Turno de {Player.get_nombre(player)} ({Player.get_ficha(player)})")
        dice = Backgammongame.tirar_dados(game)
        print(f"Dados: {Backgammongame.get_dados(game)}")

        while Backgammongame.dados_restantes(game):
            try:
                Backgammongame.get_board(game).mostrar_tablero()
                print("Seleccione una opcion: ")
                print("1. Mover ficha")
                print("2. Pasar turno (si no hay movimientos posibles)")
                print("3. Salir del juego")
                opcion = int(input("Ingrese su opción: "))

                if opcion == 1:
                    if not game.movimientos_posibles():
                        print("No hay movimientos posibles con los dados actuales")
                        continue
                    
                    print("Movimientos posibles:")
                    for origen, destinos in game.movimientos_posibles().items():
                        print(f"Desde posición {origen + 1}: puede ir a {[d+1 if d != 'retirar' else 'RETIRAR' for d in destinos]}")
                    
                    try:
                        origen = int(input("Ingrese la posición de origen (1-24): ")) - 1  # Convertir a índice 0-23
                        if origen not in game.movimientos_posibles():
                            print("No hay movimientos posibles desde esa posición")
                            continue

                        print(f"Destinos válidos desde posición {origen + 1}: {[d+1 if d != 'retirar' else 'RETIRAR' for d in game.movimientos_posibles()[origen]]}")

                        if "retirar" in game.movimientos_posibles()[origen]:
                            accion = input("¿Desea mover a una posición (M) o retirar la ficha (R)? ").upper()
                            if accion == "R":
                                game.retirar_ficha(origen)
                                print("Ficha retirada exitosamente!")
                                continue
                        
                        destino = int(input("Ingrese la posición de destino (1-24): ")) - 1  # Convertir a índice 0-23
                        
                        # Validar que el destino esté en los movimientos posibles
                        if destino not in game.movimientos_posibles()[origen]:
                            print(f"Destino inválido. Solo puede mover a: {[d+1 for d in game.movimientos_posibles()[origen] if d != 'retirar']}")
                            continue
                            
                        game.mover_ficha(origen, destino)
                        print("Movimiento realizado exitosamente!")
                        
                    except MovimientoInvalido as e:
                        print(f"Movimiento inválido: {e}")
                    
                    except ValueError as e:
                        print(f"Entrada inválida: {e}")
                    
                    except BackgammonException as e:
                        print(f"Error del juego: {e}")
                
                elif opcion == 2:
                    print("Pasando turno...")
                    Backgammongame.definir_turno(game)
                    break
                
                elif opcion == 3:
                    print("Saliendo del juego. ¡Hasta luego!")
                    return
                
                else:
                    print("Opción inválida. Intente nuevamente.")

            except SinMovimientos:
                print("No hay movimientos disponibles con los dados actuales")
                Backgammongame.definir_turno(game)
                break
            
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número.")
            
            except BackgammonException as e:
                print(f"Error del juego: {e}")
                break
            
            except ValueError:
                print("Entrada inválida. Por favor ingrese un número.")
            
            except BackgammonException as e:
                print(f"Error del juego: {e}")

