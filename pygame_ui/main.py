import pygame
import tkinter as tk
from tkinter import simpledialog

def main():


    pygame.init()
    screen = pygame.display.set_mode((800, 600))  #ventana de 800x600
    pygame.display.set_caption(f"Backgammon")  #titulo con nombres
    running = True

    while running:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  #pinta la pantalla de negro
        pygame.display.flip()  #actualiza la pantalla

    pygame.quit()

if __name__ == "__main__":
    main()