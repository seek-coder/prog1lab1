#Ejercicio 10: Crea una función que determine si una cadena dada es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
def detectar_palindromo(string: str) -> bool:
    if type(string) is str:
        string_invertido = string[::-1]
        return string.lower() == string_invertido.lower()
    else:
        return "Datos inválidos"
    
print(detectar_palindromo("Abc"))
print(detectar_palindromo("Aba"))
print(detectar_palindromo("atata"))
print(detectar_palindromo("cubo"))
print(detectar_palindromo("nanan"))