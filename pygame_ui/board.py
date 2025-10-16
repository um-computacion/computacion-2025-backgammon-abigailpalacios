import pygame

class Tablero:
    def __init__(self, ancho=800, alto=600):
        self.ancho = ancho
        self.alto = alto
        
        # Colores
        self.color_fondo = (139, 69, 19)  # Marrón
        self.triangulo_claro = (245, 222, 179)  # Trigo
        self.triangulo_oscuro = (160, 82, 45)  # Marrón silla
        self.color_borde = (101, 67, 33)  # Marrón oscuro
        
        # Diseño del tablero
        self.ancho_triangulo = 50
        self.alto_triangulo = 200
        self.ancho_barra = 60
        
    def dibujar(self, pantalla):
        # Rellenar fondo
        pantalla.fill(self.color_fondo)
        
        # Dibujar borde
        pygame.draw.rect(pantalla, self.color_borde, 
                        (0, 0, self.ancho, self.alto), 5)

        # Dibujar barra central
        barra_x = self.ancho // 2 - self.ancho_barra // 2
        pygame.draw.rect(pantalla, self.color_borde,
                        (barra_x, 50, self.ancho_barra, self.alto - 100))
    
if __name__ == "__main__":
    pygame.init()
    pantalla = pygame.display.set_mode((800, 600))
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