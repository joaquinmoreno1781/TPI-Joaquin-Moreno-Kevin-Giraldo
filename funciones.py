import csv
# Nombre del archivo CSV donde se almacenan los datos
Archivo_CSV = "Paises.csv"
# Encabezados del archivo CSV
Campos = ["Nombre","Poblacion","Superficie","Continente"]
# Verifica si un país ya existe en el archivo
def pais_existe(nombre):
    paises = leer_paises()
    for pais in paises:
        if pais["Nombre"].lower() == nombre.lower():
            return True
    return False
# Valida que el dato ingresado sea numérico entero
def validacion_numero(numero):
    if not numero.isdigit():
        print("Error.Solo numeros")
        return False
    return True
# Muestra los datos de un país con formato
def mostrar_pais(pais):
    print("-" * 40)
    print(f"Nombre      : {pais['Nombre']}")
    print(f"Población   : {pais['Poblacion']} hab.")
    print(f"Superficie  : {pais['Superficie']} km²")
    print(f"Continente  : {pais['Continente']}")
    print("-" * 40)
# Valida que el nombre del país solo contenga letras y espacios
def validacion_nombre_pais(texto):
    texto = texto.strip()
    if texto == "":
        print("Error. No puede estar vacío")
        return False
    for caracter in texto:
        if not (caracter.isalpha() or caracter == " "):
            print("Error. Solo se permiten letras y espacios")
            return False
    return True
# Valida que el dato ingresado pueda convertirse a número decimal
def validacion_float(numero):
    try:
        numero_corregido = numero.replace(",", ".")
        float(numero_corregido)
        return True
    except ValueError:
        print("Error. Debe ser un numero valido")
        return False
# Verifica que el nombre ingresado no esté vacío
def validacion_nombre(nombre, campos):
    if nombre.strip() == "":
        raise ValueError(f"{campos} no puede estar vacío")
# Verifica que un valor numérico sea mayor a cero
def validacion_numerica(valor, campo):
    if valor <= 0:
        raise ValueError(f"{campo} debe ser mayor a 0")
# Valida que el valor mínimo no sea mayor que el máximo
def validacion_rango(minimo, maximo):
    if minimo > maximo:
        raise ValueError("El mínimo no puede ser mayor al máximo")
# Busca un país dentro de la lista de países cargados
def validar_pais_existente(nombre, paises):
    encontrados = []
    for pais in paises:
        if nombre.lower() in pais["Nombre"].lower():
            encontrados.append(pais)
    if len(encontrados) == 0:
        raise ValueError("El país no existe")
    return encontrados
