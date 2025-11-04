# Prompts Desarrollo

## Prompt 1

**Herramienta utilizada:**
- GitHub Copilot

**Texto exacto del Prompt:**
```
como creo una ventana de pygame con un tablero de backgammon que tenga 24 triangulos
```

**Respuesta de la IA:**
```python
import pygame

pygame.init()
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("Backgammon")

# Definir colores
BEIGE = (222, 184, 135)
BROWN = (139, 69, 19)
WHEAT = (245, 222, 179)

# Dibujar triángulos
for i in range(12):
    x = i * 100
    if i % 2 == 0:
        color = WHEAT
    else:
        color = BROWN
    pygame.draw.polygon(screen, color, [(x, 0), (x+50, 250), (x+100, 0)])
```

**Uso:**
- Usada con modificaciones: Cambié el tamaño de ventana a 1400x700, ajusté posiciones y agregué triángulos superiores e inferiores

**Referencia:**
* `pygame_ui/iboard.py`

---

## Prompt 2

**Herramienta utilizada:**
- ChatGPT (GPT-4)

**Texto exacto del Prompt:**
```
necesito dibujar fichas circulares en pygame que se apilen en los triangulos del tablero, como hago eso
```

**Respuesta de la IA:**
```python
def dibujar_ficha(screen, x, y, radio, color):
    pygame.draw.circle(screen, color, (x, y), radio)
    pygame.draw.circle(screen, (0, 0, 0), (x, y), radio, 2)  # borde

# Para apilar fichas:
for i in range(cantidad_fichas):
    ficha_y = y_base + (i * (radio * 2 + 2))
    dibujar_ficha(screen, centro_x, ficha_y, 20, color)
```

**Uso:**
- Usada sin cambios

**Referencia:**
* `pygame_ui/iboard.py` - método `dibujar_fichas_en_triangulo`

---

## Prompt 3

**Herramienta utilizada:**
- GitHub Copilot

**Texto exacto del Prompt:**
```
como detecto clicks del mouse en pygame y convierto las coordenadas en posiciones del tablero logico
```

**Respuesta de la IA:**
```python
for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = event.pos
        # Convertir coordenadas a posición lógica
        if rect_triangulo.collidepoint(pos):
            posicion_logica = calcular_posicion(pos)
```

**Uso:**
- Usada con modificaciones: Creé un método `convertir_clic_a_posicion()` que usa diccionario de rectángulos

**Referencia:**
* `pygame_ui/events.py` - método `_handle_mouse_click`
* `pygame_ui/iboard.py` - método `convertir_clic_a_posicion`

---

## Prompt 4

**Herramienta utilizada:**
- ChatGPT (GPT-4)

**Texto exacto del Prompt:**
```
como creo un boton en pygame para tirar los dados, que se vea bien y sea clickeable
```

**Respuesta de la IA:**
```python
# Crear rectángulo del botón
rect_boton = pygame.Rect(barra_x + 5, alto // 2 - 45, ancho_barra - 10, 35)

# Dibujar botón
pygame.draw.rect(screen, (0, 120, 0), rect_boton)
pygame.draw.rect(screen, (0, 0, 0), rect_boton, 2)

# Agregar texto
font = pygame.font.SysFont("Arial", 20)
text = font.render("TIRAR", True, (255, 255, 255))
text_rect = text.get_rect(center=rect_boton.center)
screen.blit(text, text_rect)

# Detectar click
if event.type == pygame.MOUSEBUTTONDOWN:
    if rect_boton.collidepoint(event.pos):
        tirar_dados()
```

**Uso:**
- Usada sin cambios

**Referencia:**
* `pygame_ui/iboard.py` - inicialización de `rect_boton_dados`
* `pygame_ui/events.py` - método `_handle_dice_button`

---

## Prompt 5

**Herramienta utilizada:**
- GitHub Copilot

**Texto exacto del Prompt:**
```
necesito resaltar los triangulos donde se puede mover una ficha con color verde semitransparente
```

