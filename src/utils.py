"""
utils.py - Funciones del proyecto de análisis de declaraciones.

Completa cada función siguiendo las instrucciones en los comentarios TODO.
Cuando termines una función, ve a main.py, descomenta el bloque
correspondiente y ejecuta python main.py para verificar tu resultado.

Autora/Autor: [Tu nombre]
Fecha: [Fecha de la sesión]
"""


# ---------------------------------------------------------------------------
# Datos de práctica
#
# DECLARACIONES es la estructura central del proyecto: una lista de
# diccionarios donde cada elemento representa un registro de declaración
# tributaria. La usarás a partir de la sección de Diccionarios.
# ---------------------------------------------------------------------------

DECLARACIONES = [
    {
        "nit": "900123456",
        "nombre": "Empresa ABC S.A.S.",
        "municipio": "Bogota",
        "periodo": "202401",
        "valor": 1_500_000,
        "estado": "ACTIVO",
    },
    {
        "nit": "800234567",
        "nombre": "Comercial XYZ Ltda.",
        "municipio": "Medellin",
        "periodo": "202401",
        "valor": 850_000,
        "estado": "ACTIVO",
    },
    {
        "nit": "700345678",
        "nombre": "Servicios LMN S.A.S.",
        "municipio": "Cali",
        "periodo": "202401",
        "valor": 0,
        "estado": "INACTIVO",
    },
    {
        "nit": "600456789",
        "nombre": "Industrias PQR S.A.",
        "municipio": "Barranquilla",
        "periodo": "202401",
        "valor": 2_300_000,
        "estado": "ACTIVO",
    },
    {
        "nit": "500567890",
        "nombre": "Distribuidora STU Ltda.",
        "municipio": "Bogota",
        "periodo": "202402",
        "valor": 950_000,
        "estado": "PENDIENTE",
    },
    {
        "nit": "400678901",
        "nombre": "Inversiones VWX S.A.S.",
        "municipio": "Medellin",
        "periodo": "202402",
        "valor": 3_200_000,
        "estado": "ACTIVO",
    },
    {
        "nit": "300789012",
        "nombre": "Transportes YZA Ltda.",
        "municipio": "Cali",
        "periodo": "202402",
        "valor": 450_000,
        "estado": "SUSPENDIDO",
    },
    {
        "nit": "200890123",
        "nombre": "Construcciones BCD S.A.",
        "municipio": "Barranquilla",
        "periodo": "202402",
        "valor": 1_100_000,
        "estado": "ACTIVO",
    },
]


# ---------------------------------------------------------------------------
# FUNCIONES Y PROCEDIMIENTOS
# Trabajan con tipos simples: str, int, float, bool.
# ---------------------------------------------------------------------------

def calcular_iva(valor_base, tasa=0.19):
    """
    Calcula el IVA sobre un valor base.

    Args:
        valor_base (float): Monto antes de impuestos.
        tasa (float): Tasa de IVA. Por defecto 0.19 (19 %).

    Returns:
        float: Valor del IVA.

    Ejemplos:
        calcular_iva(1_000_000)        -> 190000.0
        calcular_iva(1_000_000, 0.05)  -> 50000.0
        calcular_iva(0)                -> 0.0
    """
    # TODO:
    # 1. Multiplica valor_base por tasa y guarda el resultado en una
    #    variable llamada iva.
    # 2. Retorna iva.
    iva=valor_base*tasa
    return iva
    #pass


def formatear_reporte_valor(nit, nombre, valor, estado):
    """
    Genera una línea de reporte con los campos principales de una declaración.

    Args:
        nit (str): NIT del contribuyente.
        nombre (str): Nombre o razón social.
        valor (float): Valor declarado.
        estado (str): Estado del registro.

    Returns:
        str: Cadena con formato "NIT XXXXXXXXX | Nombre | $valor | ESTADO".

    Ejemplo:
        formatear_reporte_valor("900123456", "Empresa ABC S.A.S.", 1_500_000, "ACTIVO")
        -> "NIT 900123456 | Empresa ABC S.A.S. | $1,500,000 | ACTIVO"
    """
    # TODO:
    # 1. Construye una cadena usando un f-string con este formato exacto:
    #    "NIT {nit} | {nombre} | ${valor:,} | {estado}"
    #    (el :, dentro del f-string agrega separadores de miles al número)
    # 2. Guarda el resultado en una variable llamada linea.
    # 3. Retorna linea.
    #pass
    linea=f"NIT {nit} | {nombre} | ${valor:,} | {estado}"
    return linea


def mostrar_resultado(etiqueta, valor):
    """
    Procedimiento: imprime un resultado con formato de moneda.

    Este es un procedimiento, no una función: ejecuta una acción
    (imprimir) y no retorna ningún valor útil.

    Args:
        etiqueta (str): Descripción del resultado.
        valor (float): Valor numérico a mostrar.
    """
    # TODO:
    # 1. Imprime usando print() y un f-string con este formato:
    #    "  {etiqueta}: ${valor:,.0f}"
    #    (el ,.0f formatea el número con separadores de miles y sin decimales)
    # Nota: este es un procedimiento, no retorna nada.
    print(f"{etiqueta} :${valor:,.0f}")
    #pass


