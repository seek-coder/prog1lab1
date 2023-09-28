#Ejercicio 07: Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.
def calcular_potencia_numero(base: float, exponente: float) -> float:
    if all(type(x) in (int, float) for x in (base, exponente)):
        return base ** exponente
    else:
        return "Datos inválidos"

print(calcular_potencia_numero(2,2))
print(calcular_potencia_numero(1,5))
print(calcular_potencia_numero(4,7))
print(calcular_potencia_numero("a","a"))