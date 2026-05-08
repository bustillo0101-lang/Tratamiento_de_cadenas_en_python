#10. Una cadena introducida por teclado, verificar si es palindrome, sin usar una función

cadena = input("Ingrese una cadena: ").lower()
# Eliminar espacios y signos de puntuación si se desea, pero solo comparar caracteres
# Para simplificar, solo comparamos la cadena original sin modificar.

es_palindromo = True
longitud = 0
for _ in cadena:
    longitud += 1

for i in range(longitud // 2):
    if cadena[i] != cadena[longitud - 1 - i]:
        es_palindromo = False
        break

if es_palindromo:
    print("Es palíndromo.")
else:
    print("No es palíndromo.")