def generar_ficha_contribuyente(nit, nombre, municipio, periodo, valor, estado):
    """
    Genera una ficha formal de contribuyente como texto multilínea.

    Recibe seis parámetros escalares y retorna una cadena con formato
    de recuadro. Nombre y municipio se muestran en mayúsculas.

    Args:
        nit (str): NIT del contribuyente.
        nombre (str): Nombre o razón social.
        municipio (str): Municipio de registro.
        periodo (str): Período en formato YYYYMM.
        valor (float): Valor declarado.
        estado (str): Estado del registro.

    Returns:
        str: Texto con la ficha en recuadro.

    Ejemplo de salida:
        ╔══════════════════════════════════════╗
        ║  FICHA DE CONTRIBUYENTE              ║
        ╠══════════════════════════════════════╣
          NIT        : 900123456
          Nombre     : EMPRESA ABC S.A.S.
          Municipio  : BOGOTA
          Periodo    : 202401
          Valor      : $1,500,000
          Estado     : ACTIVO
        ╚══════════════════════════════════════╝
    """
    # TODO:
    # 1. Convierte nombre a mayúsculas con .upper() y guárdalo en
    #    una variable llamada nombre_mayusculas.
    # 2. Convierte municipio a mayúsculas y guárdalo en municipio_mayusculas.
    # 3. Formatea el valor como cadena: valor_formateado = f"${valor:,}"
    # 4. Construye la ficha usando un f-string multilínea que contenga
    #    los caracteres de recuadro y los seis campos.
    #    Usa las variables intermedias del paso 1, 2 y 3.
    # 5. Retorna ficha.
    #pass
    nombre_mayusculas=nombre.upper()
    municipio_mayusculas=municipio.upper()
    valor_formateado= f"${valor:,}"
    ficha=f"""
        ╔══════════════════════════════════════╗
        ║  FICHA DE CONTRIBUYENTE              ║
        ╠══════════════════════════════════════╣
          NIT        : {nit}
          Nombre     : {nombre_mayusculas}
          Municipio  : {municipio_mayusculas}
          Periodo    : {periodo}
          Valor      : {valor_formateado}
          Estado     : {estado}
        ╚══════════════════════════════════════╝ 
    """
    
    
    return ficha
    


# ---------------------------------------------------------------------------
# ENCADENAMIENTO DE FUNCIONES
# ---------------------------------------------------------------------------

def limpiar_nit(nit):
    """
    Elimina guiones y puntos de un NIT.

    Args:
        nit (str): NIT posiblemente con guiones o puntos.

    Returns:
        str: NIT sin guiones ni puntos.

    Ejemplos:
        limpiar_nit("900-123-456")  -> "900123456"
        limpiar_nit("900.123.456")  -> "900123456"
        limpiar_nit("900123456")    -> "900123456"
    """
    # TODO:
    # 1. Elimina los guiones del nit con .replace("-", "") y guarda el
    #    resultado en una variable llamada sin_guiones.
    # 2. Elimina los puntos de sin_guiones con .replace(".", "") y guarda
    #    el resultado en una variable llamada sin_puntos.
    # 3. Retorna sin_puntos.
    #pass
    sin_guiones =nit.replace("-","")
    sin_puntos = sin_guiones.replace(".","")
    
    return sin_puntos
    

def validar_nit(nit):
    """
    Valida que un NIT tenga el formato correcto.

    Limpia el NIT antes de validar. Un NIT válido contiene solo
    dígitos y tiene entre 9 y 10 caracteres.

    Args:
        nit (str): NIT a validar (puede tener guiones o puntos).

    Returns:
        bool: True si es válido, False si no.

    Ejemplos:
        validar_nit("900123456")    -> True
        validar_nit("900-123-456")  -> True
        validar_nit("ABC123")       -> False
        validar_nit("123")          -> False
    """
    # TODO:
    # 1. Llama a limpiar_nit(nit) y guarda el resultado en nit_limpio.
    # 2. Verifica que nit_limpio solo tenga dígitos con .isdigit() y
    #    guarda el resultado (True/False) en solo_digitos.
    # 3. Verifica que la longitud sea válida:
    #    longitud_valida = len(nit_limpio) >= 9 and len(nit_limpio) <= 10
    # 4. Retorna solo_digitos and longitud_valida.
    #pass
    nit_limpio = limpiar_nit(nit)
    solo_digitos = nit_limpio.isdigit()
    longitud_valida = len(nit_limpio) >= 9 and len(nit_limpio) <= 10
    
    return solo_digitos , longitud_valida

