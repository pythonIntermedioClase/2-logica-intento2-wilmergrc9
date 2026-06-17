# main.py
# Proyecto: Procesamiento de datos - DIAN 2026
# Sesión 2: funciones, condicionales, ciclos, listas y diccionarios
#
# Ejecutar con: python main.py
#
# Instrucciones:
#   1. Completa cada función en src/utils.py siguiendo los comentarios TODO.
#   2. Descomenta el bloque correspondiente en este archivo.
#   3. Ejecuta python main.py y verifica la salida esperada.
#   4. Agrega, haz commit y sube los cambios con git push.


# ---------------------------------------------------------------------------
# Imports
# Descomenta cada import cuando empieces a trabajar en esa sección.
# ---------------------------------------------------------------------------

from src.utils import calcular_iva
from src.utils import formatear_reporte_valor
from src.utils import mostrar_resultado
from src.utils import generar_ficha_contribuyente

from src.utils import procesar_nit
from src.utils import pipeline_nit

from src.utils import esta_al_dia
from src.utils import aplicar_descuento
from src.utils import asignar_prioridad

from src.utils import clasificar_mora
from src.utils import determinar_tipo_seguimiento
from src.utils import evaluar_cumplimiento

from src.utils import clasificar_contribuyente
from src.utils import describir_periodo
from src.utils import calcular_sancion_basica
from src.utils import priorizar_cobro

from src.utils import imprimir_nits_validos
from src.utils import calcular_totales
from src.utils import generar_periodos_multiple

from src.utils import buscar_primer_valido
from src.utils import sumar_hasta_limite
from src.utils import encontrar_primer_sobre_umbral
from src.utils import validar_secuencia_periodos

from src.utils import agregar_unico
from src.utils import filtrar_valores_en_rango
from src.utils import ordenar_valores

from src.utils import DECLARACIONES
from src.utils import indexar_por_nit
from src.utils import construir_resumen_por_estado
from src.utils import agrupar_por_municipio
from src.utils import imprimir_agrupacion
from src.utils import calcular_estadisticas
from src.utils import filtrar_por_estado
from src.utils import buscar_por_nit


# ---------------------------------------------------------------------------
# Opciones del menú
# Cada función agrupa las llamadas de una sección del proyecto.
# Descomenta el cuerpo cuando hayas implementado las funciones en utils.py.
# ---------------------------------------------------------------------------

def menu_funciones_basicas():
    """Sección 1: funciones y procedimientos con tipos simples."""
    print("\n--- Funciones básicas ---")

    # TODO: descomenta cuando hayas completado calcular_iva
    valor = 1_500_000
    iva = calcular_iva(valor)
    print("El valor del IVA es ", iva)
    
    
    mostrar_resultado(f"IVA sobre ${valor:,.0f}", iva)

    # TODO: descomenta cuando hayas completado formatear_reporte_valor
    linea = formatear_reporte_valor("900123456", "Empresa ABC S.A.S.", 1_500_000, "ACTIVO")
    print(f"  Reporte: {linea}")

    # TODO: descomenta cuando hayas completado generar_ficha_contribuyente
    ficha = generar_ficha_contribuyente(
         "900123456", "Empresa ABC S.A.S.", "Bogota", "202401", 1_500_000, "ACTIVO"
     )
    print(ficha)
    pass


def menu_encadenamiento():
    """Sección 2: encadenamiento de funciones."""
    print("\n--- Encadenamiento de funciones ---")

    # TODO: descomenta cuando hayas completado limpiar_nit y validar_nit
    casos = ["900-123-456", "800.234.567", "ABC123", "123", "8001234560"]
    for nit in casos:
        resultado = procesar_nit(nit)
        print(f"  {resultado}")

    # TODO: descomenta cuando hayas completado pipeline_nit
    print()
    for nit in casos:
         informe = pipeline_nit(nit)
         print(f"  {informe}")
    #pass


