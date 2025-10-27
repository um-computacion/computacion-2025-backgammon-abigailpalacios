import pygame
from pygame_ui.checker import GrupoFichas

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
        self.alto_triangulo = 250
        self.color_ficha_blanca = (255, 255, 255)  # Blanco
        self.color_ficha_negra = (50, 50, 50)  # Gris oscuro/negro
        self.color_borde_ficha = (0, 0, 0)  # Negro para bordes
        self.radio_ficha = 18
        
        # Inicializar grupos de fichas según posiciones iniciales
        self.grupos_fichas = {
            0: GrupoFichas(self.color_ficha_blanca, 2),
            11: GrupoFichas(self.color_ficha_blanca, 5),
            16: GrupoFichas(self.color_ficha_blanca, 3),
            18: GrupoFichas(self.color_ficha_blanca, 5),
            23: GrupoFichas(self.color_ficha_negra, 2),
            12: GrupoFichas(self.color_ficha_negra, 5),
            7: GrupoFichas(self.color_ficha_negra, 3),
            5: GrupoFichas(self.color_ficha_negra, 5)
        }
        
    def dibujar_triangulo(self, pantalla, x, y, ancho, alto, color, hacia_abajo=True):
        if hacia_abajo:
            puntos = [(x, y), (x + ancho//2, y + alto), (x + ancho, y)]
        else:
            puntos = [(x, y + alto), (x + ancho//2, y), (x + ancho, y + alto)]
        pygame.draw.polygon(pantalla, color, puntos)
        pygame.draw.polygon(pantalla, self.color_borde, puntos, 2)
        
    def dibujar_ficha(self, pantalla, x, y, color):
        pygame.draw.circle(pantalla, color, (x, y), self.radio_ficha)
        pygame.draw.circle(pantalla, self.color_borde_ficha, (x, y), self.radio_ficha, 2)
    
    def dibujar_fichas_en_triangulo(self, pantalla, triangulo_x, triangulo_y, ancho_triangulo, cantidad, color, hacia_abajo=True):
        centro_x = triangulo_x + ancho_triangulo // 2
        for i in range(cantidad):
            if hacia_abajo:
                ficha_y = triangulo_y + 25 + (i * (self.radio_ficha * 2 + 2))
            else:
                ficha_y = triangulo_y + self.alto_triangulo - 25 - (i * (self.radio_ficha * 2 + 2))
            self.dibujar_ficha(pantalla, centro_x, ficha_y, color)
        
    def dibujar_fichas_iniciales(self, pantalla, espacio_lado, inicio_x_izquierdo, inicio_x_derecho):
        # Mapeo de posiciones lógicas a coordenadas visuales
        posiciones_visual = {
            0: (inicio_x_derecho + 5 * espacio_lado, 3, True),
            11: (inicio_x_izquierdo + 0 * espacio_lado, 3, True),
            16: (inicio_x_izquierdo + 4 * espacio_lado, self.alto - self.alto_triangulo - 3, False),
            18: (inicio_x_derecho + 0 * espacio_lado, self.alto - self.alto_triangulo - 3, False),
            23: (inicio_x_derecho + 5 * espacio_lado, self.alto - self.alto_triangulo - 3, False),
            12: (inicio_x_izquierdo + 0 * espacio_lado, self.alto - self.alto_triangulo - 3, False),
            7: (inicio_x_izquierdo + 4 * espacio_lado, 3, True),
            5: (inicio_x_derecho + 0 * espacio_lado, 3, True)
        }
        
        for posicion, grupo in self.grupos_fichas.items():
            x, y, hacia_abajo = posiciones_visual[posicion]
            grupo.dibujar_en_triangulo(pantalla, x, y, espacio_lado, self.alto_triangulo, hacia_abajo)
        
    def dibujar(self, pantalla):
        pantalla.fill(self.color_fondo)
        pygame.draw.rect(pantalla, self.color_borde, 
                        (0, 0, self.ancho, self.alto), 3)
        barra_x = self.ancho // 2 - self.ancho_barra // 2  #barra central
        pygame.draw.rect(pantalla, self.color_borde,
                        (barra_x, 0, self.ancho_barra, self.alto))
        
        # Calcular espacio más ajustado para los triángulos
        espacio_lado = (barra_x - 5) // 6  # Menos margen para que queden más cerca
        
        inicio_x_derecho = barra_x + self.ancho_barra #dibujar triángulos arriba derecha
        for i in range(6):
            x = inicio_x_derecho + i * espacio_lado
            color = self.color_triangulo_claro if i % 2 == 0 else self.color_triangulo_oscuro
            self.dibujar_triangulo(pantalla, x, 3, espacio_lado, self.alto_triangulo, 
                                 color, hacia_abajo=True)
        inicio_x_izquierdo = 3 #dibujar triángulos arriba izquierda
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
        
        #dibujar fichas blancas iniciales según posiciones del core
        x_pos0 = inicio_x_derecho + 5 * espacio_lado
        self.dibujar_fichas_en_triangulo(pantalla, x_pos0, 3, espacio_lado, 2, self.color_ficha_blanca, True)
        x_pos11 = inicio_x_izquierdo + 0 * espacio_lado
        self.dibujar_fichas_en_triangulo(pantalla, x_pos11, 3, espacio_lado, 5, self.color_ficha_blanca, True)
        x_pos16 = inicio_x_izquierdo + 4 * espacio_lado  
        self.dibujar_fichas_en_triangulo(pantalla, x_pos16, self.alto - self.alto_triangulo - 3, espacio_lado, 3, self.color_ficha_blanca, False)
        x_pos18 = inicio_x_derecho + 0 * espacio_lado
        self.dibujar_fichas_en_triangulo(pantalla, x_pos18, self.alto - self.alto_triangulo - 3, espacio_lado, 5, self.color_ficha_blanca, False)

        x_negra_1 = inicio_x_derecho + 5 * espacio_lado
        self.dibujar_fichas_en_triangulo(pantalla, x_negra_1, self.alto - self.alto_triangulo - 3, espacio_lado, 2, self.color_ficha_negra, False)

        # Dibujar fichas negras iniciales según posiciones del core
        x_negra_2 = inicio_x_izquierdo + 0 * espacio_lado
        self.dibujar_fichas_en_triangulo(pantalla, x_negra_2, self.alto - self.alto_triangulo - 3, espacio_lado, 5, self.color_ficha_negra, False)
        x_negra_3 = inicio_x_izquierdo + 4 * espacio_lado
        self.dibujar_fichas_en_triangulo(pantalla, x_negra_3, 3, espacio_lado, 3, self.color_ficha_negra, True)
        x_negra_4 = inicio_x_derecho + 0 * espacio_lado
        self.dibujar_fichas_en_triangulo(pantalla, x_negra_4, 3, espacio_lado, 5, self.color_ficha_negra, True)

        # Dibujar fichas usando la nueva clase
        self.dibujar_fichas_iniciales(pantalla, espacio_lado, inicio_x_izquierdo, inicio_x_derecho)

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