def normalizar_texto(texto):
    """
    Limpia y normaliza una cadena de texto.

    Aplica en cadena: elimina espacios al inicio/final, convierte a
    mayúsculas y elimina espacios dobles internos.

    Args:
        texto (str): Texto a normalizar.

    Returns:
        str: Texto normalizado en mayúsculas y sin espacios extra.

    Ejemplos:
        normalizar_texto("  bogotá d.c.  ")  -> "BOGOTÁ D.C."
        normalizar_texto("  empresa  abc  ") -> "EMPRESA ABC"
    """
    # TODO:
    # Encadena tres métodos en una sola expresión y retorna el resultado:
    # 1. texto.strip()           elimina espacios al inicio y al final
    # 2. .upper()                convierte a mayúsculas
    # 3. .replace("  ", " ")     elimina espacios dobles internos
    # Retorna todo en una sola línea: return texto.strip().upper().replace(...)
    pass


def procesar_nit(nit):
    """
    Limpia y valida un NIT. Retorna un mensaje con el resultado.

    Args:
        nit (str): NIT a procesar.

    Returns:
        str: Mensaje indicando si el NIT es válido o no.

    Ejemplos:
        procesar_nit("900-123-456")  -> "NIT 900123456: válido"
        procesar_nit("ABC-123")      -> "NIT ABC-123: INVÁLIDO"
    """
    # TODO:
    # 1. Llama a limpiar_nit(nit) y guarda el resultado en nit_limpio.
    # 2. Llama a validar_nit(nit_limpio) y guarda el resultado en es_valido.
    # 3. Si es_valido es True:
    #    mensaje = f"NIT {nit_limpio}: válido"
    # 4. Si es_valido es False:
    #    mensaje = f"NIT {nit}: INVÁLIDO"
    # 5. Retorna mensaje.
    #pass
    nit_limpio =limpiar_nit(nit)
    es_valido=validar_nit(nit_limpio)
    if es_valido:
        mensaje = f"NIT {nit_limpio}: válido"
    else:
        mensaje = f"NIT {nit_limpio}: Inválido"
    return mensaje

def pipeline_nit(nit):
    """
    Aplica un pipeline de tres operaciones sobre un NIT:
    limpieza → validación → informe de resultado.

    Args:
        nit (str): NIT de entrada (puede tener guiones o puntos).

    Returns:
        str: Informe del resultado del pipeline.

    Ejemplos:
        pipeline_nit("900-123-456")  -> "NIT 900123456 — apto para procesamiento"
        pipeline_nit("ABC-123")      -> "NIT ABC-123 — rechazado: formato inválido"
    """
    # TODO:
    # 1. Llama a limpiar_nit(nit) y guarda el resultado en nit_limpio.
    # 2. Llama a validar_nit(nit_limpio) y guarda el resultado en es_valido.
    # 3. Si es_valido es True:
    #    informe = f"NIT {nit_limpio} — apto para procesamiento"
    # 4. Si es_valido es False:
    #    informe = f"NIT {nit} — rechazado: formato inválido"
    # 5. Retorna informe.
    pass


# ---------------------------------------------------------------------------
# CONDICIONALES SIMPLES
# ---------------------------------------------------------------------------

def esta_al_dia(dias_mora):
    """
    Determina si un contribuyente está al día en sus pagos.

    Args:
        dias_mora (int): Días de mora. Cero significa al día.

    Returns:
        bool: True si dias_mora es 0, False en cualquier otro caso.

    Ejemplos:
        esta_al_dia(0)   -> True
        esta_al_dia(1)   -> False
        esta_al_dia(30)  -> False
    """
    # TODO:
    # 1. Escribe un if/else:
    #    - si dias_mora == 0: retorna True
    #    - de lo contrario: retorna False
    pass


def aplicar_descuento(valor, pago_voluntario):
    """
    Aplica un descuento del 10 % si el pago es voluntario.

    Args:
        valor (float): Valor original del pago.
        pago_voluntario (bool): True si el pago es voluntario.

    Returns:
        float: Valor con descuento, o el valor original si no aplica.

    Ejemplos:
        aplicar_descuento(1_000_000, True)   -> 900000.0
        aplicar_descuento(1_000_000, False)  -> 1000000
    """
    # TODO:
    # 1. Si pago_voluntario es True:
    #    - Calcula el descuento: descuento = valor * 0.10
    #    - Calcula el valor final: valor_con_descuento = valor - descuento
    #    - Retorna valor_con_descuento
    # 2. Si pago_voluntario es False:
    #    - Retorna valor sin modificar
    pass


