## Prompt Testing

**Herramienta usada:** ChatGPT (GPT-5)

**Texto exacto del prompt:**  
* "que tests tengo que agregar para aumentar el coverage"


**Respuesta devuelta por la IA:**  

Te faltan dos cosas súper concretas para que **Dice** llegue al 100%:

1. **Ejecutar la rama “doble” de `tirar()`** (ahora nunca se cubre).
2. **Ignorar el bloque `if __name__ == '__main__'`** en el test (coverage lo cuenta como “miss”).

Haz esto:

### A) Test simple (tu mismo estilo) que fuerza que alguna tirada sea doble

```python
def test_tirar_alguna_vez_doble(self):
    d = Dice()
    doble = False
    # repetimos varias veces hasta que salga un doble
    for _ in range(120):   # suficiente para que aparezca al menos 1 doble
        d.tirar()
        m = d.get_movimiento()
        if len(m) == 4 and m[0] == m[1] == m[2] == m[3]:
            doble = True
            break
    self.assertTrue(doble)
```

Esto hace que se ejecute **la rama del `if`** dentro de `tirar()` al menos una vez.

### B) Ignorar el “main” del test

En `tests/test_dice.py`, cambia la última línea por:

```python
if __name__ == '__main__':  # pragma: no cover
    unittest.main()
```

Con esos dos cambios deberías ver **100%** en `core/dice.py` y en `tests/test_dice.py`. Si prefieres no usar el bucle, dime y te doy otra variante igual de simple.
  

**Uso:** 
* Descartada: No utilice el test que la IA recomendo porque no comprendia la logica y ademas ya tenia un test de dados dobles

**Referencia:** 

* `test_board.py`.
