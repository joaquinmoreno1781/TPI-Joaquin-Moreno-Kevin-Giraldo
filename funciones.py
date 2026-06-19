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
    encontrados = []
    for pais in paises:
        if nombre.lower() in pais["Nombre"].lower():
            encontrados.append(pais)
    if len(encontrados) == 0:
        raise ValueError("El país no existe")
    return encontrados

def menu():
        print("Bienvenido al menú principal")
        print("1.Agregar país")
        print("2.Actualizar datos de un pais")
        print("3.Buscar país")
        print("4.Filtrar paises cargados")
        print("5.Ordenar paises")
        print("6.Estadisticas")
        print("7. Salir")
import os
def crear_csv():
    if not os.path.exists(Archivo_CSV):
        with open(Archivo_CSV, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(Campos)
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
        if not validacion_letras(continente):
            return
        with open(Archivo_CSV, "a", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow([nombre, poblacion, superficie, continente])
    except ValueError as error:
        print(error)
def actualizar_datos(paises):
    try:
        nombre = input("Ingrese el nombre del país a actualizar: ")
        validar_pais_existente(nombre, paises)
        for pais in paises:
            if pais["Nombre"].lower() == nombre.lower():
                poblacion = input("Nueva población: ")
                if not validacion_numero(poblacion):
                    return
                poblacion = int(poblacion)
                validacion_numerica(
                    poblacion,
                    "La población"
                )
                superficie = input("Nueva superficie: ")
                if not validacion_float(superficie):
                    return
                superficie = float(superficie)
                validacion_numerica(
                    superficie,
                    "La superficie"
                )
                pais["Poblacion"] = poblacion
                pais["Superficie"] = superficie
                guardar_paises(paises)
                print("Datos actualizados correctamente")
                return
    except ValueError as error:
        print(error)
def leer_paises():
    paises = []
    with open(Archivo_CSV, "r", encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            paises.append(fila)
    return paises
def guardar_paises(paises):
    with open(Archivo_CSV, "w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(
            archivo,
            fieldnames=Campos
        )
        writer.writeheader()
        for pais in paises:
            writer.writerow(pais)

def buscar_pais(paises):
    try:
        nombre = input("Ingrese el nombre del país a buscar: ")
        validacion_nombre(nombre, Campos[0])
        encontrados = validar_pais_existente(nombre, paises)
        for pais in encontrados:
            print(f"Nombre: {pais['Nombre']}")
            print(f"Población: {pais['Poblacion']}")
            print(f"Superficie: {pais['Superficie']}")
            print(f"Continente: {pais['Continente']}")
            print("-" * 30)
    except ValueError as error:
        print(error)
def filtrar_paises(paises):
    print("----Filtrar Paises----")
    print("1. Por continente")
    print("2. Por población")
    print("3. Por superficie")
    opcion = input("Seleccione una opción: ")
    match opcion:
        case "1":
            continente = input("Ingrese el continente: ")
            encontrado = False
            for pais in paises:
                if pais["Continente"].lower() == continente.lower():
                    print(pais)
                    encontrado = True
            if not encontrado:
                print("No se encontraron países en ese continente.")
        case "2":
            minimo = input("Población mínima: ")
            if not validacion_numero(minimo):
                return
            maximo = input("Población máxima: ")
            if not validacion_numero(maximo):
                return
            minimo = int(minimo)
            maximo = int(maximo)
            validacion_rango(minimo, maximo)
            encontrado = False
            for pais in paises:
                poblacion = int(pais["Poblacion"])
                if minimo <= poblacion <= maximo:
                    print(pais)
                    encontrado = True
            if not encontrado:
                print("No se encontraron países en ese rango de población.")
        case "3":
            minimo = input("Superficie mínima: ")
            if not validacion_float(minimo):
                return
            maximo = input("Superficie máxima: ")
            if not validacion_float(maximo):
                return
            minimo = float(minimo)
            maximo = float(maximo)
            validacion_rango(minimo, maximo)
            encontrado = False
            for pais in paises:
                superficie = float(pais["Superficie"])
                if minimo <= superficie <= maximo:
                    print(pais)
                    encontrado = True
            if not encontrado:
                print("No se encontraron países en ese rango de superficie.")
        case _:
            print("Opción no válida.")
            
def obtener_nombre(pais):
    return pais["Nombre"].lower()

def obtener_poblacion(pais):
    return int(pais["Poblacion"])

def obtener_superficie(pais):
    return float(pais["Superficie"])

def ordenar_paises(paises):
    print("----Ordenar Países----")
    print("1. Nombre")
    print("2. Población")
    print("3. Superficie")
    opcion = input("Seleccione una opción: ")
    orden = input("Ascendente (A) o Descendente (D): ").upper()
    if orden == "D":
        reversa = True
    else:
        reversa = False
    match opcion:
        case "1":
            paises.sort(
                key=obtener_nombre,
                reverse=reversa
            )
        case "2":
            paises.sort(
                key=obtener_poblacion,
                reverse=reversa
            )
        case "3":
            paises.sort(
                key=obtener_superficie,
                reverse=reversa
            )
        case _:
            print("Opción no válida")
            return
    for pais in paises:
        print(f"Nombre: {pais['Nombre']}")
        print(f"Población: {pais['Poblacion']}")
        print(f"Superficie: {pais['Superficie']}")
        print(f"Continente: {pais['Continente']}")
        print("-" * 30)
def estadisticas(paises):
    if len(paises) == 0:
        print("No hay países cargados para calcular estadísticas.")
        return
    mayor_poblacion = max(paises, key=obtener_poblacion)
    menor_poblacion = min(paises, key=obtener_poblacion)
    suma_poblacion = 0
    suma_superficie = 0
    cantidad_continente = {}
    for pais in paises:
        suma_poblacion += int(pais["Poblacion"])
        suma_superficie += float(pais["Superficie"])
        continente = pais["Continente"]
        if continente in cantidad_continente:
            cantidad_continente[continente] += 1
        else:
            cantidad_continente[continente] = 1
        promedio_poblacion = suma_poblacion / len(paises)
        promedio_superficie = suma_superficie / len(paises)
        print("----Estadísticas----")
        print(f"País con mayor población: {mayor_poblacion['Nombre']} ({mayor_poblacion['Poblacion']})")
        print(f"País con menor población: {menor_poblacion['Nombre']} ({menor_poblacion['Poblacion']})")
        print(f"Promedio de población: {promedio_poblacion:.2f}")
        print(f"Promedio de superficie: {promedio_superficie:.2f}")
        print("Cantidad de países por continente:")
        for continente, cantidad in cantidad_continente.items():
            print(f"{continente}: {cantidad}")