def asignar_prioridad(valor, tiene_historial_incumplimiento):
    """
    Asigna una prioridad de atención según valor e historial.

    Reglas:
        ALTA  : valor > 1.000.000 Y tiene historial de incumplimiento
        MEDIA : solo una de las dos condiciones es verdadera
        BAJA  : ninguna condición se cumple

    Args:
        valor (float): Valor declarado.
        tiene_historial_incumplimiento (bool): True si hay historial.

    Returns:
        str: "ALTA", "MEDIA" o "BAJA".
    """
    # TODO:
    # 1. Evalúa las dos condiciones por separado y guárdalas en variables:
    #    valor_alto = valor > 1_000_000
    #    tiene_historial = tiene_historial_incumplimiento
    # 2. Escribe un if/elif/else:
    #    - si valor_alto AND tiene_historial: retorna "ALTA"
    #    - si valor_alto OR tiene_historial: retorna "MEDIA"
    #    - de lo contrario: retorna "BAJA"
    pass


# ---------------------------------------------------------------------------
# CONDICIONALES ANIDADOS
# ---------------------------------------------------------------------------

def clasificar_mora(dias_mora, valor):
    """
    Clasifica la situación de mora de un contribuyente.

    Primero verifica si hay mora; si la hay, clasifica por valor.

    Args:
        dias_mora (int): Días de mora.
        valor (float): Valor declarado.

    Returns:
        str: "Mora alta", "Mora baja" o "Sin mora".
    """
    # TODO:
    # 1. Escribe el if externo: si dias_mora > 0 (hay mora)
    #    - Dentro, escribe el if interno: si valor > 500_000
    #      retorna "Mora alta"
    #    - else (valor no supera 500_000):
    #      retorna "Mora baja"
    # 2. else (no hay mora):
    #    retorna "Sin mora"
    pass


def determinar_tipo_seguimiento(estado, valor, municipio):
    """
    Determina el tipo de seguimiento que requiere un registro.

    Args:
        estado (str): Estado del registro (ACTIVO, PENDIENTE, etc.).
        valor (float): Valor declarado.
        municipio (str): Municipio del contribuyente.

    Returns:
        str: Tipo de seguimiento asignado.
    """
    # TODO:
    # 1. Si estado == "ACTIVO":
    #    - Calcula si el municipio es prioritario:
    #      municipio_prioritario = municipio == "Bogota" or municipio == "Medellin"
    #    - Calcula si el valor es alto: valor_alto = valor > 2_000_000
    #    - Si municipio_prioritario AND valor_alto: retorna "Seguimiento prioritario"
    #    - De lo contrario: retorna "Seguimiento estándar"
    # 2. elif estado == "PENDIENTE": retorna "Seguimiento urgente"
    # 3. else: retorna "Sin seguimiento"
    pass


def evaluar_cumplimiento(estado, valor, dias_mora, historial):
    """
    Evalúa el nivel de cumplimiento de un contribuyente.

    Args:
        estado (str): Estado del registro.
        valor (float): Valor declarado.
        dias_mora (int): Días de mora.
        historial (bool): True si tiene historial de incumplimiento.

    Returns:
        str: "Cumplimiento total", "Incumplimiento leve",
             "Incumplimiento grave" o "Caso crítico".
    """
    # TODO:
    # Usa una serie de if independientes (no anidados entre sí):
    #
    # 1. Si estado == "ACTIVO" AND dias_mora == 0:
    #    retorna "Cumplimiento total"
    #
    # 2. Si estado == "ACTIVO" AND dias_mora > 0:
    #    - Si dias_mora <= 30 AND NOT historial: retorna "Incumplimiento leve"
    #    - De lo contrario: retorna "Incumplimiento grave"
    #
    # 3. Si estado == "PENDIENTE" OR estado == "SUSPENDIDO":
    #    - Si historial AND valor > 1_000_000: retorna "Caso crítico"
    #    - De lo contrario: retorna "Incumplimiento grave"
    #
    # 4. Para cualquier otro caso: retorna "Incumplimiento leve"
    pass


# ---------------------------------------------------------------------------
# CONDICIONALES ENCADENADOS
# ---------------------------------------------------------------------------

def clasificar_contribuyente(valor):
    """
    Clasifica al contribuyente según su valor declarado.

    Categorías:
        GRANDE   : más de 5.000.000
        MEDIANO  : entre 1.000.001 y 5.000.000
        PEQUEÑO  : entre 100.001 y 1.000.000
        MÍNIMO   : entre 1 y 100.000
        SIN VALOR: 0

    Args:
        valor (float): Valor declarado.

    Returns:
        str: Categoría del contribuyente.
    """
    # TODO:
    # Escribe un bloque if/elif/elif/elif/else con las condiciones en
    # orden de mayor a menor (primero la más restrictiva):
    # - si valor > 5_000_000: retorna "GRANDE"
    # - elif valor > 1_000_000: retorna "MEDIANO"
    # - elif valor > 100_000: retorna "PEQUEÑO"
    # - elif valor > 0: retorna "MÍNIMO"
    # - else: retorna "SIN VALOR"
    pass


