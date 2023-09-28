#Ejercicio 03: Diseña una función que tome una lista de números y devuelva la suma de todos los elementos.
def calcular_suma_lista(lista: list) -> float:
    if type(lista) is list:
        suma_total = 0
        cantidad = len(lista)
        for i in range(cantidad):
            suma_total += lista[i]
        return suma_total
    else:
        return "Dato inválido"

print(calcular_suma_lista([1, 2, 3]))
print(calcular_suma_lista([100, 0 , 200]))
print(calcular_suma_lista([10.5, 0.2 , 20.5]))
print(calcular_suma_lista(""))