**Respuesta de la IA:**
```python
# Crear superficie con transparencia
superficie = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
superficie.fill((0, 255, 0, 100))  # Verde con alpha
screen.blit(superficie, rect.topleft)
```

**Uso:**
- Usada sin cambios

**Referencia:**
* `pygame_ui/iboard.py` - método `dibujar_superficie_alpha`

---

## Prompt 6

**Herramienta utilizada:**
- ChatGPT (GPT-4)

**Texto exacto del Prompt:**
```
como hago un dialogo de entrada en tkinter para pedir nombres de jugadores antes de iniciar pygame
```

**Respuesta de la IA:**
```python
import tkinter as tk

def get_names():
    def submit():
        nonlocal name1, name2
        name1 = entry1.get()
        name2 = entry2.get()
        root.quit()
    
    name1 = name2 = ""
    root = tk.Tk()
    root.title("Nombres")
    
    tk.Label(root, text="Jugador 1:").pack()
    entry1 = tk.Entry(root)
    entry1.pack()
    
    tk.Label(root, text="Jugador 2:").pack()
    entry2 = tk.Entry(root)
    entry2.pack()
    
    tk.Button(root, text="OK", command=submit).pack()
    
    root.mainloop()
    root.destroy()
    return name1, name2
```

**Uso:**
- Usada con modificaciones: Agregué estilos, colores y valores por defecto

**Referencia:**
* `pygame_ui/main.py` - función `get_player_input`

---

## Prompt 7

**Herramienta utilizada:**
- GitHub Copilot

**Texto exacto del Prompt:**
```
como separo la logica de eventos de pygame de la logica de renderizado, quiero una arquitectura MVC
```

**Respuesta de la IA:**
```python
# Crear clase EventHandler
class EventHandler:
    def __init__(self, juego, vista):
        self.juego = juego
        self.vista = vista
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            # Manejar otros eventos
        return True

# En main.py
event_handler = EventHandler(juego, tablero_visual)
while event_handler.running:
    event_handler.handle_events()
    tablero_visual.dibujar(screen, estado)
```

**Uso:**
- Usada sin cambios, base de la arquitectura actual

**Referencia:**
* `pygame_ui/events.py` - clase `EventHandler`
* `pygame_ui/main.py` - loop principal

---

## Prompt 8

**Herramienta utilizada:**
- ChatGPT (GPT-4)

**Texto exacto del Prompt:**
```
tengo que mostrar fichas retiradas en una zona lateral del tablero, como las organizo en filas y columnas
```

**Respuesta de la IA:**
```python
fichas_por_fila = 5
margen = 15

for i in range(cantidad_fichas_retiradas):
    fila = i // fichas_por_fila
    columna = i % fichas_por_fila
    
    x = zona_x + margen + columna * espacio_x
    y = zona_y + margen + fila * espacio_y
    
    if y < zona_bottom:
        dibujar_ficha(screen, x, y, color)
```

**Uso:**
- Usada con modificaciones: Ajusté espaciado y agregué centrado

**Referencia:**
* `pygame_ui/iboard.py` - método `dibujar_fichas_retiradas`

---

## Prompt 9

**Herramienta utilizada:**
- GitHub Copilot

**Texto exacto del Prompt:**
```
como calculo que fichas ya fueron retiradas del juego para mostrar el contador X/15
```

**Respuesta de la IA:**
```python
def contar_retiradas(tablero, banco):
    fichas_en_tablero = sum(1 for pos in tablero if pos for ficha in pos)
    fichas_en_banco = banco["Blancas"]
    fichas_retiradas = 15 - fichas_en_tablero - fichas_en_banco
    return fichas_retiradas
```

**Uso:**
- Usada con modificaciones: Separé el cálculo por color de ficha

**Referencia:**
* `pygame_ui/iboard.py` - método `_contar_fichas_retiradas`

---

## Prompt 10

