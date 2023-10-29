# con print

from data_stark import lista_personajes
from os import system
# ---------------------------------------- #
#                desafío 0                 #
# ---------------------------------------- #

quantity = len(lista_personajes)

def get_superhero_name() -> str:
    for superhero in range(quantity):
        print(f"Nombre del superhéroe N°{superhero}: {lista_personajes[superhero]['nombre']}")

def get_superhero_name_plus_height() -> str:
    for superhero in range(quantity):
        print(f"Nombre del superhéroe N°{superhero}: {lista_personajes[superhero]['nombre']}, {lista_personajes[superhero]['altura']:.6}")

def get_higher_superhero() -> str:
    higher_name = ""
    higher_num = None

    for superhero in range(quantity):
        height_float = float(lista_personajes[superhero]["altura"])

        if higher_num == None or height_float > higher_num:
            higher_name = lista_personajes[superhero]["nombre"]
            higher_num = height_float
    print(f"El superhéroe más alto es {higher_name} de {higher_num:.6}CM")

def get_lower_superhero() -> str:
    lower_name = ""
    lower_num = None

    for superhero in range(quantity):
        height_float = float(lista_personajes[superhero]["altura"])

        if lower_num == None or height_float < lower_num:
            lower_name = lista_personajes[superhero]["nombre"]
            lower_num = height_float
    print(f"El superhéroe más bajo es {lower_name} de {lower_num:.6}CM")

def get_superhero_average_height() -> str:
    height_sum = 0
    for superhero in range(quantity):
        height_float = float(lista_personajes[superhero]["altura"])
        height_sum += height_float

    if quantity > 0:
        average_height = height_sum / quantity
    print(f"El promedio de altura de los superheróes es: {average_height:.6}CM")

def get_heavier_superhero() -> str:
    heavier_name = ""
    heavier_num = None

    for superhero in range(quantity):
        weight_float = float(lista_personajes[superhero]["peso"])

        if heavier_num == None or weight_float > heavier_num:
            heavier_name = lista_personajes[superhero]["nombre"]
            heavier_num = weight_float
    print(f"El superéheroe más pesado es {heavier_name} de {heavier_num:.6}KG")

def get_lighter_superhero() -> str:
    lighter_name = ""
    lighter_num = None

    for superhero in range(quantity):
        weight_float = float(lista_personajes[superhero]["peso"])
        if lighter_num == None or weight_float < lighter_num:
            lighter_name = lista_personajes[superhero]["nombre"]
            lighter_num = weight_float
    print(f"El superéheroe más liviano es {lighter_name} de {lighter_num:.6}KG")

# ---------------------------------------- #
#                desafío 1                 #
# ---------------------------------------- #

def get_name_of_m() -> str:
    for superhero in range(quantity):
        if lista_personajes[superhero]["genero"].lower() == "m":
            print(f"Nombre del superhéroe masculino: {lista_personajes[superhero]['nombre']}")

def get_name_of_f() -> str:
    for superhero in range(quantity):
        if lista_personajes[superhero]["genero"].lower() == "f":
            print(f"Nombre del superhéroe femenino: {lista_personajes[superhero]['nombre']}")

def get_higher_of_m() -> str:
    higher_of_m_name = ""
    higher_of_m_height = None

    for superhero in range(quantity):
        if lista_personajes[superhero]["genero"].lower() == "m":
            height_float = float(lista_personajes[superhero]["altura"])

            if higher_of_m_height == None or height_float > higher_of_m_height:
                higher_of_m_name = lista_personajes[superhero]["nombre"]
                higher_of_m_height = height_float
    print(f"El superhéroe masculino más alto es: {higher_of_m_name}")

