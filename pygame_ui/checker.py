import pygame

class Ficha:
    def __init__(self, color, radio=18):
        self.color = color
        self.radio = radio
        self.color_borde = (0, 0, 0)
        
    def dibujar(self, pantalla, x, y):
        pygame.draw.circle(pantalla, self.color, (x, y), self.radio)
        pygame.draw.circle(pantalla, self.color_borde, (x, y), self.radio, 2)

class GrupoFichas:
    def __init__(self, color, cantidad, radio=18):
        self.fichas = [Ficha(color, radio) for _ in range(cantidad)]
        self.color = color
        
    def dibujar_en_triangulo(self, pantalla, triangulo_x, triangulo_y, ancho_triangulo, alto_triangulo, hacia_abajo=True):
        centro_x = triangulo_x + ancho_triangulo // 2
        for i, ficha in enumerate(self.fichas):
            if hacia_abajo:
                ficha_y = triangulo_y + 25 + (i * (ficha.radio * 2 + 2))
            else:
                ficha_y = triangulo_y + alto_triangulo - 25 - (i * (ficha.radio * 2 + 2))
            ficha.dibujar(pantalla, centro_x, ficha_y)
