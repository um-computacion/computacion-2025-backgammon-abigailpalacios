# Prompts Documentacion

## Prompt 1

**Herramienta utilizada:**
- ChatGPT (GPT-4)

**Texto exacto del Prompt:**
```
como debe ser el changelog, que estructura debe tener y que debe contener
```

**Respuesta de la IA:**
Un **changelog** es un documento donde vas registrando los cambios que le vas haciendo a tu proyecto de software. Su función es dejar claro **qué se agregó, qué se corrigió, qué se quitó o qué se modificó**, versión por versión.

Estructura típica:
1. Título y breve introducción
2. Formato de versiones (SemVer)
3. Secciones por tipo de cambio (Added, Changed, Fixed, Removed)
4. Historial cronológico (más reciente arriba)

**Uso:**
- Usada con modificaciones: Adapté la estructura pero agregué secciones específicas del proyecto

**Referencia:**
* `CHANGELOG.md`

---

## Prompt 2

**Herramienta utilizada:**
- ChatGPT (GPT-4)

**Texto exacto del Prompt:**
```
como deberia quedar un readme correcto y bien prolijo y lindo
```

**Respuesta de la IA:**
Un buen README.md debe incluir:
- Título con badges
- Descripción clara del proyecto
- Instrucciones de instalación
- Guía de uso
- Estructura del proyecto
- Información de tests y cobertura
- Roadmap
- Contribuciones y licencia

**Uso:**
- Usada con modificaciones: Usé la estructura pero personalicé contenido

**Referencia:**
* `README.md`

---

## Prompt 3

**Herramienta utilizada:**
- GitHub Copilot

**Texto exacto del Prompt:**
```
necesito agregar docstrings a todas mis clases y funciones en español sin acentos
```

**Respuesta de la IA:**
```python
def metodo_ejemplo(self, param1, param2):
    """Descripcion breve del metodo.
    
    Args:
        param1: Descripcion del parametro 1
        param2: Descripcion del parametro 2
    
    Returns:
        Descripcion del valor de retorno
    """
    pass
```

**Uso:**
- Usada con modificaciones: Simplifiqué los docstrings a una sola línea

**Referencia:**
* Todos los archivos `.py` del proyecto

---

## Prompt 4

**Herramienta utilizada:**
- ChatGPT (GPT-4)

**Texto exacto del Prompt:**
```
como documento la arquitectura MVC de mi proyecto pygame para la justificacion
```

**Respuesta de la IA:**
Para documentar arquitectura MVC:
1. Explica qué es el patrón MVC
2. Identifica cada componente en tu proyecto:
   - Modelo: core/
   - Vista: pygame_ui/iboard.py, cli/
   - Controlador: pygame_ui/events.py
3. Justifica por qué elegiste esta arquitectura
4. Muestra diagrama o estructura de carpetas

**Uso:**
- Usada sin cambios

**Referencia:**
* `JUSTIFICACION.md` - sección "Patrón de Diseño: MVC"

---

## Prompt 5

**Herramienta utilizada:**
- GitHub Copilot

**Texto exacto del Prompt:**
```
que tecnologias y versiones debo listar en el archivo de justificacion
```

**Respuesta de la IA:**
Debes listar:
- Python y su versión
- Librerías principales (pygame, tkinter)
- Frameworks de testing (unittest, coverage)
- Herramientas de linting (pylint)
- Cada una con justificación de por qué la elegiste

**Uso:**
- Usada sin cambios

**Referencia:**
* `JUSTIFICACION.md` - sección "Tecnologías Utilizadas"

---

## Prompt 6

**Herramienta utilizada:**
- ChatGPT (GPT-4)

**Texto exacto del Prompt:**
```
dime como debo hacer los prompts, que estructura deben tener
```

**Respuesta de la IA:**
Para cada prompt incluir:
1. Modelo/herramienta usada
2. Texto exacto del prompt
3. Instrucciones del sistema (si hubo)
4. Respuesta completa de la IA
5. Indicar uso (sin cambios, modificada, descartada)
6. Referencia a archivos

**Uso:**
- Usada sin cambios

**Referencia:**
* `prompts-desarrollo.md`, `prompts-testing.md`, `prompts-documentacion.md`

---

## Prompt 7

**Herramienta utilizada:**
- GitHub Copilot

