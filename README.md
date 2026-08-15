# 🚀 Mini-Proyecto Python para Jupyter Notebook

**Tema**: Sistema de Gestión de Inventario - TechStore  
**Nivel**: Introductorio / Consolidación de Fundamentos

---

## 📌 Requisitos Cumplidos

Este proyecto fue diseñado específicamente para cubrir todos los temas solicitados:

1. **Listas**: Almacenamiento de categorías, catálogo y colección de productos.
2. **Diccionarios**: Estructura de información de tienda y mapeo rápido por clave (`código -> objeto`).
3. **Funciones (con y sin parámetros)**: `mostrar_banner()` (sin parámetros), `calcular_descuento(...)` y `procesar_venta(...)` (con parámetros por defecto).
4. **Encapsulamiento**: Atributos privados `__precio_base` y `__stock` con getters/setters (`@property`).
5. **Herencia**: Clase Padre `Producto` y Clases Hijas `ProductoElectronico` y `ProductoAlimento`.
6. **Polimorfismo**: Métodos `calcular_precio_final()` y `obtener_resumen()` redefinidos de forma distinta en cada subclase.
7. **Manejo de Excepciones**: Uso de `try`, `except`, `else`, `finally` y creación de una excepción personalizada `StockInsuficienteError`.
8. **Módulos**: Importación de módulos estándar (`datetime`, `random`) y un módulo propio `modulo_inventario.py`.

---

## 📂 Archivos del Proyecto

- 📓 **`mini_proyecto_python.ipynb`**: Cuaderno interactivo de Jupyter Notebook con celdas ejecutables y explicaciones.
- ⚙️ **`modulo_inventario.py`**: Módulo Python propio con funciones reutilizables.

---

## 🛠️ ¿Cómo Ejecutar el Proyecto?

### En Jupyter Notebook / JupyterLab:
1. Abre tu consola o terminal.
2. Navega a la carpeta del proyecto:
   ```bash
   cd C:\Users\Carlos.Arauz\.gemini\antigravity\scratch\mini_proyecto_python
   ```
3. Ejecuta Jupyter:
   ```bash
   jupyter notebook mini_proyecto_python.ipynb
   ```

### En Visual Studio Code:
1. Abre la carpeta `C:\Users\Carlos.Arauz\.gemini\antigravity\scratch\mini_proyecto_python` en VS Code.
2. Abre el archivo `mini_proyecto_python.ipynb`.
3. Selecciona tu Kernel de Python y presiona **Run All** o ejecuta celda por celda.
