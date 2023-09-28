#Ejercicio 08: Define una función que reciba una lista de números y devuelva una nueva lista con solo los números pares.
def lista_solo_pares(lista_numeros: list) -> list:
    lista_pares = []

    if type(lista_numeros) is list:
        for i in range(len(lista_numeros)):
            if lista_numeros[i] % 2 == 0:
                lista_pares.append(lista_numeros[i])
        return lista_pares
    else:
        return "Datos inválidos"
    
lista_numeros = [0, 2, 3, 4, 5, 6]
print(lista_solo_pares(lista_numeros))
print(lista_solo_pares("a"))
print(lista_solo_pares("b"))

