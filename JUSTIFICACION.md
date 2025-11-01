# JUSTIFICACIÓN DEL PROYECTO BACKGAMMON

## Introducción

Este documento describe las decisiones de diseño, arquitectura y tecnologías utilizadas en el desarrollo del juego Backgammon como parte del curso de Computación 2025.

## Arquitectura del Proyecto

### Estructura de Directorios

El proyecto sigue una arquitectura modular separando responsabilidades en diferentes capas:

```
backgammon/
├── core/           # Lógica del juego (Modelo)
├── cli/            # Interfaz de línea de comandos
├── pygame_ui/      # Interfaz gráfica con Pygame
└── test/           # Tests unitarios
```

### Patrón de Diseño: MVC (Modelo-Vista-Controlador)

#### Modelo (core/)
- **Responsabilidad**: Contiene toda la lógica del juego
- **Clases principales**:
  - `Backgammongame`: Orquesta el juego completo
  - `Board`: Gestiona el tablero y las posiciones
  - `Player`: Representa a los jugadores
  - `Dice`: Maneja el lanzamiento de dados
  - `Checker`: Representa las fichas individuales

**Justificación**: Separar la lógica del juego permite reutilizarla en diferentes interfaces (CLI y GUI) sin duplicar código.

#### Vista (pygame_ui/ y cli/)
- **CLI**: Interfaz de texto simple para testing rápido
- **Pygame UI**: Interfaz gráfica completa
  - `iboard.py`: Solo renderizado visual (Vista pura)
  - `events.py`: Manejo de eventos y lógica de UI (Controlador)
  - `main.py`: Inicialización y loop principal

**Justificación**: Mantener el código de renderizado separado de la lógica de eventos facilita el mantenimiento y testing.

## Decisiones de Diseño

### 1. Sistema de Coordenadas del Tablero

Se utilizan índices 0-23 para representar las 24 posiciones del tablero:
- **Blancas**: Mueven de 0 → 23
- **Negras**: Mueven de 23 → 0

**Justificación**: Usar índices numéricos simples facilita los cálculos de distancia y validaciones de movimiento.

### 2. Representación del Estado del Juego

El método `estado_juego()` retorna un diccionario con toda la información necesaria:

```python
{
    "estado": "en curso" | "reingreso" | "ganado",
    "turno": "nombre_jugador",
    "dados": [3, 5],
    "tablero": [...],
    "banco": {"Blancas": 0, "Negras": 0},
    "movimientos posibles": {...},
    "ganador": None | "nombre_jugador"
}
```

**Justificación**: Centralizar el estado en un solo método facilita la sincronización entre modelo y vista.

### 3. Validación de Movimientos

La validación se realiza en dos niveles:
1. **Board**: Valida reglas básicas (posiciones válidas, fichas bloqueadas)
2. **Backgammongame**: Valida contexto del juego (dados disponibles, banco, etc.)

**Justificación**: Separación de responsabilidades - Board no necesita conocer sobre dados o turnos.

### 4. Manejo de Excepciones Personalizadas

Se crearon excepciones específicas:
- `MovimientoInvalido`: Movimiento no permitido por las reglas
- `SinMovimientos`: No hay movimientos posibles con los dados actuales
- `GameOver`: El juego ha terminado

**Justificación**: Excepciones descriptivas facilitan el debugging y proporcionan mensajes claros al usuario.

## Tecnologías Utilizadas

### Python 3.13
**Justificación**: Lenguaje moderno con excelente soporte para testing y desarrollo rápido.

### Pygame 2.6.1
**Justificación**: 
- Biblioteca madura para desarrollo de juegos 2D
- Fácil manejo de eventos y renderizado
- Buen rendimiento para juegos de tablero

### Tkinter
**Justificación**: Incluido en Python por defecto, ideal para diálogos simples como entrada de nombres.

### Unittest
**Justificación**: Framework de testing estándar de Python, integración perfecta con el ecosistema.

## Características Implementadas

### Core (Modelo)
- Inicialización del tablero con posiciones estándar
- Movimiento de fichas con validación completa
- Sistema de dados con dobles
- Captura de fichas (envío al banco)
- Reingreso de fichas desde el banco
- Retiro de fichas del tablero
- Detección de ganador
- Cálculo de movimientos posibles

### CLI
- Interfaz de texto completamente funcional
- Visualización ASCII del tablero
- Manejo de errores con mensajes claros
- Opciones de juego (mover, rendirse, salir)

### Pygame UI
- Tablero gráfico con diseño profesional
- Visualización de fichas en tiempo real
- Indicador visual de movimientos posibles (verde)
- Resaltado de selección (amarillo)
- Banco para fichas capturadas
- Zona de fichas retiradas
- Botón para tirar dados
- Mensajes de estado en pantalla
- Pantalla de ganador

## Testing

### Cobertura de Tests
- **Core**: 100% de cobertura en clases principales
- **CLI**: Tests de integración con mocks
- **Estrategia**: Unit tests + Integration tests

**Justificación**: Alta cobertura de tests asegura la correctitud de la lógica del juego y previene regresiones.

## Mejoras Futuras Posibles

1. **IA para jugar contra la computadora**
   - Algoritmo minimax para decisiones inteligentes
   
2. **Modo en red (multiplayer online)**
   - Socket.io para comunicación en tiempo real
   
3. **Sistema de puntuación y estadísticas**
   - Guardar historial de partidas
   
4. **Animaciones suaves**
   - Transiciones al mover fichas
   
5. **Sonidos y música**
   - Efectos de audio para eventos del juego

## Conclusiones

El proyecto cumple exitosamente con los objetivos planteados:

1. Implementación completa de las reglas del Backgammon
2. Arquitectura modular y mantenible
3. Alta cobertura de tests
4. Dos interfaces funcionales (CLI y GUI)
5. Código limpio y bien documentado

La separación clara entre modelo, vista y controlador permite que el proyecto sea extensible y fácil de mantener a largo plazo.
