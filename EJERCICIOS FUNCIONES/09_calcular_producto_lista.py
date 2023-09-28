#Ejercicio 09: Escribe una función que tome una lista de números y calcule el producto de todos los elementos.
def calcular_producto_lista(lista_numeros: list) -> float:
    if type(lista_numeros) is list:
        producto_total = 1
        for i in range(len(lista_numeros)):
            producto_total *= lista_numeros[i]
        return producto_total
    else:
        return "Datos inválidos"

lista_numeros_test = [5, 2, 4, 1, -1, -1, 2]
print(calcular_producto_lista(lista_numeros_test))
