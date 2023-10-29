# con return

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

def get_higher_superhero() -> tuple:
    higher_name = ""
    higher_num = None

    for superhero in range(quantity):
        height_float = float(lista_personajes[superhero]["altura"])

        if higher_num == None or height_float > higher_num:
            higher_name = lista_personajes[superhero]["nombre"]
            higher_num = height_float
    return (higher_name, higher_num)

def get_lower_superhero() -> tuple:
    lower_name = ""
    lower_num = None

    for superhero in range(quantity):
        height_float = float(lista_personajes[superhero]["altura"])

        if lower_num == None or height_float < lower_num:
            lower_name = lista_personajes[superhero]["nombre"]
            lower_num = height_float
    return (lower_name, lower_num)

def get_superhero_average_height() -> float:
    height_sum = 0
    for superhero in range(quantity):
        height_float = float(lista_personajes[superhero]["altura"])
        height_sum += height_float

    if quantity > 0:
        average_height = height_sum / quantity
    return average_height

def get_heavier_superhero() -> tuple:
    heavier_name = ""
    heavier_num = None

    for superhero in range(quantity):
        weight_float = float(lista_personajes[superhero]["peso"])

        if heavier_num == None or weight_float > heavier_num:
            heavier_name = lista_personajes[superhero]["nombre"]
            heavier_num = weight_float
    return (heavier_name, heavier_num)

def get_lighter_superhero() -> tuple:
    lighter_name = ""
    lighter_num = None

    for superhero in range(quantity):
        weight_float = float(lista_personajes[superhero]["peso"])
        if lighter_num == None or weight_float < lighter_num:
            lighter_name = lista_personajes[superhero]["nombre"]
            lighter_num = weight_float
    return (lighter_name, lighter_num)

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

def get_higher_of_m() -> tuple:
    higher_of_m_name = ""
    higher_of_m_height = None

    for superhero in range(quantity):
        if lista_personajes[superhero]["genero"].lower() == "m":
            height_float = float(lista_personajes[superhero]["altura"])

            if higher_of_m_height == None or height_float > higher_of_m_height:
                higher_of_m_name = lista_personajes[superhero]["nombre"]
                higher_of_m_height = height_float
    return (higher_of_m_name, higher_of_m_height)

def get_higher_of_f() -> tuple:
    higher_of_f_name = ""
    higher_of_f_height = None

    
    for superhero in range(quantity):
        if lista_personajes[superhero]["genero"].lower() == "f":
            height_float = float(lista_personajes[superhero]["altura"])

            if higher_of_f_height == None or height_float > higher_of_f_height:
                higher_of_f_name = lista_personajes[superhero]["nombre"]
                higher_of_f_height = height_float
    return (higher_of_f_name, higher_of_f_height)

def get_lower_of_m() -> tuple:
    lower_of_m_name = ""
    lower_of_m_height = None

    for superhero in range(quantity):
        if lista_personajes[superhero]["genero"].lower() == "m":
            height_float = float(lista_personajes[superhero]["altura"])

            if lower_of_m_height == None or height_float < lower_of_m_height:
                lower_of_m_name = lista_personajes[superhero]["nombre"]
                lower_of_m_height = height_float
    return (lower_of_m_name, lower_of_m_height)

def get_lower_of_f() -> tuple:
    lower_of_f_name = ""
    lower_of_f_height = None

    for superhero in range(quantity):
        if lista_personajes[superhero]["genero"].lower() == "f":
            height_float = float(lista_personajes[superhero]["altura"])

            if lower_of_f_height == None or height_float < lower_of_f_height:
                lower_of_f_name = lista_personajes[superhero]["nombre"]
                lower_of_f_height = height_float
    return (lower_of_f_name, lower_of_f_height)

def get_height_average_of_m() -> float:
    height_of_m_sum = 0
    m_count = 0
    for superhero in range(quantity):
        if lista_personajes[superhero]["genero"].lower() == "m":
            m_count += 1
            height_of_m_sum += float(lista_personajes[superhero]["altura"])
    if m_count > 0:
        average_of_m = height_of_m_sum / m_count
    return average_of_m

def get_height_average_of_f() -> float:
    height_of_f_sum = 0
    f_count = 0
    for superhero in range(quantity):
        if lista_personajes[superhero]["genero"].lower() == "f":
            f_count += 1
            height_of_f_sum += float(lista_personajes[superhero]["altura"])
    if f_count > 0:
        average_of_f = height_of_f_sum / f_count
    return average_of_f

