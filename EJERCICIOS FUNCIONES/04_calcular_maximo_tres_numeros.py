#Ejercicio 04: Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
def calcular_maximo_tres_numeros(num1: float, num2: float, num3: float) -> float:
    if all(type(x) in (int, float) for x in (num1, num2, num3)): #"Si para todos los valores x en la tupla (num1, num2, num3), el tipo de x es un entero (int) o un número decimal (float), entonces..."
        if num1 > num2 and num1 > num3:
            num_max = num1
        elif num2 > num3:
            num_max = num2
        else:
            num_max = num3
        return num_max
    else:
        return "Datos inválidos"
    
print(calcular_maximo_tres_numeros(1,2,3))
print(calcular_maximo_tres_numeros(10,100,1000))
print(calcular_maximo_tres_numeros(100,10,1))
print(calcular_maximo_tres_numeros(-1,0,1))
print(calcular_maximo_tres_numeros("", "", ""))
        