def get_higher_of_f() -> str:
    higher_of_f_name = ""
    higher_of_f_height = None

    
    for superhero in range(quantity):
        if lista_personajes[superhero]["genero"].lower() == "f":
            height_float = float(lista_personajes[superhero]["altura"])

            if higher_of_f_height == None or height_float > higher_of_f_height:
                higher_of_f_name = lista_personajes[superhero]["nombre"]
                higher_of_f_height = height_float
    print(f"El superhéroe femenino más alto es: {higher_of_f_name}")

def get_lower_of_m() -> str:
    lower_of_m_name = ""
    lower_of_m_height = None

    for superhero in range(quantity):
        if lista_personajes[superhero]["genero"].lower() == "m":
            height_float = float(lista_personajes[superhero]["altura"])

            if lower_of_m_height == None or height_float < lower_of_m_height:
                lower_of_m_name = lista_personajes[superhero]["nombre"]
                lower_of_m_height = height_float
    print(f"El superhéroe masculino más bajo es: {lower_of_m_name}")

def get_lower_of_f() -> str:
    lower_of_f_name = ""
    lower_of_f_height = None

    for superhero in range(quantity):
        if lista_personajes[superhero]["genero"].lower() == "f":
            height_float = float(lista_personajes[superhero]["altura"])

            if lower_of_f_height == None or height_float < lower_of_f_height:
                lower_of_f_name = lista_personajes[superhero]["nombre"]
                lower_of_f_height = height_float
    print(f"El superhéroe femenino más bajo es: {lower_of_f_name}")

def get_height_average_of_m() -> str:
    height_of_m_sum = 0
    m_count = 0
    for superhero in range(quantity):
        if lista_personajes[superhero]["genero"].lower() == "m":
            m_count += 1
            height_of_m_sum += float(lista_personajes[superhero]["altura"])
    if m_count > 0:
        average_of_m = height_of_m_sum / m_count
    print(f"El promedio de altura de los superhéroes masculinos es de {average_of_m:.5}CM")

def get_height_average_of_f() -> str:
    height_of_f_sum = 0
    f_count = 0
    for superhero in range(quantity):
        if lista_personajes[superhero]["genero"].lower() == "f":
            f_count += 1
            height_of_f_sum += float(lista_personajes[superhero]["altura"])
    if f_count > 0:
        average_of_f = height_of_f_sum / f_count
    print(f"El promedio de altura de los superhéroes femeninos es de {average_of_f:.5}CM")

def get_count_of_every_eye_color() -> str:
    blue_count = 0
    brown_count = 0
    red_count = 0
    yellow_count = 0
    silver_count = 0
    green_count = 0
    hazel_count = 0
    yellow_without_irises_count = 0

    superhero_per_eye_color = {
        "azul":  [],
        "marrón": [],
        "rojo": [],
        "amarillo": [],
        "plata": [],
        "verde": [],
        "avellana": [],
        "amarillo sin iris": []
    }

    for superhero in range(quantity):
        match(lista_personajes[superhero]["color_ojos"].lower()):
            case "blue":
                blue_count += 1
                superhero_per_eye_color["azul"].append(lista_personajes[superhero]["nombre"])
            case "brown":
                brown_count += 1
                superhero_per_eye_color["marrón"].append(lista_personajes[superhero]["nombre"])
            case "red":
                red_count += 1
                superhero_per_eye_color["rojo"].append(lista_personajes[superhero]["nombre"])
            case "yellow":
                yellow_count += 1
                superhero_per_eye_color["amarillo"].append(lista_personajes[superhero]["nombre"])
            case "silver":
                silver_count += 1
                superhero_per_eye_color["plata"].append(lista_personajes[superhero]["nombre"])
            case "green":
                green_count += 1
                superhero_per_eye_color["verde"].append(lista_personajes[superhero]["nombre"])
            case "hazel":
                hazel_count += 1
                superhero_per_eye_color["avellana"].append(lista_personajes[superhero]["nombre"])
            case "yellow (without irises)":
                yellow_without_irises_count += 1
                superhero_per_eye_color["amarillo sin iris"].append(lista_personajes[superhero]["nombre"])

    info = f"Lista de superhéroes agrupados por color de ojos y cantidad:\n--------------------\nCon ojos azules: {superhero_per_eye_color['azul']}, {blue_count}\nCon ojos marrones: {superhero_per_eye_color['marrón']}, {brown_count}\nCon ojos rojos: {superhero_per_eye_color['rojo']}, {red_count}\nCon ojos amarillos: {superhero_per_eye_color['amarillo']}, {yellow_count}\nCon ojos plateados: {superhero_per_eye_color['plata']}, {silver_count}\nCon ojos verdes: {superhero_per_eye_color['verde']}, {green_count}\nCon ojos azules: {superhero_per_eye_color['azul']}, {blue_count}\nCon ojos avellana: {superhero_per_eye_color['avellana']}, {hazel_count}\nCon ojos amarillo sin iris: {superhero_per_eye_color['amarillo sin iris']}. {yellow_without_irises_count}\n"

    print(info)

