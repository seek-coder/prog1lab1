from data_stark import lista_personajes

quantity = len(lista_personajes)
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
print("-------------------------")
print("Nombre de cada superhéroe")
print("-------------------------")

for superhero in range(quantity):
    print(f"N°{superhero}: {lista_personajes[superhero]['nombre']}")

print("-------------------------")
print("Nombre de cada superhéroe, su altura")
print("-------------------------")

for superhero in range(quantity):
    # C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
    print(f"N°{superhero}: {lista_personajes[superhero]['nombre']}, {lista_personajes[superhero]['altura']:.6}")

# D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
# F.Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
# G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)

print("-------------------------")
higher_name = ""
higher_num = None

lower_name = ""
lower_num = None

heavier_name = ""
heavier_num = None

lighter_name = ""
lighter_num = None

height_acc = 0

for superhero in range(quantity):
    height_float = float(lista_personajes[superhero]["altura"])
    weight_float = float(lista_personajes[superhero]["peso"])
    height_acc += height_float

    if higher_num == None or height_float > higher_num:
        higher_name = lista_personajes[superhero]["nombre"]
        higher_num = height_float

    if lower_num == None or height_float < lower_num:
        lower_name = lista_personajes[superhero]["nombre"]
        lower_num = height_float

    if heavier_num == None or weight_float > heavier_num:
        heavier_name = lista_personajes[superhero]["nombre"]
        heavier_num = weight_float

    if lighter_num == None or weight_float < lighter_num:
        lighter_name = lista_personajes[superhero]["nombre"]
        lighter_num = weight_float

if quantity > 0:
    average_height = height_acc / quantity

print(f"El superhéroe más alto es {higher_name} de {higher_num:.6}CM")
print(f"El superhéroe más bajo es {lower_name} de {lower_num:.6}CM")
print(f"El promedio de altura de los superheróes es: {average_height:.6}CM")
print(f"El superéheroe más pesado es {heavier_name} de {heavier_num:.6}KG")
print(f"El superéheroe más liviano es {lighter_name} de {lighter_num:.6}KG")