def menu_condicionales_simples():
    """Sección 3: condicionales simples."""
    print("\n--- Condicionales simples ---")

    # TODO: descomenta cuando hayas completado esta_al_dia
    casos_mora = [0, 1, 30, 90]
    for dias in casos_mora:
         al_dia = esta_al_dia(dias)
         estado = "Al día" if al_dia else "En mora"
         print(f"  {dias} días de mora → {estado}")

    # TODO: descomenta cuando hayas completado aplicar_descuento
    # valor_base = 1_000_000
    # con_descuento = aplicar_descuento(valor_base, True)
    # sin_descuento = aplicar_descuento(valor_base, False)
    # mostrar_resultado("Con descuento voluntario", con_descuento)
    # mostrar_resultado("Sin descuento", sin_descuento)

    # TODO: descomenta cuando hayas completado asignar_prioridad
    # casos = [(2_000_000, True), (2_000_000, False), (500_000, True), (500_000, False)]
    # for valor, historial in casos:
    #     prioridad = asignar_prioridad(valor, historial)
    #     print(f"  ${valor:,} / historial={historial} → {prioridad}")
    #pass


def menu_condicionales_anidados():
    """Sección 4: condicionales anidados."""
    print("\n--- Condicionales anidados ---")

    # TODO: descomenta cuando hayas completado clasificar_mora
    # casos = [(0, 0), (15, 800_000), (15, 200_000)]
    # for dias, valor in casos:
    #     clasificacion = clasificar_mora(dias, valor)
    #     print(f"  {dias} días / ${valor:,} → {clasificacion}")

    # TODO: descomenta cuando hayas completado determinar_tipo_seguimiento
    # registros_prueba = [
    #     ("ACTIVO", 2_500_000, "Bogota"),
    #     ("ACTIVO", 500_000, "Cali"),
    #     ("PENDIENTE", 1_000_000, "Medellin"),
    #     ("INACTIVO", 0, "Barranquilla"),
    # ]
    # for estado, valor, mun in registros_prueba:
    #     tipo = determinar_tipo_seguimiento(estado, valor, mun)
    #     print(f"  {estado} / ${valor:,} / {mun} → {tipo}")
    pass


def menu_condicionales_encadenados():
    """Sección 5: condicionales encadenados."""
    print("\n--- Condicionales encadenados ---")

    # TODO: descomenta cuando hayas completado clasificar_contribuyente
    # valores = [0, 50_000, 500_000, 2_000_000, 6_000_000]
    # for valor in valores:
    #     categoria = clasificar_contribuyente(valor)
    #     print(f"  ${valor:,} → {categoria}")

    # TODO: descomenta cuando hayas completado calcular_sancion_basica
    # dias_prueba = [0, 15, 45, 75, 120]
    # valor_base = 1_000_000
    # for dias in dias_prueba:
    #     sancion = calcular_sancion_basica(dias, valor_base)
    #     print(f"  {dias} días de mora → sanción: ${sancion:,.0f}")
    pass


def menu_ciclos_for():
    """Sección 6: ciclos for."""
    print("\n--- Ciclos for ---")

    # TODO: descomenta cuando hayas completado imprimir_nits_validos
    # nits_prueba = ["900123456", "ABC123", "800234567", "123", "400678901"]
    # imprimir_nits_validos(nits_prueba)

    # TODO: descomenta cuando hayas completado calcular_totales
    # valores = [1_500_000, 850_000, 0, 2_300_000, 950_000, 3_200_000, 450_000, 1_100_000]
    # total, promedio, maximo = calcular_totales(valores)
    # mostrar_resultado("Total", total)
    # mostrar_resultado("Promedio", promedio)
    # mostrar_resultado("Máximo", maximo)

    # TODO: descomenta cuando hayas completado generar_periodos_multiple
    # periodos = generar_periodos_multiple(2024, 2025, 3)
    # print(f"  Períodos generados: {periodos}")
    pass


def menu_ciclos_while():
    """Sección 7: ciclos while y variables bandera."""
    print("\n--- Ciclos while ---")

    # TODO: descomenta cuando hayas completado buscar_primer_valido
    # nits_mixtos = ["ABC123", "123", "900123456", "800234567"]
    # primer_valido = buscar_primer_valido(nits_mixtos)
    # print(f"  Primer NIT válido encontrado: {primer_valido}")

    # TODO: descomenta cuando hayas completado sumar_hasta_limite
    # valores = [1_500_000, 850_000, 2_300_000, 950_000]
    # cantidad, total = sumar_hasta_limite(valores, 3_000_000)
    # print(f"  Procesados {cantidad} registros antes de superar el límite")
    # mostrar_resultado("Total acumulado", total)

    # TODO: descomenta cuando hayas completado encontrar_primer_sobre_umbral
    # umbral = 2_000_000
    # encontrado = encontrar_primer_sobre_umbral(valores, umbral)
    # if encontrado is not None:
    #     print(f"  Primer valor sobre ${umbral:,}: ${encontrado:,}")
    # else:
    #     print(f"  Ningún valor supera ${umbral:,}")
    pass


