import pygame

class Tablero:
    def __init__(self, ancho=1200, alto=600):
        self.ancho = ancho
        self.alto = alto
        self.color_fondo = (222, 184, 135)  # Beige más claro
        self.color_borde = (101, 67, 33)  # Marrón muy oscuro
        self.ancho_barra = 60
        self.color_triangulo_claro = (245, 222, 179)  # Wheat
        self.color_triangulo_oscuro = (139, 69, 19)   # Saddle Brown
        self.ancho_triangulo = 80
        self.alto_triangulo = 200
        
    def dibujar_triangulo(self, pantalla, x, y, ancho, alto, color, hacia_abajo=True):
        if hacia_abajo:
            puntos = [(x, y), (x + ancho//2, y + alto), (x + ancho, y)]
        else:
            puntos = [(x, y + alto), (x + ancho//2, y), (x + ancho, y + alto)]
        pygame.draw.polygon(pantalla, color, puntos)
        pygame.draw.polygon(pantalla, self.color_borde, puntos, 2)
        
    def dibujar(self, pantalla):
        pantalla.fill(self.color_fondo)
        pygame.draw.rect(pantalla, self.color_borde, 
                        (0, 0, self.ancho, self.alto), 3)
        barra_x = self.ancho // 2 - self.ancho_barra // 2  #barra central
        pygame.draw.rect(pantalla, self.color_borde,
                        (barra_x, 0, self.ancho_barra, self.alto))
        espacio_lado = (barra_x - 20) // 6  # Espacio para 6 triángulos en cada lado
        inicio_x_derecho = barra_x + self.ancho_barra + 10 #dibujar triángulos arriba derecha
        for i in range(6):
            x = inicio_x_derecho + i * espacio_lado
            color = self.color_triangulo_claro if i % 2 == 0 else self.color_triangulo_oscuro
            self.dibujar_triangulo(pantalla, x, 3, espacio_lado, self.alto_triangulo, 
                                 color, hacia_abajo=True)
        inicio_x_izquierdo = 10 #dibujar triángulos arriba izquierda
        for i in range(6):
            x = inicio_x_izquierdo + i * espacio_lado
            color = self.color_triangulo_claro if i % 2 == 0 else self.color_triangulo_oscuro
            self.dibujar_triangulo(pantalla, x, 3, espacio_lado, self.alto_triangulo, 
                                 color, hacia_abajo=True)

        for i in range(6):  #triángulos abajo izquierda
            x = inicio_x_izquierdo + i * espacio_lado
            color = self.color_triangulo_oscuro if i % 2 == 0 else self.color_triangulo_claro
            self.dibujar_triangulo(pantalla, x, self.alto - self.alto_triangulo - 3, espacio_lado, self.alto_triangulo, 
                                 color, hacia_abajo=False)

        # Dibujar triángulos abajo derecha
        for i in range(6):
            x = inicio_x_derecho + i * espacio_lado
            color = self.color_triangulo_oscuro if i % 2 == 0 else self.color_triangulo_claro
            self.dibujar_triangulo(pantalla, x, self.alto - self.alto_triangulo - 3, espacio_lado, self.alto_triangulo, 
                                 color, hacia_abajo=False)

if __name__ == "__main__":
    pygame.init()
    pantalla = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Tablero de Backgammon")
    
    tablero = Tablero()
    
    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False
        
        tablero.dibujar(pantalla)
        pygame.display.flip()
    
    pygame.quit()