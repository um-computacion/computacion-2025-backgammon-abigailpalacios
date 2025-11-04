# 🎲 Backgammon

**Alumno: Palacios Abigail**  
**Carrera: Ingenieria en Informatica**  
**Ciclo lectivo: 2025**

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-100%25-blue)
![Python](https://img.shields.io/badge/python-3.13-blue)
![Pygame](https://img.shields.io/badge/pygame-2.6.1-green)

---

##  Descripción

Este proyecto implementa una version completa del juego **Backgammon** en Python con dos interfaces:
- **CLI**: Interfaz de linea de comandos para jugar en la terminal
- **GUI**: Interfaz grafica interactiva desarrollada con Pygame

### Clases principales (core/)

- `Backgammongame`: Orquesta el juego completo, turnos y reglas
- `Board`: Gestiona el tablero, movimientos y validaciones
- `Player`: Representa a los jugadores con nombre y color de ficha
- `Dice`: Maneja el lanzamiento de dados y movimientos disponibles
- `Checker`: Representa fichas individuales del juego
- `Exceptions`: Excepciones personalizadas para manejo de errores

### Interfaces

- **CLI** (`cli/`): Interfaz de texto con visualizacion ASCII del tablero
- **Pygame UI** (`pygame_ui/`): 
  - `iboard.py`: Renderizado visual del tablero
  - `events.py`: Manejo de eventos y logica de interaccion
  - `main.py`: Inicializacion y loop principal

---

## 🚀 Instalación

### Opción 1: Instalación local

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/um-computacion-tm/2025-2c-backgammon-abigailpalacios.git
   cd computacion-2025-backgammon-abigailpalacios
   ```

2. **Crear un entorno virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

### Opción 2: Usando Docker

1. **Construir la imagen:**
   ```bash
   docker-compose build
   ```

2. **Ejecutar tests:**
   ```bash
   docker-compose run backgammon-test
   ```

3. **Generar reporte de cobertura:**
   ```bash
   docker-compose run backgammon-coverage
   ```

4. **Ejecutar pylint:**
   ```bash
   docker-compose run backgammon-pylint
   ```

5. **Jugar en CLI:**
   ```bash
   docker-compose run backgammon-cli
   ```

---

##  Estructura del Proyecto
````markdown
backgammon/
│
├── assets/               
├── cli/
│   └── cli.py            
│
├── core/
│   ├── __init__.py
│   ├── board.py         
│   ├── checker.py    
│   ├── dice.py          
│   ├── exceptions.py     
│   ├── game.py          
│   └── player.py  
│
├── prompts/            
│   ├── prompts-desarrollo.md
│   ├── prompts-docs.md
│   └── prompts-testing.md
│
├── pygame_ui/          
│
├── tests/
│   ├── __init__.py
│   ├── test_board.py
│   ├── test_checker.py
│   ├── test_dice.py
│   ├── test_game.py
│   └── test_player.py
│
├── README.md
├── CHANGELOG.md
├── JUSTIFICACION.md
├── requirements.txt
└── .coverage
````
