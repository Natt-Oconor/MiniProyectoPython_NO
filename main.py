"""
===============================================================================
SISTEMA DE GESTIÓN DE INVENTARIO - TECHSTORE (Python Script)
===============================================================================
Implementación completa para ejecución directa en terminal o IDE:
- Módulos (modulo_inventario.py y nativos)
- Listas y Diccionarios
- Funciones con y sin parámetros
- Encapsulamiento (@property y atributos privados)
- Herencia y Polimorfismo
- Manejo de Excepciones y Excepción Personalizada
- Menú Interactivo (Entrada, Procesamiento y Salida de Información)
===============================================================================
"""

import datetime
import modulo_inventario as mi
from modulo_inventario import formatear_moneda, generar_codigo_unico


# =============================================================================
# 1. EXCEPCIÓN PERSONALIZADA
# =============================================================================
class StockInsuficienteError(Exception):
    """Excepción lanzada cuando se intenta vender más stock del disponible."""
    def __init__(self, solicitado, disponible):
        super().__init__(f"Stock insuficiente: Solicitado {solicitado}, pero solo hay {disponible} unidades disponibles.")
        self.solicitado = solicitado
        self.disponible = disponible


# =============================================================================
# 2. CLASE BASE: Producto (Encapsulamiento)
# =============================================================================
class Producto:
    """Clase base con atributos privados y getters/setters validados."""
    def __init__(self, codigo, nombre, precio_base, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.__precio_base = 0.0
        self.__stock = 0
        self.precio_base = precio_base
        self.stock = stock

    @property
    def precio_base(self):
        return self.__precio_base

    @precio_base.setter
    def precio_base(self, valor):
        if valor < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.__precio_base = valor

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, cantidad):
        if cantidad < 0:
            raise ValueError("El stock no puede ser negativo.")
        self.__stock = cantidad

    def obtener_resumen(self):
        return f"[{self.codigo}] {self.nombre} - Precio Base: {formatear_moneda(self.precio_base)} | Stock: {self.stock}"

    def calcular_precio_final(self):
        return self.precio_base * (1 + mi.IMPUESTO_IVA)


# =============================================================================
# 3. SUBCLASES: Herencia y Polimorfismo
# =============================================================================
class ProductoElectronico(Producto):
    def __init__(self, codigo, nombre, precio_base, stock, garantia_meses=12):
        super().__init__(codigo, nombre, precio_base, stock)
        self.garantia_meses = garantia_meses

    def calcular_precio_final(self):
        precio_con_iva = super().calcular_precio_final()
        costo_garantia = 15.0 if self.garantia_meses > 12 else 0.0
        return precio_con_iva + costo_garantia

    def obtener_resumen(self):
        return f"{super().obtener_resumen()} | Garantía: {self.garantia_meses} meses (Electrónico)"


class ProductoAlimento(Producto):
    def __init__(self, codigo, nombre, precio_base, stock, dias_para_vencer):
        super().__init__(codigo, nombre, precio_base, stock)
        self.dias_para_vencer = dias_para_vencer

    def calcular_precio_final(self):
        precio_con_iva = super().calcular_precio_final()
        if self.dias_para_vencer <= 3:
            print(f"⚠️ ¡ALERTA LIQUIDACIÓN! {self.nombre} vence en {self.dias_para_vencer} días (40% OFF).")
            return precio_con_iva * 0.60
        return precio_con_iva

    def obtener_resumen(self):
        return f"{super().obtener_resumen()} | Vence en: {self.dias_para_vencer} días (Alimento)"


# =============================================================================
# 4. FUNCIONES AUXILIARES
# =============================================================================
def mostrar_banner():
    print("=" * 70)
    print("       🏬 SISTEMA DE GESTIÓN DE INVENTARIO - TECHSTORE")
    print("=" * 70)


def procesar_venta(producto, cantidad_deseada):
    print(f"\n🛒 Intentando comprar {cantidad_deseada} unidades de '{producto.nombre}'...")
    try:
        if not isinstance(cantidad_deseada, int) or cantidad_deseada <= 0:
            raise TypeError("La cantidad debe ser un número entero positivo mayor a cero.")
            
        if cantidad_deseada > producto.stock:
            raise StockInsuficienteError(cantidad_deseada, producto.stock)
            
        producto.stock -= cantidad_deseada
        total_pagar = producto.calcular_precio_final() * cantidad_deseada
        print(f"✅ Venta exitosa. Total cobrado: {formatear_moneda(total_pagar)}")
        print(f"📦 Stock restante de '{producto.nombre}': {producto.stock} unidades.")
        
    except StockInsuficienteError as error_stock:
        print(f"❌ ERROR DE STOCK: {error_stock}")
    except TypeError as error_tipo:
        print(f"❌ ERROR DE DATO: {error_tipo}")
    except Exception as error_general:
        print(f"❌ ERROR INESPERADO: {error_general}")
    finally:
        print("🔹 (Bloque 'finally': Operación finalizada e historial de auditoría actualizado).")


