# producto.py
# Autor: Fernando Reyes
# Versión: 1.0
# Fecha: 9 de abril de 2025

class Producto:
    def __init__(self, nombre, categoria, precio, stock):
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def agregar_stock(self, cantidad):
        self.stock += cantidad

    def retirar_stock(self, cantidad):
        if cantidad <= self.stock:
            self.stock -= cantidad
        else:
            print("No hay suficiente stock.")

    def mostrar_info(self):
        print(f"\n--- Información del Producto ---")
        print("Nombre:", self.nombre)
        print("Categoría:", self.categoria)
        print("Precio: C$", self.precio)
        print("Stock:", self.stock)
        print("Valor total en inventario: C$", self.precio * self.stock)