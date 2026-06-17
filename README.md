# Sesión 2 y 3 : Funciones, Condicionales, Ciclos, Listas, Markdown

**Python Intermedio para Análisis de Datos — DIAN 2026**


## Objetivos de aprendizaje

Al finalizar esta sesión, serás capaz de:

1. Distinguir cuándo conviene trabajar con notebooks y cuándo con un proyecto estructurado en módulos.
2. Importar funciones desde módulos propios usando `from paquete.modulo import funcion`.
3. Implementar funciones que retornan valores y procedimientos que ejecutan acciones.
4. Usar condicionales simples, anidados y encadenados para tomar decisiones en el código.
5. Construir ciclos `for` con acumuladores y `while` con condición explícita.
6. Usar variables bandera para controlar la continuación de un ciclo.
7. Manipular listas y diccionarios para filtrar, agrupar y resumir datos.
8. Aplicar el flujo add → commit → push al finalizar cada sección.



## ¿Qué hay en este repositorio?

Este proyecto contiene los ejercicios de la Sesión 2 del curso.
Practicamos funciones con tipos simples, encadenamiento de funciones,
condicionales simples y anidados, ciclos `for` y `while`, listas y
diccionarios aplicados a datos tributarios de práctica.

```
repositorio_plantilla_sesion_02/
├── main.py              ← Punto de entrada. Ejecuta el menú interactivo.
├── requirements.txt     ← Dependencias del proyecto.
├── src/
│   ├── __init__.py
│   └── utils.py         ← Todas las funciones del proyecto.
└── data/
    ├── input/           ← Archivos de entrada (CSV, Excel). Vacío por ahora.
    └── output/          ← Resultados generados por el proyecto.
```



## Repaso flujo de trabajo con Git

```bash
# Ver el estado del repositorio
git status

# Agregar todos los cambios
git add .

# Hacer un commit con mensaje descriptivo
git commit -m "Sesión 2: funciones y condicionales implementados"

# Subir los cambios al repositorio remoto
git push
```
## Del notebook al proyecto: organización del código Python

### Cómo empieza un análisis

El punto de partida natural para explorar datos es un **notebook** (archivo `.ipynb`). Un notebook mezcla celdas de código con texto explicativo y muestra los resultados directamente debajo de cada celda. Esa inmediatez lo hace ideal para entender un conjunto de datos nuevo: ejecutas una celda, ves la salida, ajustas la siguiente y continúas.

```python
# En un notebook, explorar es rápido:
df.head()          # celda 1: ver las primeras filas
df.describe()      # celda 2: estadísticas básicas
df["valor"].plot() # celda 3: visualización rápida
```

Cada celda es un paso de exploración. El notebook guarda el estado de ejecución en memoria, así que puedes volver a una celda anterior, cambiar un parámetro y ver el efecto inmediatamente. Para probar hipótesis y documentar hallazgos durante el análisis, el notebook es difícil de superar.

---

### Cuándo el notebook empieza a quedar corto

El problema aparece cuando el análisis deja de ser exploratorio y se vuelve **repetible**. Imagina que el proceso que desarrollaste en el notebook: limpiar NITs, clasificar contribuyentes, calcular sanciones, necesita correr todos los meses con datos nuevos, o que otro miembro del equipo necesita usar las mismas funciones en su propio análisis.

En ese escenario el notebook presenta tres fricciones:

* La primera es el **orden de ejecución**. Un notebook funciona cuando las celdas se ejecutan en un orden específico. Si alguien abre el archivo y ejecuta las celdas en orden distinto, o si el kernel se reinicia, el resultado puede cambiar. El código depende del estado en memoria y no de lo que está escrito.

* La segunda es la **reutilización**. Una función definida en la celda 12 de un notebook no está disponible en otro notebook sin copiar y pegar. No hay forma de hacer `import notebook_analisis` y usar sus funciones directamente.

* La tercera es la **colaboración y revisión**. Los archivos `.ipynb` son JSON por dentro. Las diferencias en git muestran cambios en metadatos del notebook (número de ejecuciones, salidas guardadas) mezclados con cambios en el código, lo que hace las revisiones más difíciles de leer.



### La organización de un proyecto Python

Un proyecto con módulos separa el código en archivos con responsabilidades claras. En el repositorio del curso esa estructura es:

```
repositorio_plantilla_sesion_02/
├── main.py              ← punto de entrada
├── requirements.txt     ← dependencias
├── src/
│   ├── __init__.py      ← marca src como paquete
│   └── utils.py         ← funciones reutilizables
└── data/
    ├── input/           ← archivos de entrada
    └── output/          ← resultados generados
```

Cada pieza tiene un rol:

**`utils.py`** contiene las funciones del dominio: calcular IVA, validar NITs, clasificar contribuyentes. Son transformaciones que reciben datos, retornan resultados, no dependen de ningún estado externo. Esto las hace reutilizables porque cualquier archivo que haga `from src.utils import calcular_iva` puede usar esa función. Estas reglas *existen con independencia de cómo se presenten los resultados* si es un menú en la terminal, una hoja de cálculo o un informe generado automáticamente, la lógica de qué es "mora alta" no cambia. A ese conjunto de reglas propias del negocio se le llama *lógica de negocio o lógica del dominio*. Por eso las funciones de utils.py reciben datos y retornan resultados sin saber nada del contexto donde se usan.

**`main.py`** es el punto de entrada: orquesta las funciones, define el flujo del programa y presenta los resultados al usuario. No contiene lógica de negocio eso va en `utils.py`. `main.py` *usa* las funciones; `utils.py` las *define*. Si mañana reemplazas el menú por una API web, reescribes main.py y utils.py queda intacto.

**`data/`** separa el código de los datos. Los archivos en `data/input/` no forman parte del programa; son insumos que pueden cambiar sin tocar una sola línea de código.

---

### Importancia de la separación

* Cuando la lógica vive en `utils.py` y el flujo en `main.py`, puedes probar cada función de forma independiente. Si `clasificar_contribuyente(2_000_000)` retorna un resultado inesperado, abres `utils.py`, buscas la función y lees lo que hace. No necesitas re-ejecutar todo el notebook desde el inicio.

* El orden de ejecución deja de ser un problema. `main.py` define `main()` y la llama desde `if __name__ == "__main__"`. Cada vez que ejecutas `python main.py` el programa empieza desde cero, en el mismo estado, sin depender de lo que había en memoria de una ejecución anterior.

Git funciona mejor con archivos `.py`. Los diffs muestran qué líneas cambiaron en el código, sin el ruido de los metadatos del notebook. Un mensaje de commit como `"Sesión 2: validar_nit corregida para NITs de 10 dígitos"` describe un cambio puntual que fuede facilmente localizarse.


**`utils.py`** contiene las reglas del dominio tributario: cómo se calcula el IVA, qué hace que un NIT sea válido, a qué categoría pertenece un contribuyente según su valor declarado. Esas reglas existen con independencia de cómo se presenten los resultados — si es un menú en la terminal, una hoja de cálculo o un informe generado automáticamente, la lógica de qué es "mora alta" no cambia. A ese conjunto de reglas propias del negocio se le llama **lógica de negocio** o lógica del dominio. Por eso las funciones de `utils.py` reciben datos y retornan resultados sin saber nada del contexto donde se usan.

**`main.py`** hace algo diferente: toma esas reglas y decide cuándo aplicarlas, en qué orden y cómo mostrar los resultados al usuario. Sabe que hay un menú con nueve opciones; sabe que la opción `"3"` ejecuta los condicionales simples. Ese conocimiento es específico de este programa. `main.py` *usa* las funciones; `utils.py` las *define*. Si mañana reemplazas el menú por una API web, reescribes `main.py` y `utils.py` queda intacto.

---

### ¿Qué es el estado en programación?

> **Estado** es el conjunto de valores que están en memoria en un momento dado:
> el contenido de cada variable, el resultado de la última operación, los datos
> que se han cargado. El estado cambia a medida que el programa avanza.

#### El estado en un notebook

Cuando ejecutas una celda que define `declaraciones = [...]`, esa lista queda
en el kernel. La celda siguiente puede usarla, la de después también.

```python
# Celda 1
declaraciones = [...]   # ← queda en memoria del kernel

# Celda 2 — funciona porque Celda 1 ya corrió
total = len(declaraciones)
```

Pero si reinicias el kernel o ejecutas las celdas en otro orden, esa variable
ya no existe. El estado se perdió, y el resultado puede ser diferente.

#### Funciones sin estado externo

Una función que depende **solo de sus argumentos** y no lee ni modifica
variables externas se comporta siempre igual para los mismos datos de entrada.
Ese tipo de función se llama **pura**.

```python
calcular_iva(1_000_000, 0.19)  # → siempre 190000.0
```