**Texto exacto del Prompt:**
```
como explico las decisiones de diseño del sistema de coordenadas del tablero 0-23
```

**Respuesta de la IA:**
Explica:
1. Por qué elegiste índices 0-23
2. Dirección de movimiento de cada color
3. Ventajas sobre otras representaciones
4. Cómo facilita cálculos de distancia
5. Incluye ejemplo de código

**Uso:**
- Usada sin cambios

**Referencia:**
* `JUSTIFICACION.md` - sección "Sistema de Coordenadas del Tablero"

---

## Prompt 8

**Herramienta utilizada:**
- ChatGPT (GPT-4)

**Texto exacto del Prompt:**
```
que caracteristicas implementadas debo listar en la justificacion
```

**Respuesta de la IA:**
Lista características por componente:
- Core: reglas, validaciones, dados, banco, retiro
- CLI: interfaz texto, visualización, opciones
- Pygame UI: tablero gráfico, fichas, interacción, resaltados
Marca cada una con check o X según esté implementada

**Uso:**
- Usada con modificaciones: Agregué más detalles específicos

**Referencia:**
* `JUSTIFICACION.md` - sección "Características Implementadas"

---

## Prompt 9

**Herramienta utilizada:**
- GitHub Copilot

**Texto exacto del Prompt:**
```
como documento las excepciones personalizadas y su proposito
```

**Respuesta de la IA:**
Para cada excepción documenta:
- Nombre de la clase
- Cuándo se lanza
- Qué error representa
- Ejemplo de uso
- Justificación de por qué existe

**Uso:**
- Usada sin cambios

**Referencia:**
* `JUSTIFICACION.md` - sección "Manejo de Excepciones Personalizadas"
* `core/exceptions.py`

---

## Prompt 10

**Herramienta utilizada:**
- ChatGPT (GPT-4)

**Texto exacto del Prompt:**
```
que mejoras futuras deberia incluir en la justificacion para mostrar vision del proyecto
```

**Respuesta de la IA:**
Incluye mejoras como:
- IA para jugar contra computadora
- Modo multijugador en red
- Sistema de puntuación
- Animaciones
- Sonidos y música
- Diferentes niveles de dificultad
- Guardado de partidas

**Uso:**
- Usada con modificaciones: Seleccioné solo las más relevantes

**Referencia:**
* `JUSTIFICACION.md` - sección "Mejoras Futuras Posibles"

---

## Prompt 11

**Herramienta utilizada:**
- GitHub Copilot

**Texto exacto del Prompt:**
```
como justifico la eleccion de unittest sobre pytest para el proyecto
```

**Respuesta de la IA:**
Justificaciones válidas:
- Unittest es estándar de Python (incluido por defecto)
- No requiere instalación adicional
- Buena integración con coverage
- Sintaxis más verbosa pero clara
- Ideal para proyectos educativos

**Uso:**
- Usada sin cambios

**Referencia:**
* `JUSTIFICACION.md` - sección "Tecnologías Utilizadas > Unittest"

---

## Prompt 12

**Herramienta utilizada:**
- ChatGPT (GPT-4)

**Texto exacto del Prompt:**
```
como documento la estrategia de testing del proyecto con unit tests e integration tests
```

**Respuesta de la IA:**
Documenta:
1. Tipos de tests implementados
2. Cobertura de código alcanzada
3. Herramientas usadas (unittest, coverage, mocks)
4. Estrategia de mocking para CLI
5. Por qué no tests end-to-end de pygame
6. Justificación de la estrategia elegida

**Uso:**
- Usada sin cambios

**Referencia:**
* `JUSTIFICACION.md` - sección "Testing"

---

## Prompt 13 (DESCARTADO)

**Herramienta utilizada:**
- ChatGPT (GPT-4)

**Texto exacto del Prompt:**
```
deberia incluir diagramas UML en la justificacion del proyecto
```

**Respuesta de la IA:**
Los diagramas UML pueden incluir:
- Diagrama de clases mostrando relaciones
- Diagrama de secuencia para flujo de juego
- Diagrama de componentes para arquitectura
Se pueden crear con PlantUML o draw.io

**Uso:**
- Descartada: Decidimos que para un proyecto educativo la descripción textual y estructura de carpetas es suficiente

**Referencia:**
* Ninguna (no implementado)