def get_count_of_every_eye_color() -> list:
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

    return superhero_per_eye_color

def get_count_of_every_hair_color() -> list:
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

    return superhero_per_hair_color

def get_count_of_every_IQ() -> list:
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
    
    return superhero_per_IQ

info_menu = f"¿Qué dato necesitás saber de todos los superhéroes?:\n# ---------------------------------------------------- #\n\n1. nombre\n2. nombre y altura\n3. mas alto\n4. mas bajo\n5. promedio de altura\n6. mas pesado\n7. mas liviano\n8. nombres masculinos\n9. nombres femeninos\n10. masculino mas alto\n11. femenina mas alta\n12. masculino mas bajo\n13. femenina mas baja\n14. promedio de altura de masculinos\n15. promedio de altura de femeninos\n16. lista de color de ojos\n17. lista de color de pelo\n18. lista por inteligencia\n\n0. salir\ncls. limpiar consola\n\n# ---------------------------------------------------- #\n"

menu = input(info_menu)
while menu:
    match(menu.lower()):
        case "1" | "nombre":
            get_superhero_name()
        case "2" | "nombre y altura":
            get_superhero_name_plus_height()
        case "3" | "mas alto":
            print(get_higher_superhero())
        case "4" | "mas bajo":
            print(get_lower_superhero())
        case "5" | "promedio de altura":
            print(f"{get_superhero_average_height():.5}CM")
        case "6" | "mas pesado":
            print(get_heavier_superhero())
        case "7" | "mas liviano":
            print(get_lighter_superhero())
        case "8" | "nombres masculinos":
            get_name_of_m()
        case "9" | "nombres femeninos":
            get_name_of_f()
        case "10" | "masculino mas alto":
            print(get_higher_of_m())
        case "11" | "femenina mas alta":
            print(get_higher_of_f())
        case "12" | "masculino mas bajo":
            print(get_lower_of_m())
        case "13" | "femenina mas baja":
            print(get_lower_of_f())
        case "14" | "promedio de altura de masculinos":
            print(f"{get_height_average_of_m():.5}CM")
        case "15" | "promedio de altura de femeninos":
            print(f"{get_height_average_of_f():.5}CM")
        case "16" | "lista por color de ojos":
            eye_colors = get_count_of_every_eye_color()
            print(f"Colores de ojos:\n\n"
                f"Azul: {eye_colors['azul']}\n"
                f"Marrón: {eye_colors['marrón']}\n"
                f"Rojo: {eye_colors['rojo']}\n"
                f"Amarillo: {eye_colors['amarillo']}\n"
                f"Plateado: {eye_colors['plata']}\n"
                f"Verde: {eye_colors['verde']}\n"
                f"Avellanda: {eye_colors['avellana']}\n"
                f"Amarillo sin iris: {eye_colors['amarillo sin iris']}\n")
        case "17" | "lista por color de pelo":
            hair_colors = get_count_of_every_hair_color()
            print(f"Colores de pelo:\n\n"
                f"Negro: {hair_colors['negro']}\n"
                f"Marrón: {hair_colors['marrón']}\n"
                f"Castaño: {hair_colors['castaño']}\n"
                f"Rojo con naranja: {hair_colors['rojo con naranja']}\n"
                f"Amarillo: {hair_colors['amarillo']}\n"
                f"Sin pelo: {hair_colors['sin pelo']}\n"
                f"Rubio: {hair_colors['rubio']}\n"
                f"Verde: {hair_colors['verde']}\n"
                f"Rojo: {hair_colors['rojo']}\n"
                f"Blanco: {hair_colors['blanco']}\n"
                f"Marrón con blanco: {hair_colors['marrón con blanco']}\n"
                f"Datos insuficientes: {hair_colors['SIN DATOS']}\n")
        case "18" | "lista por inteligencia":
            iq = get_count_of_every_IQ()
            print(f"Inteligencia:\n\n"
                f"Promedio: {iq['promedio']}\n"
                f"Buena: {iq['bueno']}\n"
                f"Alta: {iq['alto']}\n"
                f"Datos insuficientes: {iq['SIN DATOS']}\n")

        case "cls" | "limpiar":
            system("cls")
        case "0" | "salir":
            system("cls")
            break
        case _:
            print("\nOPCIÓN INVÁLIDA.\nEscriba el número o el nombre de la opción. Intentá nuevamente.\n")
            menu = input(info_menu)
            continue

    back = input("¿Volver a las opciones? s/n\n")
    if back.lower() == "s":
            menu = input(info_menu)
    else:
            system("cls")
            break