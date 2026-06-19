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
        case "3":
            paises = leer_paises()
            buscar_pais(paises)
        case "4":
            paises = leer_paises()
            filtrar_paises(paises)
        case "5":
            paises = leer_paises()
            ordenar_paises(paises)
        case "6":
            paises = leer_paises()
            estadisticas(paises)
        case "7":
            print("Saliendo del programa HASTA PRONTO!")
            break
        case _:
            print("Opcion no valida, por favor ingrese un numero del menu")