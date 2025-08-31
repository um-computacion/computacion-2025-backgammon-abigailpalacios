# 🎲 Backgammon

**Alumno: Palacios Abigail**
**Carrera: Ingenieria en Informatica**
**Ciclo lectivo: 2025**

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-100%25-blue)

---

##  Descripción
En este proyecto realizaremos una version del juego **Backgammon**

Clases principales:
- `Board`: tablero, reglas de movimiento, banco de fichas y validaciones
- `Player`: representa a los jugadores con su nombre y ficha
- `Dice`: representa la tirada de dados y posibles movimientos
- `Checker`: gestiona piezas y su interacción en el tablero.
- `Game`: coordina la lógica de una partida.

Además incluye:
- `cli/`: interfaz por línea de comandos.
- `pygame_ui/`: base para interfaz gráfica con **pygame**.
- `tests/` : tests unitarios para cada módulo.



##  Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/usuario/backgammon.git
   cd backgammon

2. Crear un entorno virtual:
    python -m venv venv
    source venv/bin/activate   (Linux/Mac)
    venv\Scripts\activate      (Windows)

3. Instalar dependencias:
    pip install -r requirements.txt

## Uso

- Ejecutar los test con unittest:
    python -m unittest discover

- Reporte de cobertura:
    coverage run -m unittest discover
    coverage report
    coverage html

## Estructura del Proyecto

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
