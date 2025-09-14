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

## 1.1.0 (Segundo Sprint)

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

### Fixed

- Habian lineas en las clases `Board` y `Dice` que no eran testeadas
- En el metodo `devolver_ficha_comida` no se respetaba que si se encontaba una sola ficha en cierta posicion, el oponene que se encontraba esperando a sacar la ficha del banco, podia comer a su rival 

### Removed

- Se elimino el metodo `distancia` que generaba redundancia y provocaba error en los test

## 1.0.0 (Primer Sprint)

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