No importa qué otras variables existan en memoria, en qué orden se llamaron
las funciones anteriores, ni cuántas veces se ejecutó el programa antes.

#### Las funciones de `utils.py` siguen ese patrón

| Función | Recibe | Retorna |
|---|---|---|
| `calcular_iva` | dos números | un número |
| `clasificar_contribuyente` | un número | una cadena |
| `validar_nit` | una cadena | un booleano |

Ninguna consulta variables globales ni modifica nada fuera de su cuerpo. Eso
es lo que las hace **portables**: puedes importarlas en un notebook, en
`main.py` o en cualquier otro script y su comportamiento no cambia.



### Los notebooks siguen teniendo su lugar

La organización en módulos complementa los notebooks.  Por ejemplo, en las sesiones siguientes, cuando incorporemos `pandas` y visualizaciones, usarás notebooks para explorar los datos del proyecto, probar transformaciones y documentar hallazgos. Una vez que una transformación queda estable y la quieres reutilizar, la extraes a `utils.py` y la importas desde el notebook igual que desde `main.py`:

```python
# Ejemplo de un notebook de análisis exploratorio:
from src.utils import calcular_estadisticas, filtrar_por_estado

activos = filtrar_por_estado(DECLARACIONES, "ACTIVO")
stats = calcular_estadisticas(activos)
```

Con el notebook es más fácil hacer las preguntas; pero el archivo con las funciones reutilizables guarda las respuestas que ya probaste y quieres conservar.

---

### Lo que esto significa para el repositorio del curso

En esta sesión el repositorio tiene una estructura tal que: trabajas en `utils.py` implementando las funciones, verificas en `main.py` que producen los resultados correctos, y haces commits que documentan tu avance. Al final `utils.py` de cada sesión es una biblioteca de funciones que podrías reutilizar en otro proyecto. La pregunta que guía la decisión de diseño es: ¿esta lógica pertenece a `utils.py` porque es una transformación reutilizable o a `main.py` porque es parte del flujo de un programa específico?


### ▶ Práctica guiada · ¿Qué tan fácil sería trabajar sobre este proyecto?

Antes de empezar a modificar nuestro propio repositorio, revisaremos dos proyectos públicos en GitHub que usan notebooks para análisis de datos. La intención es mirar los repositorios como lo haría una persona que llega por primera vez y necesita continuar el trabajo de alguien más.

Trabajen en parejas o grupos de tres. Abran los siguientes repositorios:

