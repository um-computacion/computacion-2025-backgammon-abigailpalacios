from logging import root
import pygame
import tkinter as tk
from tkinter import simpledialog
from board import Tablero

def get_player_input():
    def submit():
        nonlocal player1, player2
        player1 = entry1.get() or "Jugador 1" #valor por defecto
        player2 = entry2.get() or "Jugador 2"
        root.quit()
    
    player1 = player2 = ""
    
    root = tk.Tk()
    root.title("Backgammon - Jugadores") #titulo de la ventana
    root.geometry("300x200") #tamaño de la ventana
    root.configure(bg='tan') #color de fondo
    
    tk.Label(root, text="Configuración de Jugadores",  #titulo
             font=("Times New Roman", 14, "bold"), bg='tan').pack(pady=10)

    tk.Label(root, text="Jugador 1:", font=("Times New Roman", 11, "italic"), bg='tan').pack() #etiqueta del jugador 1
    entry1 = tk.Entry(root, width=25)
    entry1.pack(pady=5)

    tk.Label(root, text="Jugador 2:", font=("Times New Roman", 11, "italic"), bg='tan').pack() #etiqueta del jugador 2
    entry2 = tk.Entry(root, width=25)
    entry2.pack(pady=5)
    
    tk.Button(root, text="Comenzar", command=submit,  #boton para comenzar el juego
             bg='green', fg='white', font=("Times New Roman", 10, "bold")).pack(pady=7)
    
    root.mainloop()
    root.destroy()
    
    return player1, player2

def main():
    player1, player2 = get_player_input()

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption(f"Backgammon - {player1} vs {player2}")
    
    # Crear el tablero
    tablero = Tablero()
    
    running = True

    while running:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                running = False

        # Dibujar el tablero en lugar de pantalla negra
        tablero.dibujar(screen)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()