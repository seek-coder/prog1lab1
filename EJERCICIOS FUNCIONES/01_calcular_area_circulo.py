#Ejercicio 01: Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
def calcular_area_circulo(radio: float) -> float:
    if type(radio) in (int, float):
        from math import pi
        area = pi * radio**2
        return area
    else:
        return "Dato inválido"
print(calcular_area_circulo(10))
print(calcular_area_circulo(""))

