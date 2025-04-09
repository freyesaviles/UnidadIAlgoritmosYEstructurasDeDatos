# main.py
# Programa principal para controlar el inventario
# Autor: Fernando Reyes
# Versión: 1.0
# Fecha: 9 de abril de 2025

from producto import Producto
from funciones import mostrar_menu, pedir_numero, buscar_producto

productos = []

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        categoria = input("Categoría: ")
        precio = pedir_numero("Precio: C$", float)
        stock = pedir_numero("Cantidad en stock: ", int)
        nuevo = Producto(nombre, categoria, precio, stock)
        productos.append(nuevo)
        print("Producto registrado exitosamente.")

    elif opcion == "2":
        nombre = input("Nombre del producto: ")
        prod = buscar_producto(nombre, productos)
        if prod:
            cantidad = pedir_numero("Cantidad a agregar: ", int)
            prod.agregar_stock(cantidad)
            print("Stock actualizado.")
        else:
            print("Producto no encontrado.")

    elif opcion == "3":
        nombre = input("Nombre del producto: ")
        prod = buscar_producto(nombre, productos)
        if prod:
            cantidad = pedir_numero("Cantidad a retirar: ", int)
            prod.retirar_stock(cantidad)
        else:
            print("Producto no encontrado.")

    elif opcion == "4":
        nombre = input("Nombre del producto: ")
        prod = buscar_producto(nombre, productos)
        if prod:
            prod.mostrar_info()
        else:
            print("Producto no encontrado.")

    elif opcion == "5":
        print("¡Gracias por usar el sistema de inventario!")
        break

    else:
        print("Opción no válida.")