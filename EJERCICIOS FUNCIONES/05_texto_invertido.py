#Ejercicio 05: Escribe una función que tome una cadena como entrada y devuelva la cadena invertida.
def texto_invertido(string: str) -> str:
    if type(string) is str:
        return string[::-1]
    else:
        return "Datos inválidos"

print(texto_invertido("Hola"))
print(texto_invertido("Hola cómo estás?"))
print(texto_invertido("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"))
print(texto_invertido(5))