# Muestra el menú principal del programa
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
# Crea el archivo CSV si no existe
def crear_csv():
    if not os.path.exists(Archivo_CSV):
        with open(Archivo_CSV, "w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow(Campos)
# Permite agregar un nuevo país al archivo
def agregar_pais(campos):
    try:
        nombre = input("Nombre del pais: ").strip().title()
        validacion_nombre(nombre, campos[0])
        if not validacion_nombre_pais(nombre):
            return
        if pais_existe(nombre):
            print("Error. El país ya existe")
            return
        poblacion = input("Poblacion: ")
        if not validacion_numero(poblacion):
            return
        poblacion = int(poblacion)
        validacion_numerica(poblacion, campos[1])
        superficie = input("Superficie:")
        if not validacion_float(superficie):
            return
        superficie = float(superficie)
        validacion_numerica(superficie, campos[2])
        print("\nSeleccione un continente:")
        print("1. America")
        print("2. Europa")
        print("3. Asia")
        print("4. Africa")
        print("5. Oceania")
        print("6. Antartida")
        opcion_continente = input("Ingrese una opcion: ")
        match opcion_continente:
            case "1":
                continente = "America"
            case "2":
                continente = "Europa"
            case "3":
                continente = "Asia"
            case "4":
                continente = "Africa"
            case "5":
                continente = "Oceania"
            case "6":
                continente = "Antartida"
            case _:
                print("Error. Opcion invalida")
                return
        with open(Archivo_CSV, "a", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            writer.writerow([nombre, poblacion, superficie, continente])
        print("País agregado correctamente")
    except ValueError as error:
        print(error)
# Actualiza la población y superficie de un país existente
def actualizar_datos(paises):
    try:
        nombre = input("Ingrese el nombre del país a actualizar: ").strip()
        encontrados = validar_pais_existente(nombre, paises)
        for pais in encontrados:
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
            superficie_float = float((superficie).replace(",", "."))
            validacion_numerica(
                superficie_float,
                "La superficie"
            )
            pais["Poblacion"] = poblacion
            pais["Superficie"] = str(superficie_float)
        guardar_paises(paises)
        print("Datos actualizados correctamente")
    except ValueError as error:
        print(error)
# Lee todos los países almacenados en el CSV
def leer_paises():
    paises = []
    with open(Archivo_CSV, "r", encoding="utf-8") as archivo:
        reader = csv.DictReader(archivo)
        for fila in reader:
            paises.append(fila)
    return paises
# Guarda la lista de países en el archivo CSV
def guardar_paises(paises):
    with open(Archivo_CSV, "w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(
            archivo,
            fieldnames=Campos
        )
        writer.writeheader()
        for pais in paises:
            writer.writerow(pais)
# Busca uno o más países por nombre
def buscar_pais(paises):
    try:
        nombre = input("Ingrese el nombre del país a buscar: ").strip().capitalize()
        validacion_nombre(nombre, Campos[0])
        encontrados = validar_pais_existente(nombre, paises)
        for pais in encontrados:
            print(f"Nombre: {pais['Nombre']}")
            print(f"Población: {pais['Poblacion']}")
            print(f"Superficie: {pais['Superficie']} km²")
            print(f"Continente: {pais['Continente']}")
            print("-" * 30)
    except ValueError as error:
        print(error)
# Filtra países por continente, población o superficie
def filtrar_paises(paises):
    print("----Filtrar Paises----")
    print("1. Por continente")
    print("2. Por población")
    print("3. Por superficie")
    opcion = input("Seleccione una opción: ")
    match opcion:
        case "1":
            print("\nSeleccione un continente:")
            print("1. America")
            print("2. Europa")
            print("3. Asia")
            print("4. Africa")
            print("5. Oceania")
            print("6. Antartida")
            opcion_continente = input("Ingrese una opcion: ")
            match opcion_continente:
                case "1":
                    continente = "America"
                case "2":
                    continente = "Europa"
                case "3":
                    continente = "Asia"
                case "4":
                    continente = "Africa"
                case "5":
                    continente = "Oceania"
                case "6":
                    continente = "Antartida"
                case _:
                    print("Error. Opcion invalida")
                    return
            encontrado = False
            for pais in paises:
                if pais["Continente"].lower() == continente.lower():
                    mostrar_pais(pais)
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
            try:
                validacion_rango(minimo, maximo)
            except ValueError as error:
                print(error)
                return
            encontrado = False
            for pais in paises:
                poblacion = int(pais["Poblacion"])
                if minimo <= poblacion <= maximo:
                    mostrar_pais(pais)
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
            try:
                validacion_rango(minimo, maximo)
            except ValueError as error:
                print(error)
                return
            encontrado = False
            for pais in paises:
                superficie = float(pais["Superficie"])
                if minimo <= superficie <= maximo:
                    mostrar_pais(pais)
                    encontrado = True
            if not encontrado:
                print("No se encontraron países en ese rango de superficie.")
        case _:
            print("Opción no válida.")
# Obtiene el nombre del país para ordenar alfabéticamente                        
def obtener_nombre(pais):
    return pais["Nombre"].lower()
# Obtiene la población del país para ordenar
def obtener_poblacion(pais):
    return int(pais["Poblacion"])
# Obtiene la superficie del país para ordenar
def obtener_superficie(pais):
    return float(pais["Superficie"])
# Ordena los países según el criterio elegido por el usuario
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
        print(f"Superficie: {pais['Superficie']} km²")
        print(f"Continente: {pais['Continente']}")
        print("-" * 30)
# Calcula y muestra estadísticas generales de los países
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
    print(f"Promedio de superficie: {promedio_superficie:.2f} km²")
    print("Cantidad de países por continente:")
    for continente, cantidad in cantidad_continente.items():
        print(f"{continente}: {cantidad}")