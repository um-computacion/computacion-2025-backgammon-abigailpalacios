# Promps Documentacion

**Herramienta utilizada:**
- Chat GPT (GPT-5)

**Texto exacto del Prompt:**
- "como debe ser el changelog, que estructura debe tener y que debe contener"


**Respuesta de la IA:**

Un **changelog** es un documento donde vas registrando los cambios que le vas haciendo a tu proyecto de software. Su función es dejar claro **qué se agregó, qué se corrigió, qué se quitó o qué se modificó**, versión por versión.

---

### 📌 Estructura típica de un CHANGELOG

1. **Título y breve introducción**
   Ejemplo:

   ```markdown
   # Changelog
   Todos los cambios notables de este proyecto se documentarán en este archivo.
   ```

2. **Formato de versiones**

   * Lo habitual es usar [SemVer](https://semver.org/) → **Mayor.Menor.Parche** (ej: `1.2.3`).
   * Cada versión lleva **fecha de publicación**.

   Ejemplo:

   ```markdown
   ## [1.0.0] - 2025-09-01
   ```

3. **Secciones por tipo de cambio**
   Generalmente se siguen estas categorías:

   * **Added** → cosas nuevas (features, funciones, endpoints, tests, etc.)
   * **Changed** → cambios en funciones existentes.
   * **Deprecated** → avisos de cosas que en el futuro se van a eliminar.
   * **Removed** → lo que ya se eliminó.
   * **Fixed** → bugs corregidos.
   * **Security** → cuestiones de seguridad.

   Ejemplo:

   ```markdown
   ### Added
   - Función `mover_ficha` validando posiciones de origen y destino.
   - Nuevos tests unitarios para `devolver_ficha_comida`.

   ### Fixed
   - Error al intentar mover fichas desde posiciones vacías.
   ```

4. **Historial cronológico**
   Lo más reciente arriba, lo más antiguo abajo.

   Ejemplo:

   ```markdown
   ## [1.0.1] - 2025-09-02
   ### Fixed
   - Corrección de bug en validación de movimientos (no permitía mover sobre posición con 1 ficha del oponente).

   ## [1.0.0] - 2025-08-30
   ### Added
   - Implementación inicial de `Board`.
   - Tests de inicialización y movimiento.
   ```

---

### 📋 En tu caso (backgammon)

Tu `CHANGELOG.md` debería tener:

* Registro de cuando creaste `Board` e inicializaste posiciones.
* Registro de cuando añadiste validaciones de movimiento.
* Registro de cuando agregaste el banco de fichas y funciones `ficha_comida`, `devolver_ficha_comida`.
* Registro de las correcciones de tests (cuando pasaste de 91% a 97% y ahora a 100%).

---

¿Querés que te arme un **ejemplo concreto de changelog para tu proyecto** con lo que ya hiciste hasta ahora (creación del tablero, tests iniciales, corrección de bugs y aumento de coverage)?

**Uso:**
- Utilizada con modificaciones: use la estructura pero agregue y modifique informacion

**Referencia:**
* `CHANGELOG.md`

---

**Texto exacto del Prompt:**
- "como deberia quedar un readme correcto y bien prolijo y lindo"

**Respuesta de la IA:**

Un buen **README.md** es como la “cara visible” de tu proyecto: explica qué es, cómo usarlo, cómo instalarlo y qué tiene adentro. Lo ideal es que sea **claro, ordenado y visualmente atractivo**.

---

### 📋 Estructura recomendada de un README

````markdown
# 🎲 Backgammon en Python

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-100%25-blue)

## 📖 Descripción
Este proyecto implementa una versión simplificada del **Backgammon** en Python.  
Incluye las clases `Board`, `Player` y `Dice`, junto con una suite completa de tests unitarios.

El objetivo es practicar:
- Programación orientada a objetos (POO).
- Validación de reglas de juego.
- Cobertura de tests con `unittest` y `coverage`.

---

## 🚀 Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/usuario/backgammon.git
   cd backgammon
````

