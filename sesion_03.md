# Sesión 3: Condicionales, ciclos, listas y Markdown

**Python Intermedio para Análisis de Datos — DIAN 2026**


## 0. Sincronizar y retomar el repositorio de sesión 2

Desde la sesión anterior se agregaron algunos archivos nuevos a la plantilla del curso. Tu repositorio es una copia independiente de esa plantilla, así que esos cambios no llegan solos: necesitas traerlos con dos pasos cortos antes de empezar.

**Paso 1 — Sincronizar tu repositorio en GitHub**

1. Abre tu repositorio en GitHub.com (la página normal del repositorio, no el Codespace).
2. Justo arriba de la lista de archivos hay un botón que dice **Sync fork**. Haz clic ahí.
3. Se abre un panel pequeño con un botón verde que dice **Update branch**. Haz clic en ese botón.
4. GitHub confirma que tu repositorio ya quedó al día con la plantilla.

> Si el botón **Sync fork** no aparece, o GitHub dice que tu repositorio ya está al día ("This branch is up to date"), no hay cambios pendientes y puedes seguir directo al paso 2.

**Paso 2 — Traer los cambios a tu Codespace**

Ese primer paso solo actualiza la copia que vive en GitHub. Para que el Codespace donde escribes código también tenga los archivos nuevos, abre la terminal dentro del Codespace y ejecuta:

```bash
git pull
```

🔁 Con esto, los archivos nuevos llegan a tu espacio de trabajo. No necesitas crear un Codespace nuevo ni configurar nada desde cero, este mismo Codespace queda listo para continuar.

⚠️ Si ya habías modificado tú mismo alguno de los archivos que el instructor también actualizó, `git pull` puede avisarte de una diferencia entre las dos versiones. Si eso pasa, avísale al instructor antes de seguir.

Al finalizar esta sesión, serás capaz de:

1. Usar condicionales simples, anidados y encadenados para tomar decisiones en el código.
2. Construir ciclos `for` con acumuladores para recorrer colecciones.
3. Usar ciclos `while` con variable bandera para controlar la repetición desde el estado del programa.
4. Manipular listas: crear, indexar, filtrar y ordenar colecciones de valores.
5. Escribir un `README.md` con la sintaxis básica de Markdown.
6. Aplicar el flujo `add → commit → push` al finalizar cada sección.


## Lógica de programación
Continuar con el README de la sesión anterior tal y como se guía en la clase.

## Markdown — documentando el proyecto

Markdown es un formato de texto ligero que se convierte automáticamente en HTML cuando lo muestra GitHub. Un archivo `.md` se escribe con caracteres especiales que indican formato:

```
# Título principal         → encabezado grande
## Sección                 → encabezado mediano
### Subsección             → encabezado pequeño

- elemento de lista        → lista sin orden
- otro elemento

1. primer paso             → lista numerada
2. segundo paso

**texto en negrita**
`codigo_en_linea`
```

Los bloques de código se abren y cierran con tres backticks, con el nombre del lenguaje justo después de los primeros:

````
```python
def calcular_iva(valor):
    return valor * 0.19
```
````

### Actualizar el README del proyecto

El `README.md` del proyecto ya tiene contenido de la sesión 2. Ábrelo y agrega una sección que describa lo que implementaste hoy:

```markdown
## Sesión 3: Condicionales, ciclos y listas

### Funciones implementadas

**Condicionales**
- `esta_al_dia(dias_mora)` — indica si un contribuyente está al día
- `aplicar_descuento(valor, pago_voluntario)` — aplica descuento voluntario
- `clasificar_mora(dias_mora, valor)` — clasifica la mora por severidad
- `clasificar_contribuyente(valor)` — categoriza según valor declarado
- `calcular_sancion_basica(dias_mora, valor_base)` — calcula sanción por tramo

**Ciclos**
- `imprimir_nits_validos(nits)` — imprime NITs válidos con contador
- `calcular_totales(valores)` — total, promedio y máximo de una lista
- `buscar_primer_valido(nits)` — primer NIT válido de una lista

**Listas**
- `filtrar_valores_en_rango(valores, minimo, maximo)` — filtra por rango

### Cómo ejecutar

```bash
python main.py
```
```

Guarda el archivo. Verifica que se vea bien en GitHub abriendo el `README.md` desde el explorador de archivos del Codespace y usando la vista previa (`Ctrl+Shift+V`).

---

## 🔁 Commit final de la sesión

```bash
git add .
git commit -m "Sesión 3: condicionales, ciclos, listas y README actualizados"
git push
```

---

## Cierre

Al terminar esta sesión tienes implementadas las funciones de condicionales, ciclos y listas del proyecto, y el `README.md` documenta el estado actual del código.

En la sesión 4 incorporamos **NumPy**: verás cómo las operaciones que hoy implementaste con ciclos `for` y condicionales — filtrar, calcular totales, aplicar reglas — tienen equivalentes directos en arrays vectorizados que operan sobre colecciones enteras sin necesidad de escribir el ciclo explícitamente.