1. [Python Diwali Sales Analysis](https://github.com/Divyanshu-RS/Python_Diwali_Sales_Analysis)
2. [Beginner Data Analysis Project](https://github.com/punneko/beginner-data-analysis-project)

Durante 10 minutos exploren los dos repositorios sin ejecutar nada todavía. Revisen el README, los notebooks, los archivos de datos, las carpetas y los nombres de archivos. Imaginen que alguien les pide hacer una mejora pequeña, por ejemplo:

- agregar una nueva visualización;
- cambiar el archivo de entrada;
- corregir una transformación de datos;
- reutilizar una parte del código en otro proyecto.

Respondan estas preguntas para cada repositorio:

| Pregunta | Repo 1 | Repo 2 |
|---|---|---|
| ¿El README explica qué hace el proyecto? | | |
| ¿Se entiende por dónde empezar? | | |
| ¿Los datos de entrada están en una carpeta clara? | | |
| ¿Hay `requirements.txt` o instrucciones de instalación? | | |
| ¿El código parece fácil de reutilizar fuera del notebook? | | |
| ¿Se distingue qué parte carga, transforma y muestra datos? | | |
| ¿Qué sería difícil si tuvieran que hacer mantenimiento? | | |

Después de completar la tabla, asignen una calificación de 1 a 5 a cada repositorio:

| Calificación | Criterio |
|---|---|
| 1 | Sería difícil empezar. No queda claro qué abrir, qué instalar o qué ejecutar. |
| 2 | Se entiende la idea general, pero faltan instrucciones o hay archivos mezclados. |
| 3 | Se puede trabajar con esfuerzo. Hay partes claras y otras confusas. |
| 4 | Es fácil iniciar. La estructura ayuda a entender el proyecto. |
| 5 | Es muy fácil continuar el trabajo. Hay instrucciones, orden, nombres claros y separación entre entradas, código y salidas. |

#### Cierre de la práctica

Después de revisar los repositorios, vuelvan al repositorio del curso y observen su estructura:

```text
data/input/
data/output/
src/
main.py
requirements.txt
README.md
```

> Si una persona nueva llegara a tu proyecto dentro de tres meses, ¿qué necesitaría encontrar para empezar a trabajar sin pedirte explicaciones?

---
## 0. Configuración inicial

### Abrir el Codespace del proyecto

Tu repositorio de la sesión está en GitHub Classroom. Para abrirlo en
Codespaces:

1. Ve a [github.com](https://github.com) e inicia sesión.
2. Abre el repositorio que te asignó el instructor. El nombre empieza con
   `sesion-02-`.
3. Haz clic en el botón verde **Code**, luego en la pestaña **Codespaces**.
4. Haz clic en **Create codespace on main**.

GitHub abrirá un VS Code en el navegador conectado a una máquina virtual con
Ubuntu 24.04 y Python 3.12 ya instalados. La primera vez puede tomar hasta
un minuto mientras se prepara el entorno.

> Si ya creaste un Codespace en una sesión anterior y aparece en la lista,
> haz clic en los tres puntos (`…`) junto a su nombre y selecciona **Open in
> browser** para retomarlo. No crees uno nuevo si ya tienes uno activo.

---

### Instalar las extensiones de Python

La primera vez que abras el Codespace, VS Code puede no tener las extensiones
de Python activas. Para instalarlas:

1. Haz clic en el ícono de extensiones en la barra lateral izquierda
   (cuatro cuadrados) o presiona `Ctrl+Shift+X`.
2. Busca **Python** e instala la extensión de **Microsoft** (la que tiene
   el símbolo de verificación azul).
3. Busca **Pylance** e instálala también. Pylance activa el autocompletado
   inteligente y el subrayado de errores mientras escribes.

Cuando VS Code detecte que el repositorio tiene archivos `.py`, puede
mostrarte una notificación en la esquina inferior derecha sugiriendo instalar
las extensiones automáticamente. Si aparece, acepta.

> **Verificación:** abre `src/utils.py`. Si el nombre de las funciones
> aparece con color de sintaxis y al pasar el cursor sobre una función ves
> su docstring, las extensiones están activas.

---

### Verificar que el proyecto corre

Abre la terminal integrada de VS Code con `` Ctrl+` `` y ejecuta:

```bash
python main.py
```

El menú aparece con nueve opciones. Por ahora todas muestran su encabezado
pero no producen salida, porque los cuerpos están comentados. Eso es lo
esperado.

---

## Python como lenguaje

### Un lenguaje interpretado

Python es un lenguaje **interpretado**: el código se ejecuta línea por línea, en tiempo real, sin necesidad de compilarlo primero. Eso tiene como consecuencia que los errores aparecen exactamente en la línea que falla, puedes probar fragmentos directamente en el intérprete interactivo, y el ciclo de prueba es rápido.

Abre el intérprete:

```bash
python
```

El prompt `>>>` indica que Python está esperando instrucciones. Escribe esto:

```python
2 + 2
```

Responde `4` inmediatamente. Ahora escribe:

```python
mensaje = "Procesamiento de datos"
print(mensaje.upper())
```

Sale `PROCESAMIENTO DE DATOS`. El intérprete ejecutó esas dos líneas en el momento. No hubo pasos intermedios.

Sal con `exit()`.

### Reglas de sintaxis a recordar

**Indentación obligatoria.** Python usa el tab para definir bloques de código. No existen llaves `{}` ni palabras clave `begin/end`. Usar 4 espacios es el estándar; usar 3 o 2 también funciona, pero mezclar tamaños en el mismo archivo produce un error.

```python
# Correcto
def saludar(nombre):
    mensaje = f"Hola, {nombre}"
    return mensaje

# Error: IndentationError
def saludar(nombre):
mensaje = f"Hola, {nombre}"  ← sin sangrado → falla
```

**Dos puntos al final de estructuras de bloque.** Todo `def`, `if`, `for`, `while` y `else` termina en `:`.

```python
def calcular(valor):        # ← dos puntos
    if valor > 0:           # ← dos puntos
        return "positivo"   # ← sangrado de 4 espacios
```

**Mayúsculas y minúsculas son distintas.** `nit`, `NIT` y `Nit` son tres variables diferentes. Por convención, las variables y funciones van en minúsculas; las constantes en MAYÚSCULAS.

**Sin punto y coma.** En Python no se usan `;` al final de cada línea (aunque técnicamente Python los acepta). El salto de línea es suficiente.

**Comentarios con `#`.** Todo lo que sigue a `#` en una línea es ignorado por Python.

```python
# Este es un comentario de línea completa
resultado = valor * tasa  # este comentario explica la línea
```

### El estándar PEP 8

PEP 8 es la guía de estilo oficial de Python. Seguirla hace que cualquier desarrollador Python pueda leer tu código sin esfuerzo adicional.

| Elemento | Convención | Ejemplo |
|----------|-----------|---------|
| Variables y funciones | `snake_case` | `valor_declarado`, `calcular_iva` |
| Constantes | `MAYUSCULAS` | `TASA_IVA`, `ESTADOS_VALIDOS` |
| Módulos y archivos | `snake_case` | `data_loader.py`, `utils.py` |
| Sangrado | 4 espacios | (no tabs) |
| Líneas | máximo 79 caracteres | |
| Líneas entre funciones | 2 líneas en blanco | |

En este curso seguimos PEP 8 en todo el código.

---

## El menú principal

Abre `main.py` en el editor. Ya tiene un menú funcional con siete opciones y una estructura `while` que mantiene el programa corriendo hasta que el usuario elige salir.

Ejecútalo ahora para ver cómo se ve:

```bash
python main.py
```

Verás el menú impreso y podrás escribir un número. La mayoría de opciones dice `(función pendiente de implementar)`. A medida que escribas cada función en `utils.py` y la importes en `main.py`, irás descomentando las líneas correspondientes en `ejecutar_opcion()` y la opción empezará a funcionar.

`main.py` no cambia de estructura, más bien incrementa en las llamadas activas a funciones o procedimientos. En el archivo `utils.py` es donde está la lógica. Esto permite hacer una mejor separación de responsabilidades

> Revisa la función `ejecutar_opcion()` en `main.py`. Cada bloque `elif` tiene el código comentado con `# TODO`. Cuando implementes la función correspondiente, descomentas esas líneas y la opción del menú puede ser utilizada.

> TODO significa “por hacer”. En programación se usa como una marca dentro del código para señalar una tarea pendiente.

En Python suele escribirse como comentario:

```python
# TODO: conectar esta opción cuando la función esté implementada
```

Python ignora esa línea porque empieza con `#`, pero la persona que lee el código entiende que allí falta completar algo.

En este proyecto, los `# TODO` indican opciones del menú que ya están planeadas, pero que todavía dependen de funciones que vas a escribir en `utils.py`. Cuando la función esté lista, podrás descomentar las líneas correspondientes y probar la opción desde `main.py`.

Usar `TODO` ayuda a trabajar por etapas: primero se deja preparada la estructura general y luego se completa la lógica paso a paso.

---


En esta sesión construyes las funciones del proyecto de análisis tributario. Partes de valores simples — números y cadenas de texto — y avanzas hasta estructuras de datos completas. Al final de la sesión, el menú interactivo del proyecto tendrá todas sus opciones funcionando.

> FlUJO DE TRABAJO DE LA SESION: 
* leer el contexto de una función, 
* implementar el cuerpo en `utils.py
* descomentar el bloque correspondiente en `main.py`
* ejecutar `python main.py` y verificar la salida. 
Cada vez que una sección queda completa, add, commit y push


---

## 1. Módulos e imports

Python organiza el código en archivos llamados **módulos**. Un módulo es
cualquier archivo `.py`: puede contener funciones, constantes o clases.
Cuando el proyecto crece, separar el código en módulos permite reutilizarlo
desde cualquier otro archivo sin copiar y pegar.

La instrucción `import` hace que las definiciones de un módulo estén
disponibles en el archivo actual:

```python
from utils import calcular_iva
```

Esto le dice a Python: "busca el módulo `utils` y trae la función
`calcular_iva` a este espacio de nombres". Después de esta línea puedes
llamar a `calcular_iva(...)` directamente.

### Paquetes: módulos organizados en carpetas

Cuando hay varios módulos relacionados, conviene agruparlos en una carpeta.
A esa carpeta con módulos adentro se le llama **paquete**.

Para que Python reconozca una carpeta como paquete (y no como una carpeta
cualquiera), debe contener un archivo llamado `__init__.py`. Ese archivo
puede estar vacío; su sola presencia es lo que marca la diferencia.

```text
src/
├── __init__.py   ← convierte src/ en un paquete
└── utils.py      ← módulo dentro del paquete
```

Con esa estructura, el import incluye el nombre del paquete antes del módulo:

```python
from src.utils import calcular_iva
```

Resumen:

| Concepto | Qué es | Ejemplo |
|---|---|---|
| Módulo | Un archivo `.py` | `utils.py` |
| Paquete | Una carpeta con `__init__.py` | `src/` |

```bash
ls src/
# __init__.py  utils.py  utils_solved.py
```

Sin `__init__.py`, la línea `from src.utils import ...` fallaría con `ModuleNotFoundError`.

### Cómo están organizados los imports en este proyecto

Todos los imports de `main.py` están al inicio del archivo, agrupados por sección. Los que corresponden a funciones que aún no has implementado ya están escritos; simplemente funcionarán en cuanto completes el cuerpo de cada función en `utils.py`.

```python
# Bloque de imports al inicio de main.py
from src.utils import calcular_iva
from src.utils import formatear_reporte_valor
from src.utils import mostrar_resultado
# ...
```

Colocar todos los imports al inicio hace que cualquier persona que lea el archivo vea de un vistazo de qué módulos depende, sin tener que buscar dentro del código.

---

## 2. Funciones y procedimientos

Una **función** recibe datos, realiza una transformación y retorna un resultado. 

Un **procedimiento** también recibe datos, pero en lugar de retornar un valor ejecuta una acción — como imprimir en pantalla — y termina sin retornar nada útil.

En Python la distinción se nota en la última línea del cuerpo:

```python
# Función: retorna un valor
def calcular_iva(valor_base, tasa=0.19):
    iva = valor_base * tasa
    return iva               # ← retorna

# Procedimiento: ejecuta una acción
def mostrar_resultado(etiqueta, valor):
    print(f"  {etiqueta}: ${valor:,.0f}")
    # no hay return
```

NOTA: Cuando defines parámetros con valor por defecto (`tasa=0.19`), el llamado a la función puede omitir estos parámetros:

```python
calcular_iva(1_000_000)        # usa tasa=0.19 → 190000.0
calcular_iva(1_000_000, 0.05)  # usa tasa=0.05 → 50000.0
```

### f-strings con formato numérico

Un **f-string** es una cadena que permite incrustar el valor de una variable
directamente dentro del texto. Se escribe poniendo una `f` antes de las
comillas, y las variables o expresiones van entre llaves `{}`:

```python
nombre = "Empresa ABC"
valor = 1500000
print(f"Cliente: {nombre}, valor: {valor}")
# → Cliente: Empresa ABC, valor: 1500000
```

Python evalúa lo que está dentro de las llaves y lo convierte en texto. Sin
f-strings tendrías que concatenar con `+` o usar `str()`, lo que hace el
código más difícil de leer.

Los f-strings también aceptan **especificadores de formato** dentro de las llaves luego de un dos puntos. Esto permite controlar cómo se muestra el valor, sin
modificar la variable original:

| Especificador | Efecto | Ejemplo |
|---|---|---|
| `:,` | separadores de miles | `f"${1500000:,}"` → `$1,500,000` |
| `:.2f` | dos decimales | `f"{3.14159:.2f}"` → `3.14` |
| `:,.0f` | miles, sin decimales | `f"${190000:,.0f}"` → `$190,000` |

### Ejercicios

**básico** — Implementa `calcular_iva` y `mostrar_resultado` en `utils.py`. Luego descomenta el primer bloque de `menu_funciones_basicas()` en `main.py`, ejecuta y verifica:

```
  IVA sobre $1,500,000: $285,000
```

**intermedio** — Implementa `formatear_reporte_valor`. El formato de salida esperado es:

```
NIT 900123456 | Empresa ABC S.A.S. | $1,500,000 | ACTIVO
```

**avanzado** — Implementa `generar_ficha_contribuyente`. Usa variables intermedias para las transformaciones de texto antes de construir el f-string multilínea.


---

▶ **Pausa y piensa — 10 minutos**

Antes de continuar, verifica que `menu_funciones_basicas()` produzca la salida esperada. Si algo no coincide, revisa el formato del f-string y compara con los ejemplos de la docstring.

---

## 3. Encadenamiento de funciones

Encadenar funciones significa usar el resultado de una función como argumento de la siguiente. El valor "fluye" a través de una secuencia de transformaciones:

```
nit con guiones
    → limpiar_nit()    → "900123456"
    → validar_nit()    → True
    → procesar_nit()   → "NIT 900123456: válido"
```

Cada función tiene una responsabilidad única. `limpiar_nit` solo elimina guiones y puntos; no valida. `validar_nit` solo comprueba dígitos y longitud; no limpia. Cuando la lógica cambia en un parte (por ejemplo, si el NIT válido pasa de 9 a 10 dígitos mínimo), solo modificas esa función.

```python
def procesar_nit(nit):
    nit_limpio = limpiar_nit(nit)      # paso 1: limpiar
    es_valido = validar_nit(nit_limpio) # paso 2: validar
    if es_valido:
        mensaje = f"NIT {nit_limpio}: válido"
    else:
        mensaje = f"NIT {nit}: INVÁLIDO"
    return mensaje
```

Nota que `procesar_nit` llama a `limpiar_nit` y `validar_nit` — no reimplementa la lógica de ninguna de las dos. Esto es reutilización: las funciones anteriores son bloques que ensamblamos.

El método `.strip().upper().replace("  ", " ")` de `normalizar_texto` también es encadenamiento, pero de métodos sobre una cadena. El resultado de `.strip()` es una nueva cadena, sobre la que inmediatamente se llama `.upper()`, y así sucesivamente.

### Ejercicios

**básico** — Implementa `limpiar_nit` y `validar_nit`. Luego implementa `procesar_nit` usando las dos anteriores. Descomenta el primer bloque de `menu_encadenamiento()` y ejecuta.

**intermedio** — Implementa `normalizar_texto` como una sola línea encadenada. Verifica con `normalizar_texto("  empresa  abc  ")` → `"EMPRESA ABC"`.

**avanzado** — Implementa `pipeline_nit`. El formato de salida esperado:

```
NIT 900123456 — apto para procesamiento
NIT ABC-123 — rechazado: formato inválido
```

---

▶ **Pausa y piensa — 10 minutos**

Escribe en el chat o en tu cuaderno la respuesta a esta pregunta: si `validar_nit` recibe un NIT ya limpio, ¿por qué `procesar_nit` llama primero a `limpiar_nit` antes de llamar a `validar_nit`? ¿Qué pasaría si el NIT llega con guiones y no se limpia antes?


## 🔁 Ciclo Git

Haz commit al repositorio de los cambios que llevas

```bash
git add src/utils.py main.py
git commit -m "Sesión: funciones y encadenamiento implementados"
git push
```
---

## 4. Condicionales simples

Un condicional evalúa una expresión booleana y ejecuta código diferente según el resultado:

```python
if condicion:
    # se ejecuta cuando condicion es True
else:
    # se ejecuta cuando condicion es False
```

### Operadores lógicos

Los operadores `and`, `or` y `not` combinan condiciones booleanas:

| Operador | Resultado `True` cuando... |
|---|---|
| `a and b` | **ambas** condiciones son verdaderas |
| `a or b` | **al menos una** condición es verdadera |
| `not a` | la condición es **falsa** |

**Precedencia:** `not` se evalúa primero, luego `and`, luego `or`. Para mayor claridad, usa paréntesis cuando combines los tres:

```python
# Con paréntesis, la intención es clara:
alerta = (dias_mora > 60) and (not esta_pagando)
```


### Ejercicio básico · `esta_al_dia` 

Escribe `esta_al_dia(dias_mora)`. Retorna `True` si `dias_mora` es 0, `False` en cualquier otro caso.

Salida esperada con `[0, 1, 30, -5]`:
```
0 dias: True
1 dias: False
30 dias: False
-5 dias: False
```

### Ejercicio intermedio · `aplicar_descuento` 

Contexto: los contribuyentes que pagan voluntariamente antes de ser notificados reciben un descuento del 10 %.

Escribe `aplicar_descuento(valor, pago_voluntario)`. Si `pago_voluntario` es `True`, retorna el valor con el 10 % de descuento. Si no, retorna el valor original.

Salida esperada con `(1_000_000, True)` y `(1_000_000, False)`:
```
Con descuento  : $900,000
Sin descuento  : $1,000,000
```

### Ejercicio avanzado · `asignar_prioridad` 

Contexto: el sistema de seguimiento asigna prioridad de atención según el valor declarado y si el contribuyente tiene historial de incumplimiento.

Escribe `asignar_prioridad(valor, tiene_historial_incumplimiento)`. Retorna `"ALTA"` si el valor supera 1.000.000 Y tiene historial, `"MEDIA"` si solo cumple una de las dos condiciones, y `"BAJA"` si no cumple ninguna.

Piensa y escribe en un papel tres casos de prueba para `asignar_prioridad` donde `valor=500_000` y varía `tiene_historial`. Verifica cada caso ejecutando el menú.

---

## 🔁 Ciclo Git · 
Haz commit al repositorio de los cambios que llevas

```bash
git add src/utils.py
git commit -m "Sesión: practia condicionales simples"
git push
```


## 5. Condicionales anidados

Un condicional anidado coloca un `if` dentro de otro. Se usa cuando la segunda condición solo tiene sentido si la primera es verdadera.

```python
def evaluar_pago(estado, valor):
    """
    Evalúa si un registro está en orden según su estado y valor.

    Args:
        estado (str): Estado del registro.
        valor (float): Valor declarado.

    Returns:
        str: Resultado de la evaluación.
    """
    if estado == "ACTIVO":
        if valor >= 100_000:
            return "En regla"
        else:
            return "Activo con valor insuficiente"
    elif estado == "INACTIVO":
        return "Registro inactivo"
    else:
        return "Requiere revisión manual"
```

Se recomienda limitar el anidamiento a dos niveles. Cuando hay más de dos niveles, el código se vuelve más difícil de seguir y casi siempre puede reescribirse de forma más clara.

### Ejercicio básico · `clasificar_mora` 

Escribe `clasificar_mora(dias_mora, valor)`. Primero verifica si hay mora (dias_mora > 0). Si hay mora, clasifica según si el valor es mayor o menor a 500.000: `"Mora alta"` o `"Mora baja"`. Si no hay mora: `"Sin mora"`.

### Ejercicio intermedio · `determinar_tipo_seguimiento` 

Escribe `determinar_tipo_seguimiento(estado, valor, municipio)`. Si el estado es `ACTIVO`: si el municipio es `"Bogota"` o `"Medellin"` y el valor supera 2.000.000 → `"Seguimiento prioritario"`; de lo contrario → `"Seguimiento estándar"`. Si el estado es `PENDIENTE` → `"Seguimiento urgente"`. Cualquier otro estado → `"Sin seguimiento"`.

### Ejercicio avanzado · `evaluar_cumplimiento` 

Escribe `evaluar_cumplimiento(estado, valor, dias_mora, historial)`. Aplica reglas de negocio que cruzan las cuatro variables para producir una de estas categorías: `"Cumplimiento total"`, `"Incumplimiento leve"`, `"Incumplimiento grave"` o `"Caso crítico"`. Define tú mismo las reglas, pero deben cruzar al menos dos variables en cada nivel.

---

## 🔁 Ciclo Git · 
Haz commit al repositorio de los cambios que llevas

```bash
git add src/utils.py
git commit -m "Sesión: condicionales anidados"
git push
```

### Ejercicio de depuración

El siguiente código tiene un error lógico. Encuentra cuál es el error sin ejecutar el código primero:

```python
def clasificar_mora_buggy(dias_mora, valor):
    if valor > 500_000:
        if dias_mora > 0:
            return "Mora alta"
        else:
            return "Sin mora"
    else:
        return "Mora baja"
```

¿Qué devuelve `clasificar_mora_buggy(0, 800_000)`? ¿Es correcto? ¿Cuál es la diferencia con la versión correcta?

### Ejercicios

**básico** — Implementa `clasificar_mora` y `determinar_tipo_seguimiento`. Descomenta los bloques en `menu_condicionales_anidados()`.

**intermedio** — Implementa `evaluar_cumplimiento`. Esta función tiene cuatro ramas. Verifica cada rama con un caso de prueba diferente.

**avanzado** — ¿En qué orden deben estar las ramas de `evaluar_cumplimiento`? ¿Qué pasaría si el primer `if` fuera `estado == "PENDIENTE"` en lugar de `estado == "ACTIVO" and dias_mora == 0`?

---

## 6. Condicionales encadenados

Los condicionales encadenados (`if / elif / elif / else`) evalúan múltiples condiciones en secuencia. En cuanto una es verdadera, se ejecuta su bloque y las demás se saltean. Por eso el orden de las condiciones importa.

Para `clasificar_contribuyente`, las condiciones van de mayor a menor:

```python
def clasificar_contribuyente(valor):
    """
    Clasifica al contribuyente según su valor declarado.

    Categorías:
        GRANDE      : más de 5.000.000
        MEDIANO     : entre 1.000.001 y 5.000.000
        PEQUEÑO     : entre 100.001 y 1.000.000
        MÍNIMO      : entre 1 y 100.000
        SIN VALOR   : 0

    Args:
        valor (float): Valor declarado.

    Returns:
        str: Categoría del contribuyente.
    """
    if valor > 5_000_000:
        return "GRANDE"
    elif valor > 1_000_000:
        return "MEDIANO"
    elif valor > 100_000:
        return "PEQUEÑO"
    elif valor > 0:
        return "MÍNIMO"
    else:
        return "SIN VALOR"
```

Si el valor es `2_000_000`, la primera condición es `False`, la segunda es `True`, y retorna `"MEDIANO"`. Las condiciones siguientes nunca se evalúan. Si invirtieras el orden y pusieras `valor > 0` primero, cualquier valor positivo retornaría `"MINIMO"`.

`calcular_sancion_basica` sigue el mismo patrón, pero el resultado no es una cadena sino un número que se calcula con la tasa asignada:

```python
if dias_mora == 0:
    tasa = 0.0
elif dias_mora <= 30:
    tasa = 0.01
elif dias_mora <= 60:
    tasa = 0.03
elif dias_mora <= 90:
    tasa = 0.05
else:
    tasa = 0.10
sancion = valor_base * tasa
return sancion
```

Separar la asignación de `tasa` del cálculo de `sancion` hace que el `if/elif` solo decida la tasa, y la línea de cálculo queda limpia y única.

### Ejercicios

**básico** — Implementa `clasificar_contribuyente` y `describir_periodo`. Para `describir_periodo`, extrae el mes con `int(periodo[4:])` antes del `if/elif`.

**intermedio** — Implementa `calcular_sancion_basica` usando la variable `tasa`. Verifica los límites: 30 días exactos, 31 días.

**avanzado** — Implementa `priorizar_cobro`. Define primero las variables `mora_alta`, `mora_media` y `valor_alto`, y luego escribe el `if/elif` combinando esas variables.

---

▶ **Pausa y piensa — 10 minutos**

Descomenta los bloques de `menu_condicionales_encadenados()` y ejecuta. Compara los resultados de `calcular_sancion_basica(30, 1_000_000)` y `calcular_sancion_basica(31, 1_000_000)`. ¿La diferencia en sanción refleja correctamente el cambio de tramo?


## 🔁 Ciclo Git · 
Haz commit y push al repositorio de los cambios que llevas

```bash
git add src/utils.py
git commit -m "Sesión: condicionales anidados"
git push
```

### Ejercicio libre · `evaluar_riesgo_tributario`

Esta función no existe en `utils.py` ni en `main.py`. Tú defines la lógica,
escribes la documentación y la pruebas desde cero.

**Qué construir:** `evaluar_riesgo_tributario(valor, dias_mora, tiene_historial)`
retorna una categoría de riesgo: `"CRÍTICO"`, `"ALTO"`, `"MEDIO"` o `"BAJO"`.
Define tus propias reglas combinando las tres variables con condicionales
encadenados y operadores lógicos. Como orientación:

- `"CRÍTICO"` podría requerir que el valor sea alto **y** la mora prolongada.
- `"BAJO"` podría ser la ausencia de mora y de historial.

El criterio exacto es tuyo; lo importante es que uses `if / elif / elif / else`
y que las cuatro categorías sean alcanzables.

---

**Paso 1 — Escribe la función en `utils.py`**

Al final de la sección `CONDICIONALES ENCADENADOS`, agrega:

```python
def evaluar_riesgo_tributario(valor, dias_mora, tiene_historial):
    """
    [escribe aquí la descripción de la función]

    Args:
        valor (float): [descripción]
        dias_mora (int): [descripción]
        tiene_historial (bool): [descripción]

    Returns:
        str: Categoría de riesgo. Valores posibles:
             "CRÍTICO", "ALTO", "MEDIO", "BAJO".

    Ejemplos:
        evaluar_riesgo_tributario(4_000_000, 100, True)  -> [tu resultado]
        evaluar_riesgo_tributario(0, 0, False)           -> [tu resultado]
    """
    # tu implementación aquí
```

Completa la descripción, los ejemplos y el cuerpo antes de continuar.

---

**Paso 2 — Agrega el import en `main.py`**

En el bloque de imports que agrupa las funciones de condicionales encadenados:

```python
from src.utils import evaluar_riesgo_tributario
```

---

**Paso 3 — Escribe el código de prueba en `main.py`**

Dentro de `menu_condicionales_encadenados()`, después del último bloque
comentado agregar el llamado a la función

```python
 riesgo = evaluar_riesgo_tributario(valor, dias, historial)
    print(f"  ${valor:,} / {dias} días / historial={historial} → {riesgo}")
```

**Paso 4 — Ejecuta y verifica**

```bash
python main.py
```

Selecciona la opción de condicionales encadenados. ¿Los resultados reflejan
tus reglas? ¿Hay algún caso donde dos ramas producen el mismo resultado
aunque los datos sean distintos? ¿Todos los casos de prueba alcanzan
categorías diferentes?

**Paso 5 — Documenta, haz commit y push**

Asegúrate de que los ejemplos en la docstring incluyan el resultado esperado
real (no `[tu resultado]`). Luego:

```bash
git add src/utils.py main.py
git commit -m "Sesión 2: agrega evaluar_riesgo_tributario"
git push
```


---
## 7. Ciclos `for`

El ciclo `for` recorre una colección de elementos y ejecuta el mismo bloque
de código para cada uno. A diferencia del `while`, no necesitas gestionar un
índice manualmente: Python extrae cada elemento en orden y lo asigna a la
variable que defines:

```python
for elemento in coleccion:
    # hacer algo con elemento
```


### `imprimir_nits_validos` — procedimiento con contador

`imprimir_nits_validos` recorre una lista de NITs e imprime solo los que
pasan la validación. Es un **procedimiento**: su propósito es ejecutar una
acción (imprimir), no calcular un valor para retornar. El contador registra
cuántos NITs válidos se encontraron:

```python
def imprimir_nits_validos(nits):
    """
    Imprime los NITs válidos de una lista con un contador incremental.

    Es un procedimiento: no retorna ningún valor.

    Args:
        nits (list): Lista de cadenas con NITs.

    Ejemplo de salida con ["ABC123", "900123456", "800234567"]:
        NIT válido 1: 900123456
        NIT válido 2: 800234567
        Total válidos: 2 de 3
    """
    contador = 0
    total = len(nits)
    for nit in nits:
        if validar_nit(nit):
            contador = contador + 1
            print(f"  NIT válido {contador}: {nit}")
    print(f"  Total válidos: {contador} de {total}")
```

El acumulador `contador` se inicializa antes del ciclo y solo aumenta cuando
`validar_nit` retorna `True`. Si la lista no tiene ningún NIT válido, el
ciclo termina sin imprimir líneas intermedias. La última línea siempre se
imprime, incluso si el contador es cero.

### `calcular_totales` — acumuladores

Un **acumulador** es una variable que se inicializa antes del ciclo y se
actualiza en cada iteración. El patrón para sumar es siempre el mismo:
empezar en cero, recorrer la lista, agregar cada elemento:

```python
total = 0
for valor in valores:
    total = total + valor
```

El promedio se calcula una sola vez al terminar el ciclo, dividiendo el total
acumulado entre la cantidad de elementos. No se calcula dentro del ciclo
porque necesitas el total completo para dividir.

**Antes de continuar: acceso por posición en listas**

Una lista en Python es una secuencia ordenada. Cada elemento tiene un índice
que empieza en cero: `valores[0]` es el primero, `valores[1]` el segundo,
`valores[-1]` el último. Puedes leer `valores[0]` como "el elemento en la
posición 0 de la lista `valores`".

Para el máximo, el acumulador no puede empezar en cero. Considera una lista
donde todos los valores son negativos: el máximo real sería negativo, y un
acumulador en cero nunca lo reflejaría. El punto de partida correcto es el
primer elemento de la lista:

```python
maximo = valores[0]
for valor in valores:
    if valor > maximo:
        maximo = valor
```

`calcular_totales` combina los tres acumuladores y retorna los tres resultados
a la vez:

```python
def calcular_totales(valores):
    """
    Calcula el total, el promedio y el valor máximo de una lista.

    Args:
        valores (list): Lista de números. Debe tener al menos un elemento.

    Returns:
        tuple: (total, promedio, maximo)

    Ejemplo:
        calcular_totales([1_500_000, 850_000, 2_300_000])
        -> (4_650_000, 1_550_000.0, 2_300_000)
    """
    total = 0
    maximo = valores[0]
    for valor in valores:
        total = total + valor
        if valor > maximo:
            maximo = valor
    promedio = total / len(valores)
    return total, promedio, maximo
```

La línea `return total, promedio, maximo` retorna los tres valores como una
tupla. En `main.py` se desempaquetan en tres variables separadas:
`total, promedio, maximo = calcular_totales(valores)`.

### `generar_periodos_multiple` — ciclos anidados

Cuando necesitas combinar dos colecciones —todos los años con todos los
meses— la solución natural son dos ciclos anidados. El externo recorre los
años; por cada año, el interno genera todos sus meses:

```python
def generar_periodos_multiple(anio_inicio, anio_fin, meses_por_anio):
    """
    Genera códigos de período para un rango de años.

    Cada código tiene el formato YYYYMM: cuatro dígitos para el año
    y dos para el mes, con cero a la izquierda si el mes es de un dígito.

    Args:
        anio_inicio (int): Año inicial del rango (inclusive).
        anio_fin (int): Año final del rango (inclusive).
        meses_por_anio (int): Número de meses a generar por cada año.

    Returns:
        list: Lista de cadenas en formato YYYYMM.

    Ejemplo:
        generar_periodos_multiple(2024, 2025, 3)
        -> ["202401", "202402", "202403", "202501", "202502", "202503"]
    """
    periodos = []
    for anio in range(anio_inicio, anio_fin + 1):
        for mes in range(1, meses_por_anio + 1):
            codigo = f"{anio}{mes:02d}"
            periodos.append(codigo)
    return periodos
```

El especificador `:02d` formatea el entero con al menos dos dígitos,
rellenando con cero a la izquierda si es necesario: `1` → `"01"`,
`12` → `"12"`. Sin él, enero de 2024 quedaría como `"20241"` en lugar de
`"202401"`. La lista `periodos` se inicializa vacía antes de los ciclos y
recibe un nuevo elemento al final de cada iteración interna.

### Ejercicios

**básico** — Implementa `imprimir_nits_validos`. El contador solo avanza
cuando el NIT es válido. Descomenta el bloque en `menu_ciclos_for()`.

**intermedio** — Implementa `calcular_totales`. Inicializa `maximo = valores[0]`
antes del ciclo. Retorna los tres valores con `return total, promedio, maximo`.

**avanzado** — Implementa `generar_periodos_multiple`. Verifica con
`generar_periodos_multiple(2024, 2025, 3)` que la lista tenga exactamente
6 elementos y que el último sea `"202503"`.

---

▶ **Pausa y piensa — 10 minutos**

Verifica `calcular_totales` con los valores de `POR_REVISAR`:
`[1_500_000, 850_000, 0, 2_300_000, 950_000, 3_200_000, 450_000, 1_100_000]`.
El total esperado es `10_350_000` y el máximo es `3_200_000`. Si los valores
no coinciden, añade un `print` temporal dentro del ciclo para ver qué valor
tiene `total` en cada iteración.

## 🔁 Ciclo Git

```bash
git add src/utils.py
git commit -m "Sesión 2: ciclos for"
git push
```

### Ejercicio libre · `resumir_nits`

Sigue el mismo proceso de la sección 6: escribe la función en `utils.py` con
docstring completa, agrégala a los imports de `main.py`, escribe el código de
prueba en `menu_ciclos_for()` y haz commit.

**Qué construir:** `resumir_nits(nits)` recibe una lista de cadenas y retorna
un diccionario con tres claves: `"validos"`, `"invalidos"` y `"total"`.
Usa un ciclo `for`, llama a `validar_nit` para clasificar cada elemento, y
acumula los conteos.

**Dónde colocarla en `utils.py`:** al final de la sección `CICLOS FOR`.

**Código de prueba sugerido para `menu_ciclos_for()`:**

```python
# Ejercicio libre: resumir_nits
nits_prueba = ["900123456", "ABC123", "800234567", "123", "400678901", "XYZ"]
resumen = resumir_nits(nits_prueba)
print(f"\n  Resumen de NITs:")
print(f"    Válidos  : {resumen['validos']}")
print(f"    Inválidos: {resumen['invalidos']}")
print(f"    Total    : {resumen['total']}")
```

**Resultado esperado:** `{"validos": 3, "invalidos": 3, "total": 6}`.
---

---

## 8. Ciclos `while`

El ciclo `while` ejecuta su bloque mientras una condición sea verdadera. Se
usa cuando no sabes de antemano cuántas iteraciones necesitas: cuando buscas
el primer elemento que cumple un criterio, cuando procesas una lista hasta
agotar un límite, o cuando la condición de parada depende de los datos mismos.

La estructura básica con índice manual permite detener el ciclo antes de
llegar al final, o avanzar de forma no uniforme:

```python
indice = 0
while indice < len(lista):
    elemento = lista[indice]
    # procesar elemento
    indice = indice + 1   # avanza siempre, fuera de cualquier if
```

La línea `indice = indice + 1` debe estar dentro del `while` pero **fuera de
cualquier `if`**. Si la colocas dentro de un condicional, el ciclo puede
volverse infinito: cuando la condición del `if` es `False`, el índice no avanza
y el `while` evalúa el mismo elemento indefinidamente.

### `buscar_primer_valido` — retorno anticipado

`buscar_primer_valido` recorre una lista de NITs y retorna el primero que
pase la validación. No necesita llegar al final: en cuanto encuentra un NIT
válido, el `return` termina tanto el ciclo como la función de inmediato. Si
recorre toda la lista sin encontrar ninguno, retorna `None`:

```python
def buscar_primer_valido(nits):
    """
    Busca y retorna el primer NIT válido en una lista.

    Args:
        nits (list): Lista de cadenas con NITs.

    Returns:
        str o None: El primer NIT válido encontrado, o None si no hay ninguno.

    Ejemplos:
        buscar_primer_valido(["ABC", "123", "900123456"])  -> "900123456"
        buscar_primer_valido(["ABC", "123"])               -> None
    """
    indice = 0
    while indice < len(nits):
        nit = nits[indice]
        if validar_nit(nit):
            return nit              # sale del while y de la función
        indice = indice + 1
    return None                     # solo llega aquí si no encontró ninguno
```

El `return nit` dentro del `while` detiene tanto el ciclo como la función de
inmediato. El `return None` al final solo se ejecuta si el ciclo terminó sin
encontrar un NIT válido. Nota que `indice = indice + 1` está fuera del `if`:
el índice avanza siempre, tanto si el NIT es válido como si no.

### `sumar_hasta_limite` — acumulación con límite

`sumar_hasta_limite` recorre una lista y acumula valores mientras agregar el
siguiente no supere un límite. La condición de parada no depende del índice
sino del resultado que se obtendría al incluir el próximo elemento:

```python
def sumar_hasta_limite(valores, limite):
    """
    Acumula valores hasta que el siguiente superaría el límite indicado.

    El valor que causaría el desborde no se incluye en el total.

    Args:
        valores (list): Lista de números.
        limite (float): Máximo acumulado permitido.

    Returns:
        tuple: (cantidad, total) — cuántos elementos se procesaron y su suma.

    Ejemplo:
        sumar_hasta_limite([1_500_000, 850_000, 2_300_000], 3_000_000)
        -> (2, 2_350_000)
    """
    total = 0
    cantidad = 0
    indice = 0
    while indice < len(valores):
        valor_actual = valores[indice]
        if total + valor_actual > limite:
            break
        total = total + valor_actual
        cantidad = cantidad + 1
        indice = indice + 1
    return cantidad, total
```

La condición `total + valor_actual > limite` evalúa si agregar el elemento
actual excedería el límite **antes** de agregarlo. Si es así, `break` termina
el ciclo sin modificar `total` ni `cantidad`. El valor que habría causado el
desborde no se cuenta ni se suma.

### Variables bandera

Una **variable bandera** es una variable booleana que controla la continuación
de un ciclo. En lugar de depender únicamente de la condición del encabezado,
la bandera se inicializa en `True` y se asigna `False` cuando el ciclo debe
terminar:

```python
continuar = True
while continuar:
    # ejecutar algo
    if condicion_de_salida:
        continuar = False   # el ciclo termina en la próxima comprobación
```

La ventaja sobre `while True` con `break` es que la condición de salida queda
expresada como un cambio de estado explícito. El encabezado `while continuar`
comunica de inmediato que hay una variable que controla el ciclo; cualquiera
que lea el código sabe dónde buscar el mecanismo de parada.

El menú del proyecto usa este patrón. La bandera `continuar` empieza en
`True`. Cuando el usuario elige la opción `"0"`, el código asigna
`continuar = False`; el `while` comprueba la bandera al inicio del siguiente
ciclo y termina sin volver a mostrar el menú:

```python
def main():
    """Punto de entrada. Ejecuta el menú interactivo con variable bandera."""
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()
        if opcion in OPCIONES:
            nombre, funcion = OPCIONES[opcion]
            if funcion is None:
                continuar = False           # bandera: ya no continuar
                print("\nHasta la proxima.\n")
            else:
                funcion()
                input("\n  Presiona Enter para volver al menu...")
        else:
            print(f"\n  Opcion '{opcion}' no reconocida.")
```

La opción `"0"` tiene `None` como función en el diccionario `OPCIONES`. Cuando
el código detecta `funcion is None`, en lugar de llamar a una función de menú
asigna `False` a la bandera. El ciclo termina de forma limpia al final de esa
iteración.

### Ejercicios

**básico** — Implementa `buscar_primer_valido` y descomenta el primer bloque
de `menu_ciclos_while()`. Verifica que retorne `"900123456"` con la lista
`["ABC123", "123", "900123456", "800234567"]`.

**intermedio** — Implementa `sumar_hasta_limite`. El resultado esperado con
`([1_500_000, 850_000, 2_300_000], 3_000_000)` es `(2, 2_350_000)`.

**avanzado** — Implementa `validar_secuencia_periodos`. Verifica dos casos:
una secuencia válida como `["202401", "202402", "202403"]` y una con salto
como `["202401", "202403"]`. La función debe retornar `(False, 1)` para el
segundo caso.

---
## 🔁 Ciclo Git

```bash
git add src/utils.py
git commit -m "Sesión 2: MOD: agrega ejercicios ciclo while"
git push
```

### Ejercicio libre · `encontrar_indice`

Sigue el mismo proceso de la sección 6: función en `utils.py`, import en
`main.py`, código de prueba en `menu_ciclos_while()`, commit.

**Qué construir:** `encontrar_indice(lista, valor)` recorre una lista con
`while` y retorna la posición (índice entero) del primer elemento igual a
`valor`. Si no lo encuentra, retorna `-1`. No uses métodos built-in como
`.index()`.

**Dónde colocarla en `utils.py`:** al final de la sección `CICLOS WHILE`.

**Código de prueba sugerido para `menu_ciclos_while()`:**

```python
# Ejercicio libre: encontrar_indice
nits = ["900123456", "800234567", "700345678", "600456789"]
buscado = "700345678"
posicion = encontrar_indice(nits, buscado)
print(f"\n  Buscando '{buscado}':")
if posicion != -1:
    print(f"    Encontrado en posición {posicion}")
else:
    print(f"    No encontrado")

posicion_ausente = encontrar_indice(nits, "000000000")
print(f"  Buscando '000000000': posición {posicion_ausente}")
```

**Resultado esperado:** posición `2` para `"700345678"`, `-1` para
`"000000000"`.



## 10. Listas

Una lista es una colección ordenada de elementos. En Python se crea con
corchetes y sus elementos se separan con comas:

```python
valores = [1_500_000, 850_000, 0, 2_300_000]
```

Algunas operaciones básicas que usarás en esta sección:

- **Acceso por posición:** `valores[0]` es el primero, `valores[-1]` el último.
- **Longitud:** `len(valores)` retorna el número de elementos.
- **Agregar al final:** `valores.append(elemento)`.
- **Verificar pertenencia:** `elemento in valores` retorna `True` o `False`.

En las funciones de esta sección trabajarás con estas operaciones para
filtrar, verificar y ordenar listas de valores declarados.

### `filtrar_valores_en_rango` — crear listas nuevas sin modificar la original

`filtrar_valores_en_rango` recorre una lista y construye una nueva con solo
los valores que caen dentro de un rango. En lugar de modificar la lista
original, crea una vacía y la puebla con los elementos que cumplen la
condición:

```python
def filtrar_valores_en_rango(valores, minimo, maximo):
    """
    Retorna una lista nueva con los valores entre minimo y maximo (inclusive).

    No modifica la lista original.

    Args:
        valores (list): Lista de números.
        minimo (float): Límite inferior del rango (inclusive).
        maximo (float): Límite superior del rango (inclusive).

    Returns:
        list: Lista nueva con los valores que cumplen la condición.

    Ejemplo:
        filtrar_valores_en_rango([100_000, 500_000, 2_000_000, 300_000],
                                  200_000, 1_000_000)
        -> [500_000, 300_000]
    """
    resultado = []
    for valor in valores:
        esta_en_rango = valor >= minimo and valor <= maximo
        if esta_en_rango:
            resultado.append(valor)
    return resultado
```

La variable intermedia `esta_en_rango` separa la evaluación de la decisión:
primero se determina si el valor cae en el rango, luego se actúa sobre esa
conclusión. La alternativa de escribir la condición directamente en el `if`
es equivalente, pero la variable hace explícito qué se comprueba.

### `agregar_unico` — verificar antes de agregar

`agregar_unico` agrega un elemento a una lista solo si ese elemento no está
ya presente. El operador `not in` evalúa si el elemento está ausente:

```python
def agregar_unico(lista, elemento):
    """
    Agrega elemento a lista solo si no está ya presente.

    Modifica la lista original directamente.

    Args:
        lista (list): Lista donde se intentará agregar el elemento.
        elemento: Valor a agregar si no existe en la lista.

    Ejemplos:
        lista = [1, 2, 3]
        agregar_unico(lista, 2)  # no agrega, ya existe → lista sigue [1, 2, 3]
        agregar_unico(lista, 4)  # agrega → lista queda [1, 2, 3, 4]
    """
    if elemento not in lista:
        lista.append(elemento)
```

A diferencia de `filtrar_valores_en_rango`, `agregar_unico` no retorna nada:
modifica directamente la lista que recibe. Esto contrasta con el patrón de
crear una lista nueva: aquí la intención es cambiar la lista que ya existe,
no producir una copia modificada.

### `ordenar_valores` — algoritmo de burbuja - solo para usuarios avanzados

`ordenar_valores` retorna una copia de la lista ordenada sin modificar la
original. El ordenamiento usa el **algoritmo de burbuja**: recorre la lista
comparando pares de elementos adyacentes e intercambiando los que están en
el orden incorrecto, y repite este proceso hasta que ningún par quede fuera
de lugar:

```python
def ordenar_valores(valores, descendente=True):
    """
    Retorna una copia de la lista ordenada por el algoritmo de burbuja.

    No modifica la lista original.

    Args:
        valores (list): Lista de números a ordenar.
        descendente (bool): Si True, ordena de mayor a menor.
                            Si False, ordena de menor a mayor.
                            Por defecto True.

    Returns:
        list: Lista nueva con los mismos elementos ordenados.

    Ejemplos:
        ordenar_valores([3, 1, 2])             -> [3, 2, 1]
        ordenar_valores([3, 1, 2], False)      -> [1, 2, 3]
    """
    resultado = list(valores)   # copia para no modificar el original
    n = len(resultado)
    for i in range(n):
        for j in range(0, n - i - 1):
            if descendente:
                deben_intercambiarse = resultado[j] < resultado[j + 1]
            else:
                deben_intercambiarse = resultado[j] > resultado[j + 1]
            if deben_intercambiarse:
                temporal = resultado[j]
                resultado[j] = resultado[j + 1]
                resultado[j + 1] = temporal
    return resultado
```

El intercambio de dos posiciones requiere una variable temporal. Sin ella,
la primera asignación sobrescribe el valor original antes de guardarlo:

```python
# Con variable temporal: correcto
temporal      = resultado[j]
resultado[j]  = resultado[j + 1]
resultado[j + 1] = temporal

# Sin variable temporal: incorrecto
resultado[j]     = resultado[j + 1]   # resultado[j] se pierde
resultado[j + 1] = resultado[j]       # ahora ambas posiciones tienen el mismo valor
```

La variable `deben_intercambiarse` hace que el ciclo interno sea legible:
primero se determina si hay que intercambiar, luego se ejecuta si la respuesta
es afirmativa. El criterio de comparación cambia según el parámetro
`descendente`, pero la mecánica del intercambio es siempre la misma.

### Ejercicios

**básico** — Implementa `filtrar_valores_en_rango` y `agregar_unico`.
Descomenta los bloques de `menu_listas()`.

**intermedio** — Implementa `ordenar_valores`. Verifica que la lista original
no cambie después de llamar a la función (imprime la lista original antes y
después de la llamada).

**avanzado** — Prueba `ordenar_valores` con los dos modos (ascendente y descendente) sobre el mismo
conjunto de valores. Comprueba que el primer y el último elemento sean
correctos en cada caso.

---

---
## 🔁 Ciclo Git

```bash
git add src/utils.py
git commit -m "Sesión 2: MOD: agrega ejercicios listas"
git push
```

### Ejercicio libre · `separar_por_umbral`

Sigue el mismo proceso de la sección 6: función en `utils.py`, import en
`main.py`, código de prueba en `menu_listas()`, commit.

**Qué construir:** `separar_por_umbral(valores, umbral)` recibe una lista de
números y un umbral, y retorna una tupla de dos listas:
`(menores_o_iguales, mayores)`. La primera contiene los valores `<= umbral`;
la segunda, los `> umbral`. No modifica la lista original.

**Dónde colocarla en `utils.py`:** al final de la sección `LISTAS`.

**Código de prueba sugerido para `menu_listas()`:**

```python
# Ejercicio libre: separar_por_umbral
valores = [1_500_000, 850_000, 0, 2_300_000, 950_000, 3_200_000, 450_000]
umbral = 1_000_000
menores, mayores = separar_por_umbral(valores, umbral)
print(f"\n  Umbral: ${umbral:,}")
print(f"  Menores o iguales : {menores}")
print(f"  Mayores           : {mayores}")
print(f"  Total verificado  : {len(menores) + len(mayores) == len(valores)}")
```

**Resultado esperado:** `menores` con 4 elementos, `mayores` con 3,
`Total verificado: True`.

---

## 11. Diccionarios  - solo para usuarios más avanzados

Un diccionario asocia claves con valores. A diferencia de una lista, donde
accedes a los elementos por su posición numérica, en un diccionario accedes
por nombre. Cada registro de `DECLARACIONES` es un diccionario:

```python
registro = {
    "nit":       "900123456",
    "nombre":    "Empresa ABC S.A.S.",
    "municipio": "Bogota",
    "periodo":   "202401",
    "valor":     1_500_000,
    "estado":    "ACTIVO",
}
```

Accedes a un campo con su clave: `registro["valor"]` retorna `1_500_000`. Si
la clave no existe, Python lanza un `KeyError`. Para evitarlo, puedes usar
`.get("clave")`, que retorna `None` si la clave no está presente.

Puedes recorrer las claves de un diccionario con `for`, y verificar si una
clave existe con el operador `in`:

```python
for clave in diccionario:
    print(clave, diccionario[clave])

if "municipio" in registro:
    print(registro["municipio"])
```

### DECLARACIONES

`DECLARACIONES` es la constante central del proyecto: una lista de ocho
diccionarios que simulan registros tributarios reales. La encuentras al
inicio de `utils.py`. A partir de esta sección, todas las funciones la
reciben como argumento.

```python
primer_registro = DECLARACIONES[0]
primer_registro["nombre"]   # "Empresa ABC S.A.S."
primer_registro["valor"]    # 1_500_000
len(DECLARACIONES)          # 8
```

### `indexar_por_nit` — acceso directo por clave

`indexar_por_nit` construye un nuevo diccionario donde la clave es el NIT y
el valor es el registro completo. Con la lista original, buscar un registro
por NIT requiere recorrer todos los elementos hasta encontrar el que coincide.
Con el índice, la búsqueda es directa: `indice["900123456"]` retorna el
registro en una sola operación, sin importar cuántos registros haya:

```python
def indexar_por_nit(declaraciones):
    """
    Construye un índice de declaraciones usando el NIT como clave.

    Args:
        declaraciones (list): Lista de diccionarios con datos de declaraciones.

    Returns:
        dict: Diccionario donde cada clave es un NIT y el valor es el
              registro completo correspondiente.

    Ejemplo:
        indice = indexar_por_nit(DECLARACIONES)
        indice["900123456"]["nombre"]  -> "Empresa ABC S.A.S."
    """
    indice = {}
    for declaracion in declaraciones:
        nit = declaracion["nit"]
        indice[nit] = declaracion
    return indice
```

### `agrupar_por_municipio` — el patrón de agrupación

`agrupar_por_municipio` construye un diccionario donde cada clave es un
municipio y su valor es una lista con todos los registros de ese municipio.
El patrón de agrupación siempre sigue la misma estructura: si la clave aún
no existe se inicializa con una lista vacía, luego se agrega el elemento:

```python
def agrupar_por_municipio(declaraciones):
    """
    Agrupa las declaraciones por municipio.

    Args:
        declaraciones (list): Lista de diccionarios con datos de declaraciones.

    Returns:
        dict: Diccionario donde cada clave es un municipio y el valor es
              una lista de registros de ese municipio.

    Ejemplo:
        grupos = agrupar_por_municipio(DECLARACIONES)
        len(grupos["Bogota"])          -> 2
        grupos["Bogota"][0]["nit"]     -> "900123456"
    """
    grupos = {}
    for declaracion in declaraciones:
        municipio = declaracion["municipio"]
        if municipio not in grupos:
            grupos[municipio] = []
        grupos[municipio].append(declaracion)
    return grupos
```

La primera vez que aparece un municipio, `municipio not in grupos` es `True`
y se crea una lista vacía para esa clave. Las veces siguientes, la clave ya
existe y se omite la inicialización. Al final, cada entrada contiene todos
los registros de ese municipio en el orden en que aparecieron en la lista
original.

### `construir_resumen_por_estado` — acumuladores en diccionarios

`construir_resumen_por_estado` sigue el mismo patrón de agrupación, pero en
lugar de guardar registros completos acumula conteos y totales. Cada entrada
del resultado es a su vez un diccionario con dos acumuladores:

```python
def construir_resumen_por_estado(declaraciones):
    """
    Construye un resumen con conteo y total de valores por estado.

    Args:
        declaraciones (list): Lista de diccionarios con datos de declaraciones.

    Returns:
        dict: Diccionario donde cada clave es un estado y el valor es un
              diccionario con 'conteo' y 'total_valor'.

    Ejemplo:
        resumen = construir_resumen_por_estado(DECLARACIONES)
        resumen["ACTIVO"]["conteo"]       -> 5
        resumen["ACTIVO"]["total_valor"]  -> 9_350_000
    """
    resumen = {}
    for declaracion in declaraciones:
        estado = declaracion["estado"]
        if estado not in resumen:
            resumen[estado] = {"conteo": 0, "total_valor": 0}
        resumen[estado]["conteo"] = resumen[estado]["conteo"] + 1
        resumen[estado]["total_valor"] = (
            resumen[estado]["total_valor"] + declaracion["valor"]
        )
    return resumen
```

La inicialización `{"conteo": 0, "total_valor": 0}` establece los dos
acumuladores en cero la primera vez que aparece un estado. Las líneas
siguientes los actualizan en cada iteración, independientemente de si el
estado era nuevo o ya existía.

### Ejercicios

**básico** — Implementa `indexar_por_nit` y `filtrar_por_estado`. Descomenta
los primeros bloques de `menu_diccionarios()`.

**intermedio** — Implementa `agrupar_por_municipio` e `imprimir_agrupacion`.
La salida esperada debe mostrar los cuatro municipios con su conteo y total.

**avanzado** — Implementa `calcular_estadisticas`. Maneja el caso de división
por cero cuando no hay registros activos. Verifica que `promedio_valor_activos`
sea aproximadamente `1_787_500` con los datos de `DECLARACIONES`.

---

▶ **Pausa y piensa — 10 minutos**

Ejecuta `menu_diccionarios()` con todas las secciones descomentadas. Verifica
la salida de `imprimir_agrupacion`: Bogotá y Medellín deben tener 2 registros
cada una; Cali y Barranquilla también. El total general debe ser `10_350_000`.

Si algún total no coincide, añade un `print` temporal dentro del ciclo de
`construir_resumen_por_estado` para ver el valor de `total_valor` después de
cada iteración.

---

🔁 **Ciclo Git**

Cuando todas las secciones estén funcionando:

```bash
git add .
git commit -m "Sesión 2: listas y diccionarios implementados"
git push
```

### Ejercicio libre · `calcular_promedio_por_municipio`

Sigue el mismo proceso de la sección 6: función en `utils.py`, import en
`main.py`, código de prueba en `menu_diccionarios()`, commit.

**Qué construir:** `calcular_promedio_por_municipio(declaraciones)` retorna
un diccionario donde cada clave es un municipio y el valor es el promedio de
`"valor"` de sus registros. Usa el patrón de `construir_resumen_por_estado`
como referencia: acumula conteo y suma por grupo, luego calcula el promedio
al final.

**Dónde colocarla en `utils.py`:** al final de la sección `DICCIONARIOS`.

**Código de prueba sugerido para `menu_diccionarios()`:**

```python
# Ejercicio libre: calcular_promedio_por_municipio
promedios = calcular_promedio_por_municipio(DECLARACIONES)
print("\n  Promedio por municipio:")
for municipio in promedios:
    print(f"    {municipio}: ${promedios[municipio]:,.0f}")
```

**Resultado esperado aproximado:**

## Cierre

Al terminar esta sesión tienes implementadas todas las funciones del proyecto en `utils.py`, el menú del proyecto funciona con las nueve opciones activas, y los commits reflejan el progreso por sección.
En la Sesión 4 incorporamos `numpy` y posteriormente Pandas, donde verás que muchos de los patrones que hoy implementaste manualmente (filtrar, agrupar, calcular estadísticas) tienen equivalentes directos en los DataFrame.