2. Crear un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate   # en Linux/Mac
   venv\Scripts\activate      # en Windows
   ```

3. Instalar dependencias:

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Uso

Ejecutar los tests:

```bash
pytest --maxfail=1 --disable-warnings -q
```

O con `unittest`:

```bash
python -m unittest discover
```

Ejecutar reporte de cobertura:

```bash
coverage run -m unittest discover
coverage report
coverage html
```

Abrir `htmlcov/index.html` en el navegador para ver el reporte gráfico.

---

## 📂 Estructura del proyecto

```
backgammon/
│
├── core/
│   ├── __init__.py
│   ├── board.py       # Clase Board: tablero, movimientos y reglas
│   ├── player.py      # Clase Player: jugadores y fichas
│   └── dice.py        # Clase Dice: tiradas y movimientos
│
├── tests/
│   ├── __init__.py
│   └── test_board.py  # Tests unitarios
│
├── README.md
├── CHANGELOG.md
└── requirements.txt
```

---

## 🧪 Cobertura de tests

Actualmente el proyecto cuenta con **100% de cobertura** en `core/board.py` y tests automatizados para todas las clases.

---

## 📌 Roadmap

* [ ] Implementar interfaz gráfica simple con `tkinter`.
* [ ] Simulación de partidas completas.
* [ ] Integración con bots de estrategia.

---

## 🤝 Contribuciones

¡Contribuciones son bienvenidas!
Por favor, abre un **issue** o un **pull request** con tus sugerencias.

---

## 📜 Licencia

Este proyecto está bajo la licencia MIT.
Consulta el archivo [LICENSE](LICENSE) para más información.

```

---

### 🔑 Claves para un README “lindo”:
- **Títulos claros y emojis** para hacerlo más visual.  
- **Badges** (build, coverage, version) para mostrar estado del proyecto.  
- **Código en bloques** para instalación y uso.  
- **Estructura de carpetas** para guiar al lector.  
- **Roadmap** para mostrar hacia dónde va el proyecto.  

---

👉 ¿Querés que te lo prepare ya completo con **los datos de tu proyecto actual** (nombre, tests, coverage, clases `Board`, `Player`, `Dice`), listo para que lo copies y pegues?
```
**Uso:**
- Utilizada con modificaciones: use la estructura pero agregue y modifique informacion

**Referencia:**
* `README.md`

**Texto exacto del Prompt:**
- "dime como debo hacer los promps, que estructura deben tener, que deben contener, teniendo en cuenta que los promps son: desarrollo, testing y documentacion"

**Respuesta de la IA:**

Genial 🙌. En el PDF de la materia se aclara que debés entregar **prompts exactos** que usaste para el proyecto, separados en tres archivos:

* `prompts-desarrollo.md`
* `prompts-testing.md`
* `prompts-documentacion.md`

Y cada uno tiene que seguir una **estructura mínima**:

---

### 📌 Estructura que deben tener

Para **cada prompt** guardado en esos archivos tenés que incluir:

1. **Modelo / herramienta usada**
   Ejemplo: *ChatGPT (GPT-5, agosto 2025)*

2. **Texto exacto del prompt**
   → Lo que vos escribiste (sin reescrituras ni resúmenes).

3. **Instrucciones del sistema** (si hubo)
   Ejemplo: *“Compórtate como abogado experto en normas legales…”*.

4. **Respuesta completa devuelta por la IA**
   → Copiarla tal cual, o si la modificaste, poner qué cambiaste.

5. **Indicar uso**

   * *Usada sin cambios*
   * *Usada con modificaciones (mostrar diferencias)*
   * *Descartada (explicar por qué)*

6. **Referencia**
   → A qué archivo(s) del proyecto se aplicó. Ejemplo: `core/board.py`, `tests/test_board.py`.


```

#### 🟢 `prompts-documentacion.md`

```markdown
## Prompt 2

**Modelo / herramienta usada:** ChatGPT (GPT-5, agosto 2025)  

**Texto exacto del prompt:**  
> dime como debo hacer los promps, que estructura deben tener, que deben contener, teniendo en cuenta que los promps son: desarrollo, testing y documentacion  

**Instrucciones del sistema:**  
_No hubo._  

**Respuesta devuelta por la IA:**  
(explicación de estructura de prompts, puntos a incluir, ejemplos).  

**Uso:** Usada sin cambios.  

**Referencia:** prompts-desarrollo.md, prompts-testing.md, prompts-documentacion.md
```

---

👉 Con esto tenés un esquema uniforme y cumplís con el requisito de la materia.

¿Querés que te arme directamente los **tres archivos `.md`** (`prompts-desarrollo.md`, `prompts-testing.md` y `prompts-documentacion.md`) con algunos de tus prompts reales ya volcados, para que solo los completes con más casos?

**Referencia:**
* `prompts-desarrollo.md`, `prompts-testing.md` y `prompts-documentacion.md`