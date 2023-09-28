import os

seguir = True
flag = True


while seguir:
    print("*** menu de opciones ***")
    print("-----")
    print("1- saludar")
    print("2- brindar")
    print("3- despedir")
    print("4- salir")
    opcion = input("Ingrese opcion: ")

    match opcion:
        case "1":
            print("Hola")
        case "2":
            print("Chin chin")
        case "3":
            print("Chau. Hasta la proxima")
        case "4":
            confirma = input("Confirma salida? :")
            seguir = False if confirma == "s" else True #operador ternario. Se puede usar en f-strings (ver CLASE 11-09b)

    if flag:
        os.system("pause")

    # os.system("cls") # para limpiar consola
    # os.system("pause") # para pausar un toque la consola
        


