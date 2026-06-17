import csv

Archivo_CSV = "Paises.csv"
Campos = ["Nombre","Poblacion","Superficie","Continente"]
def validacion_letras(texto):
    if not texto.isalpha():
        print("Error.Solo letras")
        return False
    return True
def validacion_numero(numero):
    if not numero.isdigit():
        print("Error.Solo numeros")
        return False
    return True
def validacion_float(numero):
    try:
        float(numero)
        return True
    except ValueError:
        print("Error. Debe ser un numero")
        return False
def validacion_nombre(nombre, campos):
    if nombre.strip() == "":
        raise ValueError(f"{campos} no puede estar vacío")

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
        print("1.Agregar país")
        print("2.Actualizar datos de un pais")
        print("3.Buscar país")
        print("4.Filtrar paises cargados")
        print("5.Ordenar paises")
        print("6.Estadisticas")
        print("7. Salir")

def agregar_pais(campos):
    try:
        nombre= input("Nombre del pais: ")
        validacion_nombre(nombre, campos[0])
        if not validacion_letras(nombre):
            return
        poblacion=input("Poblacion: ")
        validacion_numero(poblacion)
        poblacion = int(poblacion)
        validacion_numerica(poblacion, campos[1])
        superficie= input("Superficie: ")
        if not validacion_float(superficie):
            return
        superficie = float(superficie)
        validacion_numerica(superficie, campos[2])
        continente = input("Continente: ")
        validacion_nombre(continente, campos[3])
        with open(Archivo_CSV, "a", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow([nombre, poblacion, superficie, continente])
    except ValueError as error:
        print(error)