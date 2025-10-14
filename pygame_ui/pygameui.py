import pygame


def get_player():
    pygame.init()
    pantalla = pygame.display.set_mode((400, 300))  #superficie de visualizacion 400x300
    pygame.display.set_caption("Backgammon jugadores")

    fuente = pygame.font.Font(None, 36)
    texto1 = fuente.render("Jugador 1 (Blancas)", True, (0, 0, 0))
    texto2 = fuente.render("Jugador 2 (Negras)", True, (0, 0, 0))
    
    pantalla.fill((240, 230, 200))
    pantalla.blit(texto1, (50, 100))
    pantalla.blit(texto2, (50, 150))
    pygame.display.flip()
    return "Jugador 1", "Jugador 2"
