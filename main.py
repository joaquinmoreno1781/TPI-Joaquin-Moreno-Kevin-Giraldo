from funciones import *
while True:
    menu()
    opcion = input("Ingrese un numero del menu: ")
    match opcion:
        case "1":
            agregar_pais(Campos)