def describir_periodo(periodo):
    """
    Retorna el trimestre al que pertenece un período.

    Args:
        periodo (str): Período en formato YYYYMM (ej: "202401").

    Returns:
        str: Nombre del trimestre, o "Período no reconocido".

    Ejemplos:
        describir_periodo("202401")  -> "Primer trimestre"
        describir_periodo("202407")  -> "Tercer trimestre"
        describir_periodo("abc")     -> "Período no reconocido"
    """
    # TODO:
    # 1. Verifica si el formato es válido:
    #    si len(periodo) != 6 OR NOT periodo.isdigit():
    #    retorna "Período no reconocido"
    # 2. Extrae el mes: mes = int(periodo[4:])
    #    (los últimos dos caracteres son el mes)
    # 3. Escribe un if/elif/elif/elif:
    #    - si mes >= 1 and mes <= 3: retorna "Primer trimestre"
    #    - elif mes >= 4 and mes <= 6: retorna "Segundo trimestre"
    #    - elif mes >= 7 and mes <= 9: retorna "Tercer trimestre"
    #    - elif mes >= 10 and mes <= 12: retorna "Cuarto trimestre"
    # 4. Al final: retorna "Período no reconocido" (si el mes no es 1-12)
    pass


def calcular_sancion_basica(dias_mora, valor_base):
    """
    Calcula la sanción por mora según los días de atraso.

    Tasas:
        0 días     :  0 %
        1-30 días  :  1 %
        31-60 días :  3 %
        61-90 días :  5 %
        > 90 días  : 10 %

    Args:
        dias_mora (int): Días de mora.
        valor_base (float): Valor sobre el que se aplica la sanción.

    Returns:
        float: Valor de la sanción.

    Ejemplos:
        calcular_sancion_basica(0, 1_000_000)    -> 0.0
        calcular_sancion_basica(15, 1_000_000)   -> 10000.0
        calcular_sancion_basica(100, 1_000_000)  -> 100000.0
    """
    # TODO:
    # 1. Usa if/elif/elif/elif/else para asignar la tasa según dias_mora:
    #    - si dias_mora == 0: tasa = 0.0
    #    - elif dias_mora <= 30: tasa = 0.01
    #    - elif dias_mora <= 60: tasa = 0.03
    #    - elif dias_mora <= 90: tasa = 0.05
    #    - else: tasa = 0.10
    # 2. Calcula: sancion = valor_base * tasa
    # 3. Retorna sancion.
    pass


def priorizar_cobro(valor, dias_mora, tipo_contribuyente):
    """
    Asigna una prioridad de cobro de P1 (más urgente) a P5 (menos urgente).

    Args:
        valor (float): Valor declarado.
        dias_mora (int): Días de mora.
        tipo_contribuyente (str): "GRANDE", "MEDIANO" o "PEQUEÑO".

    Returns:
        str: Prioridad de cobro ("P1", "P2", "P3", "P4" o "P5").
    """
    # TODO:
    # 1. Calcula variables de apoyo antes del if/elif:
    #    mora_alta = dias_mora > 60
    #    mora_media = dias_mora > 30 and dias_mora <= 60
    #    valor_alto = valor > 1_000_000
    # 2. Escribe un if/elif encadenado combinando las tres variables.
    #    Las reglas son tuyas, pero deben ser consistentes:
    #    los casos más graves (GRANDE + mora_alta) van primero → P1
    #    los casos menos urgentes van al final → P5
    # 3. El else final retorna "P5".
    pass


# ---------------------------------------------------------------------------
# CICLOS FOR
# ---------------------------------------------------------------------------

def imprimir_nits_validos(nits):
    """
    Imprime solo los NITs válidos de una lista, numerados desde 1.

    Procedimiento: no retorna nada.

    Args:
        nits (list): Lista de NITs como cadenas de texto.
    """
    # TODO:
    # 1. Imprime el encabezado: print("NITs válidos:")
    # 2. Inicializa un contador: contador = 1
    # 3. Recorre la lista con: for nit in nits:
    #    - Llama a validar_nit(nit)
    #    - Si es válido: imprime "  {contador}. {nit}"
    #      e incrementa: contador = contador + 1
    pass


def calcular_totales(valores):
    """
    Calcula el total, el promedio y el valor máximo de una lista.

    Usa acumuladores manuales con ciclo for.
    No usa sum(), max() ni statistics.

    Args:
        valores (list): Lista de valores numéricos. Debe tener al menos
                        un elemento.

    Returns:
        tuple: (total, promedio, maximo)

    Ejemplo:
        total, promedio, maximo = calcular_totales([100, 200, 300])
        # total=600, promedio=200.0, maximo=300
    """
    # TODO:
    # 1. Inicializa el acumulador: total = 0
    # 2. Inicializa el máximo con el primer elemento: maximo = valores[0]
    #    (así tenemos un valor real con el que comparar en el ciclo)
    # 3. Recorre con: for valor in valores:
    #    - Acumula: total = total + valor
    #    - Actualiza el máximo: si valor > maximo, haz maximo = valor
    # 4. Calcula el promedio: promedio = total / len(valores)
    # 5. Retorna total, promedio, maximo (los tres en esa línea)
    pass


