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

    try:
        while not Backgammongame.game_over(game):
            player = Backgammongame.get_turno(game)
            print(f"{'='*30}")
            print(f"Turno de {Player.get_nombre(player)} ({Player.get_ficha(player)})")
            dice = Backgammongame.tirar_dados(game)
            print(f"Dados: {Backgammongame.get_dados(game)}")


            if not game.movimientos_posibles():
                print("No hay movimientos posibles con los dados actuales")
                Backgammongame.definir_turno(game)
                continue

            while Backgammongame.dados_restantes(game):
                try:
                    Backgammongame.get_board(game).mostrar_tablero()
                    print(f"Turno de {Player.get_nombre(player)} ({Player.get_ficha(player)})")
                    print(f"Dados disponibles: {Backgammongame.get_dados(game)}")
                    print("1. Mover ficha")
                    print("2. Rendirse") 
                    print("3. Salir del juego")
                    
                    opcion = int(input("Ingrese una opcion: "))

                    if opcion == 1:
                        movimientos = game.movimientos_posibles()
                        if not movimientos:
                            print("No hay movimientos posibles con los dados actuales")
                            break
                        
                        print("Movimientos posibles:")
                        for origen, destinos in movimientos.items():
                            print(f" Desde posicion {origen + 1}: → {[d+1 if d != 'retirar' else 'SACAR' for d in destinos]}")
                        
                        origen = int(input("Mover ficha desde (1-24): ")) - 1

                        if origen < 0 or origen > 23:
                            print("Posición invalida. Debe estar entre 1 y 24")
                            continue
                            
                        if origen not in movimientos:
                            print("No hay movimientos posibles desde esa posicion")
                            continue

                        destinos_validos = movimientos[origen]
                        if "retirar" in destinos_validos:
                            accion = input("¿Desea mover a una posicion (M) o sacar ficha (S)? ").upper()
                            if accion == "S":
                                game.retirar_ficha(origen)
                                print(f"Ficha sacada desde posicion {origen + 1}")
                                continue
                        
                        destino = int(input("Hasta (1-24): ")) - 1
            
                        if destino < 0 or destino > 23:
                            print("Posicion invalida. Debe estar entre 1 y 24")
                            continue
                            
                        if destino not in destinos_validos:
                            destinos_mostrar = [d+1 for d in destinos_validos if d != 'retirar']
                            print(f"Destino invalido. Solo puede mover a: {destinos_mostrar}")
                            continue
                            
                        game.mover_ficha(origen, destino)
                        print(f"Ficha movida de {origen + 1} a {destino + 1}")
                    
                    elif opcion == 2:
                        print(f"{Player.get_nombre(player)} se ha rendido")
                        print("¡Gracias por jugar!")
                        return
                    
                    elif opcion == 3:
                        print("Juego finalizado por el usuario")
                        print("¡Hasta luego!")
                        return
                    
                    else:
                        print("Opcion invalida. Intente nuevamente.")
                        continue
                    
                    if Backgammongame.game_over(game):
                        print(f"¡El juego ha terminado!")
                        winner = game.get_ganador() if hasattr(game, 'get_ganador') else None
                        if winner:
                            print(f"Ganador: {Player.get_nombre(winner)} ({Player.get_ficha(winner)})")
                        return

                except MovimientoInvalido as e:
                    print(f"Movimiento invalido: {e}")
                except ValueError:
                    print("Entrada invalida.")
                except BackgammonException as e:
                    print(f"Error del juego: {e}")
            
            # Cambiar turno cuando se agoten los dados
            Backgammongame.definir_turno(game)
        
        print("¡Juego terminado!")
        
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    main()

