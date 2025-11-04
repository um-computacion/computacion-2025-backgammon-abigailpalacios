# Prompts Testing

## Prompt 1

**Herramienta utilizada:**
- GitHub Copilot

**Texto exacto del Prompt:**
```
como testeo la interfaz CLI con mocks para simular inputs del usuario
```

**Respuesta de la IA:**
```python
from unittest.mock import patch, MagicMock
import io

@patch('builtins.input')
@patch('sys.stdout', new_callable=io.StringIO)
def test_cli(mock_stdout, mock_input):
    mock_input.side_effect = ["Dana", "Abi", "3"]
    main()
    output = mock_stdout.getvalue()
    assert "Bienvenido" in output
```

**Uso:**
- Usada sin cambios, base de los tests CLI

**Referencia:**
* `tests/test_cli.py`

---

## Prompt 2

**Herramienta utilizada:**
- ChatGPT (GPT-4)

**Texto exacto del Prompt:**
```
necesito mockear la clase Backgammongame completa para testear solo la logica CLI 
```

**Respuesta de la IA:**
```python
@patch('cli.cli.Backgammongame')
def test_cli_sin_juego(mock_game_class):
    mock_game_instance = MagicMock()
    mock_game_instance.game_over.return_value = True
    mock_game_instance.get_turno.return_value = mock_player
    mock_game_instance.get_dados.return_value = [5, 3]
    
    mock_game_class.return_value = mock_game_instance
    
    main()
    
    mock_game_class.assert_called_once()
```

**Uso:**
- Usada sin cambios

**Referencia:**
* `tests/test_cli.py` - todos los tests de CLI

---

## Prompt 3

**Herramienta utilizada:**
- GitHub Copilot

**Texto exacto del Prompt:**
```
como testeo que se muestran correctamente los movimientos posibles en la CLI
```

**Respuesta de la IA:**
```python
def test_mostrar_movimientos():
    mock_game.movimientos_posibles.return_value = {0: [3, 5], 1: [4]}
    mock_input.side_effect = ["Dana", "Abi", "3"]
    
    main()
    
    output = mock_stdout.getvalue()
    assert "Movimientos posibles:" in output
    assert "Desde posicion 1:" in output
```
**Uso:**
- Usada con modificaciones: Agregué verificación de formato de destinos

**Referencia:**
* `tests/test_cli.py` - `test_jugar_movimiento_y_rendirse`

---

## Prompt 4

**Herramienta utilizada:**
- ChatGPT (GPT-4)

**Texto exacto del Prompt:**
```
como verifico que el coverage de tests llegue al 100% en todas las clases del core
```

**Respuesta de la IA:**
```bash
coverage run -m unittest discover
coverage report -m
coverage html
```

**Instrucciones adicionales:**
```
# Para ver líneas no cubiertas:
coverage report --show-missing

# Para generar reporte XML (para CI/CD):
coverage xml -o cobertura.xml
```

**Uso:**
- Usada sin cambios

**Referencia:**
* `.github/workflows/ci.yml`
* Comando ejecutado localmente

---

## Prompt 5

**Herramienta utilizada:**
- GitHub Copilot

**Texto exacto del Prompt:**
```
como simulo que un jugador se rinde en medio de una partida en los tests CLI
```

**Respuesta de la IA:**
```python
def test_rendirse():
    mock_input.side_effect = ["Dana", "Abi", "2"]  # Opción 2 = Rendirse
    
    main()
    
    output = mock_stdout.getvalue()
    assert "se ha rendido" in output
    assert "¡Gracias por jugar!" in output
```
**Uso:**
- Usada con modificaciones: Agregué verificación del nombre del jugador que se rinde

**Referencia:**
* `tests/test_cli.py` - `test_jugar_movimiento_y_rendirse`

---

## Prompt 6

**Herramienta utilizada:**
- ChatGPT (GPT-4)

**Texto exacto del Prompt:**
```
necesito testear el caso donde no hay movimientos posibles y se pasa automaticamente el turno
```

**Respuesta de la IA:**
```python
def test_sin_movimientos():
    mock_game.movimientos_posibles.side_effect = [{}, {10: [11]}]
    mock_game.get_turno.side_effect = [player1, player2]
    
    main()
    
    output = mock_stdout.getvalue()
    assert "No hay movimientos posibles" in output
    mock_game.definir_turno.assert_called()
```
**Uso:**
- Usada sin cambios