def generar_periodos_multiple(anio_inicio, anio_fin, meses_por_anio=12):
    """
    Genera los códigos de período para un rango de años.

    Usa dos ciclos for anidados: el externo recorre los años,
    el interno genera los meses de cada año.

    Args:
        anio_inicio (int): Primer año a incluir.
        anio_fin (int): Último año a incluir.
        meses_por_anio (int): Cuántos meses generar por año.

    Returns:
        list: Lista de cadenas en formato YYYYMM.

    Ejemplo:
        generar_periodos_multiple(2024, 2025, 3)
        -> ['202401', '202402', '202403', '202501', '202502', '202503']
    """
    # TODO:
    # 1. Crea una lista vacía: periodos = []
    # 2. Ciclo externo: for anio in range(anio_inicio, anio_fin + 1):
    #    (el +1 es para que anio_fin quede incluido)
    # 3. Ciclo interno: for mes in range(1, meses_por_anio + 1):
    #    - Construye el código: codigo = f"{anio}{mes:02d}"
    #      (el :02d formatea el mes con cero a la izquierda: 1 -> "01")
    #    - Agrega a la lista: periodos.append(codigo)
    # 4. Retorna periodos
    pass


# ---------------------------------------------------------------------------
# CICLOS WHILE
# ---------------------------------------------------------------------------

def buscar_primer_valido(nits):
    """
    Busca el primer NIT válido en una lista usando while.

    Args:
        nits (list): Lista de NITs como cadenas de texto.

    Returns:
        str | None: El primer NIT válido, o None si no hay ninguno.
    """
    # TODO:
    # 1. Inicializa el índice: indice = 0
    # 2. Escribe: while indice < len(nits):
    #    - Extrae el elemento: nit = nits[indice]
    #    - Si validar_nit(nit) es True: retorna nit
    #    - Incrementa: indice = indice + 1
    #      (esta línea va SIEMPRE dentro del while, válido o no)
    # 3. Si el while termina sin retornar: retorna None
    pass


def sumar_hasta_limite(valores, limite):
    """
    Acumula valores de la lista mientras el total no supere el límite.

    Args:
        valores (list): Lista de valores numéricos.
        limite (float): Tope máximo de acumulación.

    Returns:
        tuple: (cantidad_procesada, total_acumulado)

    Ejemplo:
        sumar_hasta_limite([1_500_000, 850_000, 2_300_000], 3_000_000)
        -> (2, 2350000)
    """
    # TODO:
    # 1. Inicializa: total = 0, cantidad = 0, indice = 0
    # 2. Escribe: while indice < len(valores):
    #    - Extrae: valor_actual = valores[indice]
    #    - Si total + valor_actual > limite: break (sal del ciclo)
    #    - Acumula: total = total + valor_actual
    #    - Incrementa: cantidad = cantidad + 1
    #    - Incrementa: indice = indice + 1
    # 3. Retorna cantidad, total
    pass


def encontrar_primer_sobre_umbral(valores, umbral):
    """
    Busca el primer valor de la lista que supere el umbral.

    Args:
        valores (list): Lista de valores numéricos.
        umbral (float): Valor que debe superarse.

    Returns:
        float | None: El primer valor que supera el umbral, o None.

    Ejemplos:
        encontrar_primer_sobre_umbral([850_000, 950_000, 2_300_000], 2_000_000)
        -> 2300000
        encontrar_primer_sobre_umbral([100, 200, 300], 5_000_000)
        -> None
    """
    # TODO:
    # 1. Inicializa: indice = 0
    # 2. Escribe: while indice < len(valores):
    #    - Extrae: valor_actual = valores[indice]
    #    - Si valor_actual > umbral: retorna valor_actual
    #    - Incrementa: indice = indice + 1
    # 3. Si el while termina sin retornar: retorna None
    pass


def validar_secuencia_periodos(periodos):
    """
    Verifica que una lista de períodos esté en orden consecutivo.

    Args:
        periodos (list): Lista de códigos en formato YYYYMM.

    Returns:
        tuple: (es_valida, indice_salto)
            es_valida (bool): True si la secuencia es consecutiva.
            indice_salto (int | None): Posición del primer salto, o None.

    Ejemplos:
        validar_secuencia_periodos(["202401", "202402", "202403"])
        -> (True, None)
        validar_secuencia_periodos(["202401", "202403"])
        -> (False, 1)
    """
    # TODO:
    # 1. Si len(periodos) <= 1: retorna True, None (no hay nada que comparar)
    # 2. Inicializa: indice = 0
    # 3. Escribe: while indice < len(periodos) - 1:
    #    - Lee el período actual y el siguiente usando indice e indice + 1
    #    - Extrae el año y mes de cada uno con int() y slicing:
    #      anio_actual = int(periodos[indice][:4])
    #      mes_actual  = int(periodos[indice][4:])
    #    - Calcula el mes y año esperados para el siguiente período:
    #      si mes_actual == 12: el siguiente es enero del año siguiente
    #      de lo contrario: el siguiente es mes_actual + 1 del mismo año
    #    - Compara con el período siguiente real
    #    - Si hay un salto: retorna False, indice + 1
    #    - Incrementa: indice = indice + 1
    # 4. Si el while termina sin encontrar salto: retorna True, None
    pass