def get_count_of_every_hair_color() -> str:
    black_count = 0
    brown_count = 0
    auburn_count = 0
    red_orange_count = 0
    yellow_count = 0
    no_hair_count = 0
    blond_count = 0
    green_count = 0
    red_count = 0
    brown_white_count = 0
    white_count = 0

    empty_count = 0

    superhero_per_hair_color = {
        "negro":  [],
        "marrón": [],
        "castaño": [],
        "rojo con naranja": [],
        "amarillo": [],
        "sin pelo": [],
        "rubio": [],
        "verde": [],
        "rojo": [],
        "blanco": [],
        "marrón con blanco": [],
        
        "SIN DATOS": []
    }

    for superhero in range(quantity):
        match(lista_personajes[superhero]["color_pelo"].lower()):
            case "black":
                black_count += 1
                superhero_per_hair_color["negro"].append(lista_personajes[superhero]["nombre"])
            case "brown":
                brown_count += 1
                superhero_per_hair_color["marrón"].append(lista_personajes[superhero]["nombre"])
            case "auburn":
                auburn_count += 1
                superhero_per_hair_color["castaño"].append(lista_personajes[superhero]["nombre"])
            case "red / orange":
                red_orange_count += 1
                superhero_per_hair_color["rojo con naranja"].append(lista_personajes[superhero]["nombre"])
            case "yellow":
                yellow_count += 1
                superhero_per_hair_color["amarillo"].append(lista_personajes[superhero]["nombre"])
            case "no hair":
                no_hair_count += 1
                superhero_per_hair_color["sin pelo"].append(lista_personajes[superhero]["nombre"])
            case "blond" | "blonde":
                blond_count += 1
                superhero_per_hair_color["rubio"].append(lista_personajes[superhero]["nombre"])
            case "green":
                green_count += 1
                superhero_per_hair_color["verde"].append(lista_personajes[superhero]["nombre"])
            case "red":
                red_count += 1
                superhero_per_hair_color["rojo"].append(lista_personajes[superhero]["nombre"])
            case "brown / white":
                brown_white_count += 1
                superhero_per_hair_color["marrón con blanco"].append(lista_personajes[superhero]["nombre"])
            case "white":
                white_count += 1
                superhero_per_hair_color["blanco"].append(lista_personajes[superhero]["nombre"])
            case _:
                empty_count += 1
                superhero_per_hair_color["SIN DATOS"].append(lista_personajes[superhero]["nombre"])

    info = f"Lista de superhéroes agrupados por color de pelo y cantidad:\n--------------------\nPelo negro:{superhero_per_hair_color['negro']}, {black_count}\nPelo marrón: {superhero_per_hair_color['marrón']}, {brown_count}\nPelo castaño: {superhero_per_hair_color['castaño']}, {auburn_count}\nPelo rojo con naranja: {superhero_per_hair_color['rojo con naranja']}, {red_orange_count}\nPelo amarillo: {superhero_per_hair_color['amarillo']}, {yellow_count}\nSin pelo: {superhero_per_hair_color['sin pelo']}, {no_hair_count}\nRubios/as: {superhero_per_hair_color['rubio']}, {blond_count}\nPelo verde: {superhero_per_hair_color['verde']}, {green_count}\nPelo rojo: {superhero_per_hair_color['rojo']}, {red_count}\nMarrón con blanco: {superhero_per_hair_color['marrón con blanco']}, {brown_white_count}\nPelo blanco: {superhero_per_hair_color['blanco']}, {white_count}\nSin datos suficientes: {superhero_per_hair_color['SIN DATOS']}, {empty_count}"

    print(info)

