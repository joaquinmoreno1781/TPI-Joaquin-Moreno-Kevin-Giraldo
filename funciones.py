def validacion_nombre(nombre):
    if nombre.strip() == "":
        raise ValueError("El nombre no puede estar vacio")
def validacion_poblacion(poblacion):
    if poblacion < 0:
        raise ValueError("La poblacion debe ser mayor a 0")
def valiadacion_superficie(superficie):
    if superficie < 0:
        raise ValueError("La superficie debe ser mayor a 0")
def validacion_continente(continente):
    if continente.strip() == "":
        raise ValueError("El continente no puede estar vacio")
def validacion_rango_poblacion(poblacion, minimo, maximo):
    if poblacion < minimo or poblacion > maximo:
        raise ValueError(f"La poblacion debe estar entre {minimo} y {maximo}")
def validacion_rango_superficie(superficie, minimo, maximo):
    if superficie < minimo or superficie > maximo:
        raise ValueError(f"La superficie debe estar entre {minimo} y {maximo}")
def menu():
        print("Bienvenido al menú principal")
        print("1. Agregar país")
        print("2. Buscar país")
        print("3. Salir")