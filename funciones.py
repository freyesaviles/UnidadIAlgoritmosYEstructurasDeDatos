# funciones.py
# Funciones auxiliares para el control de inventario
# Autor: Fernando Reyes
# Versión: 1.0
# Fecha: 9 de abril de 2025

def mostrar_menu():
    print("\n--- MENÚ ---")
    print("1. Registrar nuevo producto")
    print("2. Agregar stock")
    print("3. Retirar stock")
    print("4. Mostrar información del producto")
    print("5. Salir")

def pedir_numero(mensaje, tipo=float):
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor >= 0:
                return valor
            else:
                print("Por favor ingresa un número positivo.")
        except:
            print("Entrada inválida. Intenta de nuevo.")

def buscar_producto(nombre, lista):
    for p in lista:
        if p.nombre.lower() == nombre.lower():
            return p
    return None