def get_count_of_every_IQ() -> str:
    average_count = 0
    good_count = 0
    high_count = 0

    empty_count = 0

    superhero_per_IQ = {
        "promedio" : [],
        "bueno" : [],
        "alto" : [],

        "SIN DATOS" : [],
    }

    for superhero in range(quantity):
        match(lista_personajes[superhero]["inteligencia"].lower()):
            case "average":
                average_count += 1
                superhero_per_IQ["promedio"].append(lista_personajes[superhero]["nombre"])
            case "good":
                good_count += 1
                superhero_per_IQ["bueno"].append(lista_personajes[superhero]["nombre"])
            case "high":
                high_count += 1
                superhero_per_IQ["alto"].append(lista_personajes[superhero]["nombre"])
            case _:
                empty_count += 1
                superhero_per_IQ["SIN DATOS"].append(lista_personajes[superhero]["nombre"])
    
    info = f"Lista de superhéroes agrupados por inteligencia:\n--------------------\nPromedio:{superhero_per_IQ['promedio']}, {average_count}\nBuena:{superhero_per_IQ['bueno']}, {good_count}\nAlta: {superhero_per_IQ['alto']}, {high_count}\nSIN DATOS: {superhero_per_IQ['SIN DATOS']}, {empty_count}"

    print(info)




info_menu = f"¿Qué dato necesitás saber de todos los superhéroes?:\n1. nombre\n2. nombre y altura\n3. mas alto\n4. mas bajo\n5. promedio de altura\n6. mas pesado\n7. mas liviano\n8. masculinos\n0. salir\n"

menu = input(info_menu)
while menu:
    match(menu.lower()):
        case "1" | "nombre":
            get_superhero_name()
        case "2" | "nombre y altura":
            get_superhero_name_plus_height()
        case "3" | "mas alto":
            get_higher_superhero()
        case "4" | "mas bajo":
            get_lower_superhero()
        case "5" | "promedio de altura":
            get_superhero_average_height()
        case "6" | "mas pesado":
            get_heavier_superhero()
        case "7" | "mas liviano":
            get_lighter_superhero()
        case "8" | "masculinos":
            get_name_of_m()
        case "9" | "femeninos":
            get_name_of_f()
        case "10" | "masculino mas alto":
            get_higher_of_m()
        case "11" | "femenina mas alta":
            get_higher_of_f()
        case "12" | "masculino mas bajo":
            get_lower_of_m()
        case "13" | "femenina mas baja":
            get_lower_of_f()
        case "14" | "promedio de altura de masculinos":
            get_height_average_of_m()
        case "15" | "promedio de altura de femeninos":
            get_height_average_of_f()
        case "16" | "lista por color de ojos":
            get_count_of_every_eye_color()
        case "17" | "lista por color de pelo":
            get_count_of_every_hair_color() 
        case "18" | "lista por inteligencia":
            get_count_of_every_IQ()

        case "cls" | "limpiar":
            system("cls")
        case "0" | "salir":
            system("cls")
            break
        case _:
            print("Opción inválida. Escriba el número o el nombre de la opción. Intentá nuevamente.\n")
            menu = input(info_menu)
            continue

    back = input("¿Volver a las opciones? s/n\n")
    if back.lower() == "s":
            menu = input(info_menu)
    else:
            system("cls")
            break