**Herramienta utilizada:**
- ChatGPT (GPT-4)

**Texto exacto del Prompt:**
```
necesito un mapa que convierta posiciones logicas 0-23 en coordenadas visuales x,y del tablero pygame
```

**Respuesta de la IA:**
```python
mapa = {}
for i in range(6):
    x = inicio_derecha + i * espacio
    mapa[i] = (x, y_arriba, True)  # True = hacia abajo
    
for i in range(6):
    x = inicio_izquierda + i * espacio
    mapa[i+6] = (x, y_arriba, True)
    
# Continuar con parte inferior...
```

**Uso:**
- Usada con modificaciones: Agregué pygame.Rect para detección de clicks

**Referencia:**
* `pygame_ui/iboard.py` - método `_crear_mapa_visual`

---

## Prompt 11

**Herramienta utilizada:**
- GitHub Copilot

**Texto exacto del Prompt:**
```
como dibujo texto centrado en pygame con diferentes fuentes y colores
```

**Respuesta de la IA:**
```python
font = pygame.font.SysFont("Arial", 24, bold=True)
texto_surface = font.render("Texto", True, (255, 255, 255))
texto_rect = texto_surface.get_rect(center=(x, y))
screen.blit(texto_surface, texto_rect)
```

**Uso:**
- Usada sin cambios

**Referencia:**
* `pygame_ui/iboard.py` - método `dibujar_texto`

---

## Prompt 12

**Herramienta utilizada:**
- ChatGPT (GPT-4)

**Texto exacto del Prompt:**
```
cuando el jugador selecciona una ficha, quiero mostrar solo los movimientos posibles desde esa posicion
```

**Respuesta de la IA:**
```python
if origen_seleccionado is None:
    # Primera selección
    origen_seleccionado = posicion_clickeada
    todos_movimientos = juego.movimientos_posibles()
    movimientos_filtrados = {origen_seleccionado: todos_movimientos.get(origen_seleccionado, [])}
else:
    # Segunda selección = destino
    juego.mover_ficha(origen_seleccionado, posicion_clickeada)
    origen_seleccionado = None
```

**Uso:**
- Usada con modificaciones: Agregué manejo de errores y feedback visual

**Referencia:**
* `pygame_ui/events.py` - métodos `_handle_select_origin` y `_handle_move_to_destination`

---

## Prompt 13

**Herramienta utilizada:**
- GitHub Copilot

**Texto exacto del Prompt:**
```
quiero una pantalla de victoria semitransparente cuando alguien gana con el nombre del ganador
```

**Respuesta de la IA:**
```python
if estado_juego["ganador"]:
    overlay = pygame.Surface((ancho, alto), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    screen.blit(overlay, (0, 0))
    
    font_grande = pygame.font.SysFont("Arial", 70, bold=True)
    texto = f"¡GANADOR: {estado_juego['ganador']}!"
    texto_surface = font_grande.render(texto, True, (255, 215, 0))
    texto_rect = texto_surface.get_rect(center=(ancho//2, alto//2))
    screen.blit(texto_surface, texto_rect)
```

**Uso:**
- Usada sin cambios

**Referencia:**
* `pygame_ui/iboard.py` - método `dibujar` (sección ganador)

---

## Prompt 14 (DESCARTADO)

**Herramienta utilizada:**
- ChatGPT (GPT-4)

**Texto exacto del Prompt:**
```
como agrego sonidos cuando muevo fichas o tiro dados en pygame
```

**Respuesta de la IA:**
```python
pygame.mixer.init()
sonido_dado = pygame.mixer.Sound("dados.wav")
sonido_movimiento = pygame.mixer.Sound("movimiento.wav")

# Al tirar dados
sonido_dado.play()

# Al mover ficha
sonido_movimiento.play()
```

**Uso:**
- Descartada: Decidimos no incluir sonidos para mantener el proyecto simple y enfocado en la lógica

**Referencia:**
* Ninguna (no implementado)