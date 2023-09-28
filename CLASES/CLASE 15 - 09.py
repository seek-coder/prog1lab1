# desarrollar una función que se llame calcular_IVA que reciba un monto y retorne 21% de ese valor. Llamar a la función para testearlo.

# def calcular_IVA(monto: float) -> float:
#     # return monto * 21/ 100 # si poner algo o no ponerlo tiene el mismo efecto, NO SE PONE!
#     # no agregar cosas cuando no sean necesarias
#     return monto * 0.21

# print(calcular_IVA(123.4))

# def calcular_IVA(monto: float) -> float:
#     try:
#         impuesto = monto * 0.21
#     except:
#         impuesto = None
#     return impuesto

# print(calcular_IVA("asd"))

# def calcular_IVA(monto: float, iva: float = 21) -> float:
#     try:
#         impuesto = monto * iva / 100
#     except:
#         impuesto = None
#     return impuesto

# print(calcular_IVA(200, 10.5))
# ---------------------------- #
# desarrollar una función que se llame calcular_superficie_circulo

# def calcular_superficie_circulo(radio:float, π:float = 3.14) -> float:
#     try:
#         superficie = π * radio**2
#     except:
#         superficie = None
#     return superficie
# print(calcular_superficie_circulo(200))

# def calcular_superficie_circulo(radio:float) -> float:
#     from math import pi
#     try:
#         superficie = math.pi * radio**2
#     except:
#         superficie = None
#     return superficie
# print(calcular_superficie_circulo(200))

# def calcular_superficie_rectangulo(base: float, altura: float) -> float:
#     try:
#         superficie = float(base * altura)
#     except:
#         superficie = None
#     return superficie

# print(calcular_superficie_rectangulo(5, 2))

def calcular_superficie_triangulo(base: float, altura: float) -> float:
    try:
        superficie = float(base * altura / 2)
    except:
        superficie = None
    return superficie

print(calcular_superficie_triangulo(5, 2))
