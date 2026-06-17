import csv

Archivo_CSV = "Paises.csv"
Campos = ["Nombre","Poblacion","Superficie","Continente"]

def validacion_nombre(texto, campo):
    if texto.strip() == "":
        raise ValueError(f"{campo} no puede estar vacío")

def validacion_numerica(valor, campo):
    if valor <= 0:
        raise ValueError(f"{campo} debe ser mayor a 0")
def validacion_rango(minimo, maximo):
    if minimo > maximo:
        raise ValueError("El mínimo no puede ser mayor al máximo")
def validar_pais_existente(nombre, paises):
    for pais in paises:
        if pais["Nombre"].lower() == nombre.lower():
            return

    raise ValueError("El país no existe")

def menu():
        print("Bienvenido al menú principal")
        print("1. Agregar país")
        print("2. Buscar país")
        print("3. Salir")
        print
        
        