def menu_listas():
    """Sección 8: listas."""
    print("\n--- Listas ---")

    # TODO: descomenta cuando hayas completado filtrar_valores_en_rango
    # valores = [1_500_000, 850_000, 0, 2_300_000, 950_000, 3_200_000, 450_000, 1_100_000]
    # en_rango = filtrar_valores_en_rango(valores, 500_000, 2_000_000)
    # print(f"  Valores entre $500,000 y $2,000,000: {en_rango}")

    # TODO: descomenta cuando hayas completado ordenar_valores
    # ordenados = ordenar_valores(valores)
    # print(f"  Ordenados descendente: {ordenados}")
    # ordenados_asc = ordenar_valores(valores, descendente=False)
    # print(f"  Ordenados ascendente: {ordenados_asc}")
    pass


def menu_diccionarios():
    """Sección 9: diccionarios con DECLARACIONES."""
    print("\n--- Diccionarios ---")

    # TODO: descomenta cuando hayas completado indexar_por_nit
    # indice = indexar_por_nit(DECLARACIONES)
    # registro = indice.get("600456789")
    # if registro:
    #     print(f"  Encontrado: {registro['nombre']} — ${registro['valor']:,}")

    # TODO: descomenta cuando hayas completado construir_resumen_por_estado
    # resumen = construir_resumen_por_estado(DECLARACIONES)
    # print("\n  Resumen por estado:")
    # for estado in resumen:
    #     datos = resumen[estado]
    #     print(f"    {estado}: {datos['conteo']} registros, ${datos['total_valor']:,}")

    # TODO: descomenta cuando hayas completado agrupar_por_municipio e imprimir_agrupacion
    # print()
    # agrupacion = agrupar_por_municipio(DECLARACIONES)
    # imprimir_agrupacion(agrupacion)

    # TODO: descomenta cuando hayas completado calcular_estadisticas
    # print()
    # stats = calcular_estadisticas(DECLARACIONES)
    # print("  Estadísticas generales:")
    # print(f"    Total registros   : {stats['total_registros']}")
    # print(f"    Registros activos : {stats['total_activos']}")
    # mostrar_resultado("Suma total", stats["suma_valores"])
    # mostrar_resultado("Promedio activos", stats["promedio_valor_activos"])
    # mostrar_resultado("Valor máximo", stats["valor_maximo"])
    pass


# ---------------------------------------------------------------------------
# Menú principal
# ---------------------------------------------------------------------------

OPCIONES = {
    "1": ("Funciones básicas",            menu_funciones_basicas),
    "2": ("Encadenamiento de funciones",  menu_encadenamiento),
    "3": ("Condicionales simples",        menu_condicionales_simples),
    "4": ("Condicionales anidados",       menu_condicionales_anidados),
    "5": ("Condicionales encadenados",    menu_condicionales_encadenados),
    "6": ("Ciclos for",                   menu_ciclos_for),
    "7": ("Ciclos while",                 menu_ciclos_while),
    "8": ("Listas",                       menu_listas),
    "9": ("Diccionarios",                 menu_diccionarios),
    "0": ("Salir",                        None),
}


def mostrar_menu():
    """Imprime las opciones disponibles en el menu."""
    print("\n" + "=" * 50)
    print("  Procesamiento de datos - DIAN 2026")
    print("  Sesion 2")
    print("=" * 50)
    for clave in OPCIONES:
        nombre, _ = OPCIONES[clave]
        print(f"  {clave}. {nombre}")
    print()


def main():
    """Punto de entrada. Ejecuta el menu interactivo con variable bandera."""
    continuar = True
    while continuar:
        mostrar_menu()
        opcion = input("Selecciona una opcion: ").strip()
        if opcion in OPCIONES:
            nombre, funcion = OPCIONES[opcion]
            if funcion is None:
                # La opcion 0 detiene el ciclo asignando False a la bandera.
                # La bandera controla la continuacion sin usar break.
                continuar = False
                print("\nHasta la proxima.\n")
            else:
                funcion()
                input("\n  Presiona Enter para volver al menu...")
        else:
            print(f"\n  Opcion '{opcion}' no reconocida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