# ---------------------------------------------------------------------------
# LISTAS
# ---------------------------------------------------------------------------

def agregar_unico(lista, elemento):
    """
    Agrega un elemento a la lista solo si no está ya presente.

    Args:
        lista (list): Lista de elementos.
        elemento: Elemento a agregar (cualquier tipo).

    Returns:
        list: Lista con el elemento, o sin cambios si ya existía.

    Ejemplos:
        agregar_unico(["ACTIVO", "INACTIVO"], "PENDIENTE")
        -> ["ACTIVO", "INACTIVO", "PENDIENTE"]

        agregar_unico(["ACTIVO", "INACTIVO"], "ACTIVO")
        -> ["ACTIVO", "INACTIVO"]
    """
    # TODO:
    # 1. Si elemento NOT in lista:
    #    - lista.append(elemento)
    # 2. Retorna lista
    pass


def filtrar_valores_en_rango(valores, minimo, maximo):
    """
    Retorna una nueva lista con los valores dentro del rango dado.

    La lista original no se modifica.

    Args:
        valores (list): Lista de valores numéricos.
        minimo (float): Límite inferior del rango (inclusive).
        maximo (float): Límite superior del rango (inclusive).

    Returns:
        list: Lista filtrada.

    Ejemplo:
        filtrar_valores_en_rango([100, 500, 1000, 1500], 400, 1100)
        -> [500, 1000]
    """
    # TODO:
    # 1. Crea una lista vacía: resultado = []
    # 2. Recorre: for valor in valores:
    #    - Verifica: esta_en_rango = valor >= minimo and valor <= maximo
    #    - Si esta_en_rango: resultado.append(valor)
    # 3. Retorna resultado
    pass


def ordenar_valores(valores, descendente=True):
    """
    Retorna una nueva lista ordenada usando el algoritmo de burbuja.

    El algoritmo compara pares de elementos adyacentes e intercambia
    los que están en el orden incorrecto, repitiendo hasta ordenar todo.

    No usa .sort() ni sorted().

    Args:
        valores (list): Lista de valores numéricos.
        descendente (bool): True para orden descendente. Por defecto True.

    Returns:
        list: Lista ordenada. La original no se modifica.

    Ejemplo:
        ordenar_valores([1_500_000, 850_000, 2_300_000, 450_000])
        -> [2300000, 1500000, 850000, 450000]
    """
    # TODO:
    # 1. Copia la lista para no modificar la original:
    #    resultado = list(valores)
    # 2. Guarda la longitud: n = len(resultado)
    # 3. Ciclo externo: for i in range(n):
    # 4. Ciclo interno: for j in range(0, n - i - 1):
    #    - Si descendente es True:
    #      deben_intercambiarse = resultado[j] < resultado[j + 1]
    #    - Si descendente es False:
    #      deben_intercambiarse = resultado[j] > resultado[j + 1]
    #    - Si deben_intercambiarse:
    #      usa una variable temporal para intercambiar los dos elementos:
    #        temporal = resultado[j]
    #        resultado[j] = resultado[j + 1]
    #        resultado[j + 1] = temporal
    # 5. Retorna resultado
    pass


# ---------------------------------------------------------------------------
# DICCIONARIOS
# A partir de aquí los ejercicios usan DECLARACIONES.
# ---------------------------------------------------------------------------

def indexar_por_nit(declaraciones):
    """
    Construye un diccionario donde la clave es el NIT y el valor
    es el registro completo de esa declaración.

    Args:
        declaraciones (list): Lista de registros de declaraciones.

    Returns:
        dict: Diccionario indexado por NIT.

    Ejemplo:
        indice = indexar_por_nit(DECLARACIONES)
        indice["600456789"]["nombre"]  -> "Industrias PQR S.A."
    """
    # TODO:
    # 1. Crea un diccionario vacío: indice = {}
    # 2. Recorre: for declaracion in declaraciones:
    #    - Extrae: nit = declaracion["nit"]
    #    - Agrega al índice: indice[nit] = declaracion
    # 3. Retorna indice
    pass


