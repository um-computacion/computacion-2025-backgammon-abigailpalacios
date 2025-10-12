from core.backgammongame import Backgammongame
from core.player import Player
from core.board import Board
from core.dice import Dice  

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
                    origen = int(input("Ingrese la posición de origen (1-24): "))
                    destino = int(input("Ingrese la posición de destino (1-24): "))
                    Backgammongame.mover_ficha(game, origen, destino)
                    
