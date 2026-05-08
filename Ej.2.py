#2. Una cadena introducida por teclado, contar las vocales de la cadena.

cadena = input("Ingrese una cadena: ").lower()
vocales = "aeiou"
contador = 0

for c in cadena:
    if c in vocales:
        contador += 1

print(f"Cantidad de vocales: {contador}")