def construir_resumen_por_estado(declaraciones):
    """
    Agrupa las declaraciones por estado y acumula conteo y total.

    Args:
        declaraciones (list): Lista de registros de declaraciones.

    Returns:
        dict: Diccionario donde cada clave es un estado y el valor es
              un diccionario con "conteo" y "total_valor".

    Ejemplo de salida:
        {
            "ACTIVO":     {"conteo": 5, "total_valor": 9150000},
            "INACTIVO":   {"conteo": 1, "total_valor": 0},
        }
    """
    # TODO:
    # 1. Crea un diccionario vacío: resumen = {}
    # 2. Recorre: for declaracion in declaraciones:
    #    - Extrae: estado = declaracion["estado"]
    #    - Extrae: valor  = declaracion["valor"]
    #    - Si estado NOT in resumen:
    #      inicializa: resumen[estado] = {"conteo": 0, "total_valor": 0}
    #    - Acumula:
    #      resumen[estado]["conteo"] = resumen[estado]["conteo"] + 1
    #      resumen[estado]["total_valor"] = resumen[estado]["total_valor"] + valor
    # 3. Retorna resumen
    pass


def agrupar_por_municipio(declaraciones):
    """
    Agrupa los registros por municipio.

    Args:
        declaraciones (list): Lista de registros de declaraciones.

    Returns:
        dict: Diccionario donde cada clave es un municipio y el valor
              es una lista con todos los registros de ese municipio.
    """
    # TODO:
    # 1. Crea un diccionario vacío: grupos = {}
    # 2. Recorre: for declaracion in declaraciones:
    #    - Extrae: municipio = declaracion["municipio"]
    #    - Si municipio NOT in grupos:
    #      inicializa: grupos[municipio] = []
    #    - Agrega: grupos[municipio].append(declaracion)
    # 3. Retorna grupos
    pass


def imprimir_agrupacion(agrupacion):
    """
    Procedimiento: imprime un resumen formateado por municipio.

    Args:
        agrupacion (dict): Resultado de agrupar_por_municipio().
    """
    # TODO:
    # 1. Imprime el encabezado:
    #    print("Resumen por municipio:")
    #    print(f"  {'Municipio':<15} {'Declaraciones':>14} {'Total':>14}")
    #    print("  " + "-" * 45)
    # 2. Recorre: for municipio in agrupacion:
    #    - registros = agrupacion[municipio]
    #    - cantidad = len(registros)
    #    - Calcula el total con un ciclo for:
    #        total = 0
    #        for registro in registros:
    #            total = total + registro["valor"]
    #    - Imprime la fila:
    #      print(f"  {municipio:<15} {cantidad:>14} ${total:>13,}")
    pass


def calcular_estadisticas(declaraciones):
    """
    Calcula estadísticas generales d    Calcula estadísticas generales del conjunto de declaraciones.

    Args:
        declaraciones (list): Lista de registros de declaraciones.

    Returns:
        dict: Con las claves total_registros, total_activos,
              suma_valores, promedio_valor_activos, valor_maximo.
    """
    # TODO:
    # 1. Inicializa contadores antes del ciclo:
    #    total_registros = len(declaraciones)
    #    total_activos = 0
    #    suma_valores = 0
    #    suma_valores_activos = 0
    #    valor_maximo = 0
    # 2. Recorre: for declaracion in declaraciones:
    #    - Extrae: valor = declaracion["valor"]
    #    - Acumula suma_valores
    #    - Actualiza valor_maximo si valor > valor_maximo
    #    - Si declaracion["estado"] == "ACTIVO":
    #        acumula total_activos y suma_valores_activos
    # 3. Calcula el promedio (cuidado: evita división por cero):
    #    si total_activos > 0: promedio_activos = suma_valores_activos / total_activos
    #    else: promedio_activos = 0
    # 4. Construye y retorna el diccionario de estadísticas con las claves:
    #    "total_registros", "total_activos", "suma_valores",
    #    "promedio_valor_activos", "valor_maximo"
    pass


def filtrar_por_estado(declaraciones, estado):
    """
    Retorna una nueva lista con solo los registros del estado indicado.

    Args:
        declaraciones (list): Lista de registros de declaraciones.
        estado (str): Estado a filtrar.

    Returns:
        list: Registros que coinciden con el estado.
    """
    # TODO:
    # 1. Crea una lista vacía: resultado = []
    # 2. Recorre: for declaracion in declaraciones:
    #    - Si declaracion["estado"] == estado:
    #        resultado.append(declaracion)
    # 3. Retorna resultado
    pass


def buscar_por_nit(declaraciones, nit_buscado):
    """
    Busca la primera declaración con el NIT indicado usando while.

    Args:
        declaraciones (list): Lista de registros de declaraciones.
        nit_buscado (str): NIT a buscar.

    Returns:
        dict | None: El primer registro con ese NIT, o None si no existe.

    Ejemplo:
        resultado = buscar_por_nit(DECLARACIONES, "600456789")
        resultado["nombre"]  -> "Industrias PQR S.A."
    """
    # TODO:
    # 1. Inicializa: indice = 0
    # 2. Escribe: while indice < len(declaraciones):
    #    - declaracion = declaraciones[indice]
    #    - Si declaracion["nit"] == nit_buscado: retorna declaracion
    #    - Incrementa: indice = indice + 1
    #      (avanzamos aunque no coincida, para no quedarnos en el mismo lugar)
    # 3. Si el while termina sin retornar: retorna None
    pass
