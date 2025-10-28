import pygame
import tkinter as tk
from tkinter import simpledialog
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from core.backgammongame import Backgammongame
from core.player import Player
from iboard import TableroVisual
from core.exceptions import BackgammonException, MovimientoInvalido, SinMovimientos

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
    player1_name, player2_name = get_player_input()
    
    if not player1_name or not player2_name:
        print("Juego cancelado.")
        return

    pygame.init()
    pygame.font.init()
    
    player1 = Player(player1_name, "Blancas")
    player2 = Player(player2_name, "Negras")
    juego = Backgammongame(player1, player2)

    screen = pygame.display.set_mode((1400, 700))
    pygame.display.set_caption(f"Backgammon - {player1_name} vs {player2_name}")
    vista_tablero = TableroVisual()

    running = True
    dados_tirados = False
    origen_seleccionado = None  
    mensaje_ui = "¡Bienvenido! Tira los dados para comenzar."
    
    clock = pygame.time.Clock()

    while running:
        estado_juego = juego.estado_juego()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_clic = pygame.mouse.get_pos()
                mensaje_ui = "" 
                if vista_tablero.rect_boton_dados.collidepoint(pos_clic):
                    if not dados_tirados and not estado_juego["ganador"]:
                        try:
                            juego.tirar_dados()
                            dados_tirados = True
                            if not juego.mov_posible():
                                mensaje_ui = "No hay movimientos. Pasa el turno."
                            else:
                                mensaje_ui = f"Mueve {estado_juego['ficha actual']}"
                        except Exception as e:
                            mensaje_ui = f"Error: {e}"
                    elif estado_juego["ganador"]:
                         mensaje_ui = f"Juego terminado. Ganador: {estado_juego['ganador']}"
                    else:
                        mensaje_ui = "Ya tiraste. Pasa el turno cuando termines."
                    origen_seleccionado = None
            
                elif dados_tirados and not estado_juego["ganador"]:
                    pos_logica = vista_tablero.convertir_clic_a_posicion(pos_clic)

                    if pos_logica is None:
                        origen_seleccionado = None
                        mensaje_ui = "Clic fuera del tablero."
                        continue

                    if origen_seleccionado is None:

                        if pos_logica == "banco" and estado_juego["estado"] == "reingreso":
                            origen_seleccionado = "banco"
                            mensaje_ui = "Banco seleccionado. Elige destino."
                        elif pos_logica == "retiro":
                            mensaje_ui = "Esta es la zona para sacar fichas."
                        elif isinstance(pos_logica, int):
                            if estado_juego["tablero"][pos_logica] and \
                               estado_juego["tablero"][pos_logica][0] == estado_juego["ficha actual"]:
                                origen_seleccionado = pos_logica
                                mensaje_ui = f"Posición {pos_logica+1} seleccionada. Elige destino."
                            else:
                                mensaje_ui = "No hay fichas tuyas en esa posición."
                    
                    else:
                        destino = pos_logica
                        
                        try:
                            if origen_seleccionado == "banco":
                                if isinstance(destino, int):
                                    ficha = estado_juego["ficha actual"]
                                    dado_necesario = -1
                                    if ficha == "Blancas":
                                        dado_necesario = destino + 1 # pos 0 -> dado 1
                                    else:
                                        dado_necesario = 24 - destino # pos 23 -> dado 1
                                    
                                    juego.reingresar_ficha(dado_necesario)
                                    mensaje_ui = f"Ficha reingresada en {destino+1}"
                                else:
                                    raise MovimientoInvalido("Destino inválido para reingresar")

                            elif destino == "retiro":

                                if isinstance(origen_seleccionado, int):
                                    juego.retirar_ficha(origen_seleccionado)
                                    mensaje_ui = f"Ficha retirada desde {origen_seleccionado+1}"
                                else:
                                    raise MovimientoInvalido("Origen inválido para retirar")

                            elif isinstance(destino, int) and isinstance(origen_seleccionado, int):
                                juego.mover_ficha(origen_seleccionado, destino)
                                mensaje_ui = f"Movido de {origen_seleccionado+1} a {destino+1}"
                            
                            else:
                                raise MovimientoInvalido("Movimiento no reconocido")

                        except (BackgammonException, ValueError) as e:
                            mensaje_ui = f"Error: {e}"
                        origen_seleccionado = None
        if dados_tirados and juego.turno_completo() and not estado_juego["ganador"]:
            juego.definir_turno()
            dados_tirados = False
            origen_seleccionado = None
            mensaje_ui = f"Turno de {juego.get_turno().get_nombre()}. ¡Tira los dados!"
        screen.fill((0, 0, 0)) 
        vista_tablero.dibujar(screen, estado_juego, origen_seleccionado, mensaje_ui)
        
        pygame.display.flip() 
        clock.tick(30) 

    pygame.quit()

if __name__ == "__main__":
    main()