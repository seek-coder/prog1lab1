from data_stark import lista_personajes

quantity = len(lista_personajes)

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
    print(f"Lista de superhéroes agrupados por color de ojos:\n--------------------\nCon ojos azules: {superhero_per_eye_color['azul']}\nCon ojos marrones: {superhero_per_eye_color['marrón']}\nCon ojos rojos: {superhero_per_eye_color['rojo']}\nCon ojos amarillos: {superhero_per_eye_color['amarillo']}\nCon ojos plateados: {superhero_per_eye_color['plata']}\nCon ojos verdes: {superhero_per_eye_color['verde']}\nCon ojos azules: {superhero_per_eye_color['azul']}\nCon ojos avellana: {superhero_per_eye_color['avellana']}\nCon ojos amarillo sin iris: {superhero_per_eye_color['amarillo sin iris']}\n")

get_count_of_every_eye_color()