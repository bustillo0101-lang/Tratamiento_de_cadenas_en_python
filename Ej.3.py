#3. Una cadena introducida por teclado, contar las consonantes de una cadena.

cadena = input("Ingrese una cadena: ").lower()
vocales = "aeiou"
contador = 0

for c in cadena:
    if c.isalpha() and c not in vocales:
        contador += 1

print(f"Cantidad de consonantes: {contador}")