**Referencia:**
* `tests/test_cli.py` - `test_sin_movimientos_posibles_pasa_turno`

---

## Prompt 7

**Herramienta utilizada:**
- GitHub Copilot

**Texto exacto del Prompt:**
```
como mockeo la funcion tirar_dados para que siempre retorne valores especificos en los tests
```

**Respuesta de la IA:**
```python
mock_game.tirar_dados.return_value = [5, 3]
mock_game.get_dados.return_value = [5, 3]

# O con side_effect para diferentes llamadas:
mock_game.get_dados.side_effect = [[5, 3], [5, 3], [5]]
```
**Uso:**
- Usada sin cambios

**Referencia:**
* `tests/test_cli.py` - todos los tests

---

## Prompt 8

**Herramienta utilizada:**
- ChatGPT (GPT-4)

**Texto exacto del Prompt:**
```
como verifico que se llama correctamente al metodo mover_ficha con los parametros esperados
```

**Respuesta de la IA:**
```python
# Después de simular movimiento
mock_game.mover_ficha.assert_called_with(0, 3)

# O verificar que se llamó al menos una vez
mock_game.mover_ficha.assert_called()

# O contar llamadas
assert mock_game.mover_ficha.call_count == 1
```
**Uso:**
- Usada sin cambios

**Referencia:**
* `tests/test_cli.py` - `test_jugar_movimiento_y_rendirse`

---

## Prompt 9

**Herramienta utilizada:**
- GitHub Copilot

**Texto exacto del Prompt:**
```
como testeo que el tablero se imprime correctamente en la consola con el formato esperado
```

**Respuesta de la IA:**
```python
def test_imprimir_tablero():
    mock_input.side_effect = ["Dana", "Abi", "3"]
    
    main()
    
    output = mock_stdout.getvalue()
    assert "ESTADO DEL TABLERO" in output
    assert "13 14 15 16 17 18" in output
    assert "BARRA / BANCO" in output
```
**Uso:**
- Usada sin cambios

**Referencia:**
* `tests/test_cli.py` - `test_iniciar_juego_y_salir`

---

## Prompt 10

**Herramienta utilizada:**
- ChatGPT (GPT-4)

**Texto exacto del Prompt:**
```
como hago que los mocks de jugadores devuelvan nombres especificos para testear mensajes personalizados
```

**Respuesta de la IA:**
```python
mock_player1 = MagicMock(spec=Player)
mock_player1.get_nombre.return_value = "Dana"
mock_player1.get_ficha.return_value = "Blancas"

mock_player2 = MagicMock(spec=Player)
mock_player2.get_nombre.return_value = "Abi"
mock_player2.get_ficha.return_value = "Negras"
```
**Uso:**
- Usada sin cambios

**Referencia:**
* `tests/test_cli.py` - método `setUp`

---

## Prompt 11

**Herramienta utilizada:**
- GitHub Copilot

**Texto exacto del Prompt:**
```
como simulo multiples turnos con diferentes jugadores en un solo test
```

**Respuesta de la IA:**
```python
mock_game.get_turno.side_effect = [player1, player1, player2]
mock_game.game_over.side_effect = [False, False, False, True]

# Cada llamada retorna el siguiente elemento
```
**Uso:**
- Usada sin cambios

**Referencia:**
* `tests/test_cli.py` - `test_sin_movimientos_posibles_pasa_turno`

---

## Prompt 12 (DESCARTADO)

**Herramienta utilizada:**
- ChatGPT (GPT-4)

**Texto exacto del Prompt:**
```
necesito tests de integracion que ejecuten pygame completo sin mocks
```

**Respuesta de la IA:**
```python
def test_pygame_integration():
    pygame.init()
    screen = pygame.display.set_mode((1400, 700))
    # Simular eventos reales de pygame
    event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': (700, 350)})
    pygame.event.post(event)
    # Ejecutar loop
```
**Uso:**
- Descartada: Los tests de pygame requieren display real, optamos por tests unitarios con mocks

**Referencia:**
* Ninguna (no implementado)