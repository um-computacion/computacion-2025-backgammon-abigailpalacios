import pygame
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ichecker import GrupoFichas

class TableroVisual:
    def __init__(self, ancho=1400, alto=700):
        self.ancho = ancho
        self.alto = alto
        
        # --- Colores y Fuentes ---
        self.color_fondo = (222, 184, 135)  # Beige
        self.color_borde = (101, 67, 33)  # Marrón oscuro
        self.color_triangulo_claro = (245, 222, 179)  # Wheat
        self.color_triangulo_oscuro = (139, 69, 19)   # Saddle Brown
        self.color_ficha_blanca = (255, 255, 255)
        self.color_ficha_negra = (50, 50, 50)
        self.color_borde_ficha = (0, 0, 0)
        self.color_seleccion = (255, 255, 0, 150) # Amarillo semitransparente
        self.color_texto = (10, 10, 10)
        self.color_error = (200, 0, 0)
        self.color_destacado = (0, 200, 0)
        
        pygame.font.init()
        self.fuente_ui = pygame.font.SysFont("Times New Roman", 20)
        self.fuente_dados = pygame.font.SysFont("Arial", 32, bold=True)
        self.fuente_error = pygame.font.SysFont("Arial", 18, bold=True)
        self.fuente_titulo = pygame.font.SysFont("Times New Roman", 24, bold=True)

        #geometria del Tablero
        self.ancho_barra = 70
        self.alto_triangulo = 280
        self.radio_ficha = 20
        
        #calcular coordenadas clave
        self.barra_x = self.ancho // 2 - self.ancho_barra // 2 - 100
        self.espacio_lado = (self.barra_x - 5) // 6
        self.inicio_x_izquierdo = 3
        self.inicio_x_derecho = self.barra_x + self.ancho_barra
        self.y_arriba = 3
        self.y_abajo = self.alto - self.alto_triangulo - 3
        
        self.mapa_posiciones_visuales = self._crear_mapa_visual()
        
        #banco 
        self.rect_banco_blancas = pygame.Rect(self.barra_x, 0, self.ancho_barra, self.alto // 2 - 25)
        self.rect_banco_negras = pygame.Rect(self.barra_x, self.alto // 2 + 25, self.ancho_barra, self.alto // 2 - 25)
        
        #boton de tirar dados (en la barra)
        self.rect_boton_dados = pygame.Rect(self.barra_x + 5, self.alto // 2 - 45, self.ancho_barra - 10, 35)
        ancho_zona_retiro = 200
        margen_derecha = 20
        self.rect_retiro_negras = pygame.Rect(
            self.ancho - ancho_zona_retiro - margen_derecha, 
            20, 
            ancho_zona_retiro, 
            self.alto // 2 - 40
        )
        self.rect_retiro_blancas = pygame.Rect(
            self.ancho - ancho_zona_retiro - margen_derecha, 
            self.alto // 2 + 20, 
            ancho_zona_retiro, 
            self.alto // 2 - 40
        )

    def _crear_mapa_visual(self):
        mapa = {}
  
        for i in range(6):
            x = self.inicio_x_derecho + (5 - i) * self.espacio_lado
            rect = pygame.Rect(x, self.y_arriba, self.espacio_lado, self.alto_triangulo)
            mapa[i] = (x, self.y_arriba, True, rect)
            
        for i in range(6):
            x = self.inicio_x_izquierdo + (5 - i) * self.espacio_lado
            rect = pygame.Rect(x, self.y_arriba, self.espacio_lado, self.alto_triangulo)
            mapa[i+6] = (x, self.y_arriba, True, rect)
            
        for i in range(6):
            x = self.inicio_x_izquierdo + i * self.espacio_lado
            rect = pygame.Rect(x, self.y_abajo, self.espacio_lado, self.alto_triangulo)
            mapa[i+12] = (x, self.y_abajo, False, rect)
            
        for i in range(6):
            x = self.inicio_x_derecho + i * self.espacio_lado
            rect = pygame.Rect(x, self.y_abajo, self.espacio_lado, self.alto_triangulo)
            mapa[i+18] = (x, self.y_abajo, False, rect)
            
        return mapa

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
            
            if 0 < ficha_y < self.alto:
                self.dibujar_ficha(pantalla, centro_x, ficha_y, color)
    
    def dibujar_fichas_en_barra(self, pantalla, cantidad, color, zona_rect):
        centro_x = zona_rect.centerx
        for i in range(cantidad):
            if color == self.color_ficha_blanca:
                y = zona_rect.top + 20 + (i * (self.radio_ficha * 2 + 2))
            else:
                y = zona_rect.bottom - 20 - (i * (self.radio_ficha * 2 + 2))
            self.dibujar_ficha(pantalla, centro_x, y, color)

    def dibujar_fichas_retiradas(self, pantalla, cantidad, color, zona_rect):
        if cantidad == 0:
            return
            
        margen = 15
        fichas_por_fila = 5
        espacio_x = (zona_rect.width - 2 * margen) // fichas_por_fila
        espacio_y = self.radio_ficha * 2 + 5
        
        for i in range(cantidad):
            fila = i // fichas_por_fila
            columna = i % fichas_por_fila
            
            x = zona_rect.left + margen + columna * espacio_x + espacio_x // 2
            y = zona_rect.top + margen + 40 + fila * espacio_y
            
            if y < zona_rect.bottom - margen:
                self.dibujar_ficha(pantalla, x, y, color)

    def dibujar_texto(self, pantalla, texto, pos_centro, fuente, color):
        superficie_texto = fuente.render(texto, True, color)
        rect_texto = superficie_texto.get_rect(center=pos_centro)
        pantalla.blit(superficie_texto, rect_texto)
        
    def dibujar_superficie_alpha(self, pantalla, rect, color):
        s = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
        s.fill(color)
        pantalla.blit(s, rect.topleft)

    def contar_fichas_retiradas(self, tablero):
        fichas_blancas_tablero = sum(
            1 for pos in tablero if pos and "Blancas" in pos for _ in pos
        )
        fichas_negras_tablero = sum(
            1 for pos in tablero if pos and "Negras" in pos for _ in pos
        )
        
        return {
            "Blancas": 15 - fichas_blancas_tablero,
            "Negras": 15 - fichas_negras_tablero
        }

    def dibujar(self, pantalla, estado_juego, origen_seleccionado, mensaje_ui):
        
        pantalla.fill(self.color_fondo)
        pygame.draw.rect(pantalla, self.color_borde, (0, 0, self.ancho, self.alto), 3)
        pygame.draw.rect(pantalla, self.color_borde, (self.barra_x, 0, self.ancho_barra, self.alto))

        for i in range(6):
            x_dr = self.inicio_x_derecho + i * self.espacio_lado
            color_dr = self.color_triangulo_claro if i % 2 == 0 else self.color_triangulo_oscuro
            self.dibujar_triangulo(pantalla, x_dr, self.y_arriba, self.espacio_lado, self.alto_triangulo, color_dr, True)
            
            x_iz = self.inicio_x_izquierdo + i * self.espacio_lado
            color_iz = self.color_triangulo_claro if i % 2 == 0 else self.color_triangulo_oscuro
            self.dibujar_triangulo(pantalla, x_iz, self.y_arriba, self.espacio_lado, self.alto_triangulo, color_iz, True)

            color_iz_ab = self.color_triangulo_oscuro if i % 2 == 0 else self.color_triangulo_claro
            self.dibujar_triangulo(pantalla, x_iz, self.y_abajo, self.espacio_lado, self.alto_triangulo, color_iz_ab, False)
            
            color_dr_ab = self.color_triangulo_oscuro if i % 2 == 0 else self.color_triangulo_claro
            self.dibujar_triangulo(pantalla, x_dr, self.y_abajo, self.espacio_lado, self.alto_triangulo, color_dr_ab, False)
        
        pygame.draw.rect(pantalla, (60, 60, 60), self.rect_retiro_negras)
        pygame.draw.rect(pantalla, self.color_borde, self.rect_retiro_negras, 3)
        self.dibujar_texto(
            pantalla, 
            "FICHAS RETIRADAS", 
            (self.rect_retiro_negras.centerx, self.rect_retiro_negras.top + 20), 
            self.fuente_ui, 
            self.color_ficha_blanca
        )
        
        pygame.draw.rect(pantalla, (240, 240, 240), self.rect_retiro_blancas)
        pygame.draw.rect(pantalla, self.color_borde, self.rect_retiro_blancas, 3)
        self.dibujar_texto(
            pantalla, 
            "FICHAS RETIRADAS", 
            (self.rect_retiro_blancas.centerx, self.rect_retiro_blancas.top + 20), 
            self.fuente_ui, 
            self.color_texto
        )

        tablero_logico = estado_juego["tablero"]
        for pos_logica, fichas in enumerate(tablero_logico):
            if fichas:
                cantidad = len(fichas)
                color = self.color_ficha_blanca if fichas[0] == "Blancas" else self.color_ficha_negra
                x, y, hacia_abajo, rect = self.mapa_posiciones_visuales[pos_logica]
                self.dibujar_fichas_en_triangulo(pantalla, x, y, self.espacio_lado, cantidad, color, hacia_abajo)

        banco = estado_juego["banco"]
        if banco["Blancas"] > 0:
            self.dibujar_fichas_en_barra(pantalla, banco["Blancas"], self.color_ficha_blanca, self.rect_banco_blancas)
        if banco["Negras"] > 0:
            self.dibujar_fichas_en_barra(pantalla, banco["Negras"], self.color_ficha_negra, self.rect_banco_negras)

        fichas_retiradas = self.contar_fichas_retiradas(tablero_logico)
        fichas_retiradas["Blancas"] -= banco["Blancas"]
        fichas_retiradas["Negras"] -= banco["Negras"]
        
        self.dibujar_fichas_retiradas(pantalla, fichas_retiradas["Negras"], self.color_ficha_negra, self.rect_retiro_negras)
        self.dibujar_fichas_retiradas(pantalla, fichas_retiradas["Blancas"], self.color_ficha_blanca, self.rect_retiro_blancas)
        
        self.dibujar_texto(
            pantalla, 
            f"{fichas_retiradas['Negras']}/15", 
            (self.rect_retiro_negras.centerx, self.rect_retiro_negras.bottom - 15), 
            self.fuente_dados, 
            self.color_ficha_blanca
        )
        self.dibujar_texto(
            pantalla, 
            f"{fichas_retiradas['Blancas']}/15", 
            (self.rect_retiro_blancas.centerx, self.rect_retiro_blancas.bottom - 15), 
            self.fuente_dados, 
            self.color_texto
        )

        pygame.draw.rect(pantalla, (0, 120, 0), self.rect_boton_dados)
        pygame.draw.rect(pantalla, self.color_borde, self.rect_boton_dados, 2)
        self.dibujar_texto(pantalla, "TIRAR", self.rect_boton_dados.center, self.fuente_ui, (255,255,255))
        
        # Turno
        turno_texto = f"Turno: {estado_juego['turno']}"
        self.dibujar_texto(pantalla, turno_texto, (self.barra_x + self.ancho_barra//2, 20), self.fuente_ui, self.color_fondo)
        
        # Dados
        dados_texto = f"{estado_juego['dados']}"
        self.dibujar_texto(pantalla, dados_texto, (self.barra_x + self.ancho_barra//2, self.alto // 2 + 60), self.fuente_dados, self.color_ficha_blanca)

        # Mensaje 
        color_msg = self.color_error if "Error" in mensaje_ui else self.color_destacado
        self.dibujar_texto(pantalla, mensaje_ui, (self.ancho // 2, self.alto - 25), self.fuente_error, color_msg)
        
        # Ganador
        if estado_juego["ganador"]:
            s = pygame.Surface((self.ancho, self.alto), pygame.SRCALPHA)
            s.fill((0,0,0,180))
            pantalla.blit(s, (0,0))
            texto_ganador = f"¡GANADOR: {estado_juego['ganador']}!"
            self.dibujar_texto(pantalla, texto_ganador, (self.ancho // 2, self.alto // 2), pygame.font.SysFont("Arial", 70, bold=True), (255, 215, 0))

        if origen_seleccionado is not None:
            if origen_seleccionado == "banco":
                zona_banco = self.rect_banco_blancas if estado_juego["ficha actual"] == "Blancas" else self.rect_banco_negras
                self.dibujar_superficie_alpha(pantalla, zona_banco, self.color_seleccion)
            elif isinstance(origen_seleccionado, int):
                rect_seleccion = self.mapa_posiciones_visuales[origen_seleccionado][3]
                self.dibujar_superficie_alpha(pantalla, rect_seleccion, self.color_seleccion)

    def convertir_clic_a_posicion(self, pos_clic):
        for pos_logica, (x, y, ha, rect) in self.mapa_posiciones_visuales.items():
            if rect.collidepoint(pos_clic):
                return pos_logica
                
        if self.rect_banco_blancas.collidepoint(pos_clic) or self.rect_banco_negras.collidepoint(pos_clic):
            return "banco"

        if self.rect_retiro_blancas.collidepoint(pos_clic) or self.rect_retiro_negras.collidepoint(pos_clic):
            return "retiro"

        if self.rect_boton_dados.collidepoint(pos_clic):
            return None

        return None