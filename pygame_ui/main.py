import pygame
import tkinter as tk
from tkinter import simpledialog
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from core.backgammongame import Backgammongame
from core.player import Player
from iboard import TableroVisual


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

# controlador principal
def main():
    player1_name, player2_name = get_player_input()
    
    if not player1_name or not player2_name:
        print("Juego cancelado.")
        return

    pygame.init()
    pygame.font.init()
    
    player1 = Player(player1_name, "Blancas")
    player2 = Player(player2_name, "Negras")
    juego = Backgammongame(player1, player2)

    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption(f"Backgammon - {player1_name} vs {player2_name}")
    vista_tablero = TableroVisual()

    running = True
    dados_tirados = False
    mensaje_ui = "¡Bienvenido! Tira los dados para comenzar."
    
    clock = pygame.time.Clock()

    while running:
        estado_juego = juego.estado_juego()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_clic = pygame.mouse.get_pos()

                # Solo manejar el botón de tirar dados
                if vista_tablero.rect_boton_dados.collidepoint(pos_clic):
                    if not dados_tirados:
                        try:
                            juego.tirar_dados()
                            dados_tirados = True
                            mensaje_ui = f"Dados tirados: {estado_juego['dados']}"
                            print(f"Jugador {estado_juego['turno']} tiró: {estado_juego['dados']}")
                        except Exception as e:
                            mensaje_ui = f"Error: {e}"
                    else:
                        mensaje_ui = "Ya tiraste los dados. Presiona SPACE para pasar turno."
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and dados_tirados:
                    # Pasar turno
                    juego.definir_turno()
                    dados_tirados = False
                    mensaje_ui = f"Turno de {juego.get_turno().get_nombre()}. ¡Tira los dados!"

        # Dibujar
        screen.fill((0, 0, 0))
        vista_tablero.dibujar(screen, estado_juego, None, mensaje_ui)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()