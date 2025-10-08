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
        print(f"\n{'='*30}")
        print(f"Turno de {Player.get_nombre(player)} ({Player.get_ficha(player)})")
        dice = Backgammongame.tirar_dados(game)
        print(f"Dados: {Backgammongame.get_dados(game)}")
