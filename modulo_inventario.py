"""
===============================================================================
MÓDULO CUSTOM: modulo_inventario.py
===============================================================================
Este módulo demuestra el uso de MÓDULOS en Python.
Contiene funciones de utilidad reutilizables para el cálculo de impuestos,
formateo de precios y generación de códigos únicos de producto.
===============================================================================
"""

from datetime import datetime
import random

# Constante del módulo
IMPUESTO_IVA = 0.13  # 13% IVA (ejemplo)

def generar_codigo_unico(prefijo="PROD"):
    """
    Función con parámetro por defecto que genera un código de producto.
    Ejemplo: PROD-8472
    """
    numero_aleatorio = random.randint(1000, 9999)
    return f"{prefijo.upper()}-{numero_aleatorio}"

def formatear_moneda(monto):
    """
    Función que recibe un parámetro numérico y devuelve una cadena formateada en moneda ($).
    """
    if not isinstance(monto, (int, float)):
        raise TypeError("El monto debe ser un número entero o flotante.")
    return f"${monto:,.2f}"

def calcular_iva(monto):
    """
    Calcula el IVA correspondiente a un monto dado.
    """
    return monto * IMPUESTO_IVA

def obtener_timestamp():
    """
    Función SIN parámetros que retorna la fecha y hora actual formateada.
    """
    ahora = datetime.now()
    return ahora.strftime("%Y-%m-%d %H:%M:%S")
