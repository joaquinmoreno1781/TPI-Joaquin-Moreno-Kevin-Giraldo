from funciones import *
crear_csv()
while True:
    menu()
    opcion = input("Ingrese un numero del menu: ")
    match opcion:
        case "1":
            agregar_pais(Campos)
        case "2":
            paises = leer_paises()
            actualizar_datos(paises)
