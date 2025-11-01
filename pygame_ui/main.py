"""Modulo principal de la interfaz grafica con pygame."""

import tkinter as tk

import pygame

from core.backgammongame import Backgammongame
from core.player import Player

from .events import EventHandler
from .iboard import TableroVisual


def get_player_input():
    """Obtiene los nombres de los jugadores mediante Tkinter."""

    def submit():
        nonlocal player1, player2
        player1 = entry1.get() or "Jugador 1"
        player2 = entry2.get() or "Jugador 2"
        root.quit()

    player1 = player2 = ""

    root = tk.Tk()
    root.title("Backgammon - Jugadores")
    root.geometry("300x200")
    root.configure(bg="tan")

    tk.Label(
        root, text="Configuración de Jugadores", font=("Times New Roman", 14, "bold"), bg="tan"
    ).pack(pady=10)

    tk.Label(root, text="Jugador 1:", font=("Times New Roman", 11, "italic"), bg="tan").pack()
    entry1 = tk.Entry(root, width=25)
    entry1.pack(pady=5)

    tk.Label(root, text="Jugador 2:", font=("Times New Roman", 11, "italic"), bg="tan").pack()
    entry2 = tk.Entry(root, width=25)
    entry2.pack(pady=5)

    tk.Button(
        root,
        text="Comenzar",
        command=submit,
        bg="green",
        fg="white",
        font=("Times New Roman", 10, "bold"),
    ).pack(pady=7)

    root.mainloop()
    root.destroy()

    return player1, player2


def main():
    """Funcion principal que inicializa y ejecuta el juego."""
    # Obtener nombres de jugadores
    player1_name, player2_name = get_player_input()

    if not player1_name or not player2_name:
        print("Juego cancelado.")
        return

    # Inicializar pygame
    pygame.init()
    pygame.font.init()

    # Crear jugadores y juego
    player1 = Player(player1_name, "Blancas")
    player2 = Player(player2_name, "Negras")
    juego = Backgammongame(player1, player2)

    # Configurar pantalla
    screen = pygame.display.set_mode((1400, 700))
    pygame.display.set_caption(f"Backgammon - {player1_name} vs {player2_name}")

    # Crear componentes
    vista_tablero = TableroVisual()
    event_handler = EventHandler(juego, vista_tablero)

    clock = pygame.time.Clock()

    # Loop principal del juego
    while event_handler.running:
        event_handler.handle_events()

        estado_juego = juego.estado_juego()
        handler_state = event_handler.get_state()

        screen.fill((0, 0, 0))
        vista_tablero.dibujar(
            screen,
            estado_juego,
            handler_state["origen_seleccionado"],
            handler_state["mensaje_ui"],
            handler_state["movimientos_posibles"],
        )

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()


if __name__ == "__main__":
    main()