# =============================================================================
# 5. GESTOR DE INVENTARIO (Listas y Diccionarios)
# =============================================================================
class GestorInventario:
    def __init__(self, nombre_tienda):
        self.nombre_tienda = nombre_tienda
        self.inventario_lista = []
        self.inventario_dict = {}

    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden agregar objetos que deriven de la clase Producto.")
        self.inventario_lista.append(producto)
        self.inventario_dict[producto.codigo] = producto
        print(f"➕ Producto registrado: [{producto.codigo}] {producto.nombre}")

    def buscar_por_codigo(self, codigo):
        try:
            return self.inventario_dict[codigo]
        except KeyError:
            print(f"⚠️ Error: El producto con código '{codigo}' no existe en la tienda.")
            return None

    def mostrar_reporte_completo(self):
        mostrar_banner()
        print(f"📍 REPORTE GENERAL DE INVENTARIO | {mi.obtener_timestamp()}")
        print("-" * 85)
        
        total_valor_inventario = 0.0
        for prod in self.inventario_lista:
            print(prod.obtener_resumen())
            precio_f = prod.calcular_precio_final()
            valor_subtotal = precio_f * prod.stock
            total_valor_inventario += valor_subtotal
            print(f"   💰 Precio Final c/Impuesto: {formatear_moneda(precio_f)} | Valor Total Stock: {formatear_moneda(valor_subtotal)}\n")
            
        print("=" * 85)
        print(f"💵 VALOR TOTAL DEL INVENTARIO EN TIENDA: {formatear_moneda(total_valor_inventario)}")
        print("=" * 85)


# =============================================================================
# 6. MENÚ INTERACTIVO (Entrada, Procesamiento y Salida)
# =============================================================================
def menu_interactivo(tienda):
    while True:
        print("\n" + "=" * 55)
        print(f"   🏬 MENÚ DE CONTROL INTERACTIVO - {tienda.nombre_tienda.upper()}")
        print("=" * 55)
        print("1. ➕ Registrar Producto Electrónico")
        print("2. 🥖 Registrar Producto Alimento")
        print("3. 🛒 Realizar Venta (Validación de Stock y Excepciones)")
        print("4. 📊 Ver Reporte General de Inventario")
        print("5. 🚪 Salir del Sistema")
        print("=" * 55)
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            try:
                nombre = input("Nombre del producto electrónico: ").strip()
                if not nombre:
                    raise ValueError("El nombre no puede estar vacío.")
                precio = float(input("Precio base ($): "))
                stock = int(input("Cantidad inicial en stock: "))
                garantia = int(input("Meses de garantía (ej. 12, 24): "))
                
                codigo = mi.generar_codigo_unico("ELEC")
                nuevo_prod = ProductoElectronico(codigo, nombre, precio, stock, garantia)
                tienda.agregar_producto(nuevo_prod)
                print(f"✅ ¡Producto registrado con éxito! Código asignado: {codigo}")
            except ValueError as e:
                print(f"❌ ERROR EN ENTRADA: {e}")
                
        elif opcion == "2":
            try:
                nombre = input("Nombre del alimento: ").strip()
                if not nombre:
                    raise ValueError("El nombre no puede estar vacío.")
                precio = float(input("Precio base ($): "))
                stock = int(input("Cantidad inicial en stock: "))
                dias_vence = int(input("Días para que venza (ej. 2, 15): "))
                
                codigo = mi.generar_codigo_unico("ALIM")
                nuevo_prod = ProductoAlimento(codigo, nombre, precio, stock, dias_vence)
                tienda.agregar_producto(nuevo_prod)
                print(f"✅ ¡Alimento registrado con éxito! Código asignado: {codigo}")
            except ValueError as e:
                print(f"❌ ERROR EN ENTRADA: {e}")

        elif opcion == "3":
            codigo = input("Ingrese el código del producto a vender (ej. ELEC-101): ").strip().upper()
            prod = tienda.buscar_por_codigo(codigo)
            if prod:
                try:
                    cant = int(input(f"Stock disponible de '{prod.nombre}' ({prod.stock} uds). ¿Cuántas desea comprar?: "))
                    procesar_venta(prod, cant)
                except ValueError:
                    print("❌ ERROR: Debe ingresar un número entero válido.")
                    
        elif opcion == "4":
            tienda.mostrar_reporte_completo()
            
        elif opcion == "5":
            print("\n👋 Gracias por utilizar el Sistema de Gestión TechStore. ¡Hasta pronto!")
            break
        else:
            print("⚠️ Opción inválida. Por favor, ingrese un número del 1 al 5.")


# =============================================================================
# PUNTO DE ENTRADA PRINCIPAL
# =============================================================================
if __name__ == "__main__":
    tienda = GestorInventario("TechStore Costa Rica")
    
    # Cargar 3 productos de prueba iniciales
    prod1 = ProductoElectronico(generar_codigo_unico("TV"), "Smart TV 55 Pulgadas", 550.0, 4, garantia_meses=24)
    prod2 = ProductoAlimento(generar_codigo_unico("SNK"), "Chocolates Gourmet", 8.50, 30, dias_para_vencer=1)
    prod3 = ProductoElectronico(generar_codigo_unico("AUD"), "Audífonos Noise Cancelling", 120.0, 10, garantia_meses=12)
    
    tienda.agregar_producto(prod1)
    tienda.agregar_producto(prod2)
    tienda.agregar_producto(prod3)
    
    # Iniciar menú interactivo
    menu_interactivo(tienda)
