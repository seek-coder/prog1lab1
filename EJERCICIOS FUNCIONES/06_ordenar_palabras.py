#Ejercicio 06: Crea una función que reciba una lista de palabras y devuelva una nueva lista con las palabras ordenadas alfabéticamente.
def ordenar_palabras(lista_palabras: list) -> list:
    if type(lista_palabras) is list:
        return sorted(lista_palabras) #sorted crea nueva lista; sort modifica in-place
    else:
        return "Datos Inválidos"

lista1 = ["X", "B", "E", "G", "C", "D", "Z", "Y", "A"]

print(ordenar_palabras(lista1))
print(ordenar_palabras("a"))