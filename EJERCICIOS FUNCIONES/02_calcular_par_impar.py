#Ejercicio 02: Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
def calcular_par_impar(num: float) -> float:
    if type(num) in (int, float):
        if num % 2 == 0:
            return f"El numero {num} es par"
        else:
            return f"El numero {num} es impar"
    else:
        return "Dato inválido"
print(calcular_par_impar(1))
print(calcular_par_impar(2))
print(calcular_par_impar(""))
