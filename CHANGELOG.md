# CHANGELOG

En este archivo se guardaran todos los cambios realizados en el proyecto

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto se adhiere a [Semantic Versioning](https://semver.org/lang/es/).

# UNRELEASE

### Categorias

- Added: agregados en el documento
- Changed: cambios en el documento
- Removed: borrados en el documento
- Fixed: arreglos en el documento

## 1.6.0 (Sexto Sprint - Finalización)

### Added

- Se creó el archivo `pygame_ui/events.py` para separar la lógica de eventos de la interfaz gráfica
- Se implementó la clase `EventHandler` que maneja todos los eventos de pygame
- Se agregó la funcionalidad de resaltado visual de movimientos posibles en verde
- Se implementó la visualización de fichas retiradas en zonas específicas
- Se agregó contador visual de fichas retiradas (X/15)
- Se creó el archivo `pygame_ui/ichecker.py` con las clases `Ficha` y `GrupoFichas`
- Se implementó el método `reingreso_posible()` en `Backgammongame` para calcular posiciones válidas de reingreso
- Se agregó el método `estado_juego()` que retorna un diccionario completo con el estado del juego
- Se implementaron métodos auxiliares `mov_posible()` y `turno_completo()` en `Backgammongame`
- Se crearon tests completos para la CLI en `cli/test_cli.py`
- Se agregó la función `imprimir_tablero()` en CLI para visualización mejorada del tablero
- Se documentó la arquitectura del proyecto en `JUSTIFICACION.md`

### Changed

- Se refactorizó `pygame_ui/main.py` para usar la arquitectura MVC correctamente
- Se separó la lógica de renderizado en `iboard.py` (Vista) de la lógica de eventos (Controlador)
- Se mejoró la organización del código en `pygame_ui/` siguiendo el patrón MVC
- Se optimizó el método `movimientos_posibles()` para considerar el caso de retirar fichas
- Se actualizó la CLI para mostrar el tablero de forma más visual y clara
- Se mejoró el manejo de errores en CLI con mensajes más descriptivos
- Se refactorizó el código de la CLI para eliminar redundancias

### Fixed

- Se corrigió el error en `reingreso_posible()` que devolvía un diccionario con dado como clave en lugar de lista de destinos
- Se solucionaron problemas de imports relativos en `pygame_ui/`
- Se corrigió el cálculo de fichas retiradas para no contar las fichas en el banco
- Se arreglaron los tests de CLI para que pasen correctamente con la nueva implementación
- Se corrigió el método `retirar_ficha()` para manejar correctamente el caso de usar un dado mayor

### Removed

- Se removió código duplicado en la clase `Tablero` (antiguo board.py de pygame_ui)
- Se eliminaron métodos obsoletos que generaban redundancia

## 1.5.0 (Quinto Sprint)

### Added

- Se implementó la interfaz gráfica con Pygame en el directorio `pygame_ui/`
- Se creó la clase `Tablero` en `pygame_ui/board.py` para la visualización del tablero de Backgammon
- Se implementó el método `dibujar_triangulo()` para crear las puntas triangulares del tablero
- Se agregó el archivo `pygame_ui/main.py` con interfaz de entrada de jugadores usando Tkinter
- Se implementaron los 24 triángulos del tablero con colores alternados (claro y oscuro)
- Se añadió la barra central divisoria del tablero
- Se configuró el tamaño de pantalla optimizado para Backgammon (1200x600 píxeles)
- Se integró la lógica del juego desde `Backgammongame` con la interfaz pygame
- Se implementó la visualización dinámica de fichas según el estado del juego


### Changed

- Se ajustó el espaciado y posicionamiento de los triángulos para mayor precisión visual
- Se optimizaron los colores del tablero: beige claro para fondo, wheat para triángulos claros, y saddle brown para triángulos oscuros
- Se mejoró la altura de los triángulos (250 píxeles) para mejor proporción visual
- Se aumentó el tamaño de la ventana a 1400x700 píxeles para mejor visualización

### Fixed

- Se corrigió el posicionamiento de los triángulos para que queden correctamente alineados desde los bordes
- Se ajustó el cálculo del espacio disponible para evitar solapamientos entre triángulos

## 1.4.0 (Cuarto Sprint)

### Added

- Se implementó la interfaz CLI (Command Line Interface) en el archivo `cli/cli.py`
- Se agregó la función `main()` que permite jugar Backgammon desde la terminal
- Se implementaron excepciones personalizadas en el archivo `core/exceptions.py`
- Se agregaron las excepciones: `BackgammonException`, `MovimientoInvalido`, `SinMovimientos` y `GameOver`
- Se implementó el manejo de la opción de sacar fichas del tablero en la CLI
- Se agregó verificación de fin de partida después de cada movimiento

### Changed

- Se refactorizó el código CLI para seguir una lógica más clara y estructurada
- Se mejoró la visualización de movimientos posibles en la CLI
- Se implementó mejor flujo del juego con manejo de turnos y dados restantes

### Fixed

- Se corrigieron las excepciones duplicadas en el manejo de errores de la CLI
- Se eliminó código redundante en el manejo de excepciones
- Se arreglaron problemas en el flujo de turnos cuando no hay movimientos posibles
- Se corrigió la validación de movimientos posibles al inicio de cada turno


## 1.3.0 (Tercer Sprint)

### Added

- Se agrego el metodo `movimientos_posibles` en la clase `Backgammon`, que permite saber que movimiento le es posible cada ficha para mover
- Se actualizaron los prompts
- Se han agregado metodos con sus test, que ayudaran al cli 

### Fixed

- En el metodo  `movimientos_posibles` no se tenia en cuenta si la ficha salia del tablero 

## 1.2.0 (Segundo Sprint)

### Added

- Se agregaron test en la clase `Dice` vistos en clase para poder testear la herramienta `randint`
- Se agregaron test en la clase `Board` para aumentar el coverage
- Se comenzo a implementar la clase `Backgammon`, que relacionara todas las clases 
- Se agregaron test pra los metodos implementadas en `Backgammon`
- Se agregaron funciones y test en la clase `Backgammon`
- Se implemento el metodo `mover_ficha` en la clase `Backgammon`
- Se implemento el metodo `reingresar_ficha` en la clase `Backgammon`
- Se implemento el metodo `gaandor` en la clase `Backgammon`
- Se implemento el metodo `posicioines` en la clase `Backgammon`, para permitir retirar una ficha 
- Se implemento el metodo `retirar_ficha`, la cual saca definitivamente a una ficha del tablero

### Fixed

- Habian lineas en las clases `Board` y `Dice` que no eran testeadas
- En el metodo `devolver_ficha_comida` no se respetaba que si se encontaba una sola ficha en cierta posicion, el oponene que se encontraba esperando a sacar la ficha del banco, podia comer a su rival 
- Se corrigio el metodo `retirar_ficha`, que solo verificaba que una ficha podia ser retirada si el dado coincidia exactamente con la distancia que le faltaba a la ficha para salir

### Removed

- Se elimino el metodo `distancia` que generaba redundancia y provocaba error en los test

## 1.1.0 (Primer Sprint)

### Added

- Creacion de las carpetas y sus archivos

- **Clase 'Player' y sus test:**
    - Estructura principal con el nombre y sus fichas
    - metodo `get_nombre`, que me devolvera el nombre del jugador
    - metodo `get_ficha`, que me devolvera la ficha del jugador

- **Clase 'Dice' y sus test:**
    - Estructura principal con dado 1 y 2
    - Metodo `movimiento` que esta definido como una lista que guardara los valores de los dados
    - Metodo `tirar`, que nos devuelve un numero cualquiera entre 1 y 6
    - En el metodo `tirar` tenemos dos caminos posibles, que ambos dados sean iguales, el cual nos devuelve 4 valores o que sean distintos donde solo nos devuelve dos valores

- **Clase 'Board' y sus test:**
    - Estructura principal que es una lista con 24 posiciones vacias
    - Metodo `inicializar` donde definimos la posicion inicial de las fichas
    - Metodo `banco` donde definimos las fichas comidas
    - Metodo `distancia` donde definimos como se moveran las fichas en el tablero
    - Metodo `validar_movimiento` donde definimos de que manera se pueden mover las fichas en el tablero
    - Metodo `ficha_comida` donde definimos cuando una ficha puede comer otra
    - Metodo `devolver_ficha` donde definimos si podemos devolver la ficha al tablero
    - Metodo `mover_ficha` donde definimos el movimiento de las fichas en el tablero
    - Metodo `sin_fichas` donde nos devuel que ficha ya no se encuentra en el tablero

- **Clase 'Checker' y sus test**
    - Estructura principal con la ficha y posicion de cada una
    - Metodo `get_movimiento` que me dira donde esta la ficha
    - Metodo `en_banco` que define si la ficha esta en el banco (True) o no (False)
    - Metodo `ficha_afuera` que me define si la ficha se encuentra todavia participando en el juego o no
    - Metodo `__str__` que me devuelve una string con la ficha en particular y su posicion

- Cada una de las clases cuentan con sus test

### Fixed

- Corrección en los métodos `validar_movimiento` y `mover_ficha` para contemplar casos inválidos de destino y origen.  
- Ajuste en `devolver_ficha_comida` para cubrir casos de fichas del mismo color y del color opuesto.  
- Agregados tests adicionales en la clase `Board` para incrementar la cobertura hasta 100%.

## 1.0.0 (Versión Inicial)

### Added

- Estructura inicial del proyecto
- Configuración de git y README básico
- Definición de requisitos del proyecto