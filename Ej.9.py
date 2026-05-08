#9. Una cadena introducida por teclado, contar los hiatos de una cadena.

cadena = input("Ingrese una cadena: ").lower()
abiertas = "aeo"  # a, e, o
hiatos = 0
i = 0

while i < len(cadena) - 1:
    c1 = cadena[i]
    c2 = cadena[i+1]
    if c1 in abiertas and c2 in abiertas:
        hiatos += 1
        i += 1
    i += 1

print(f"Cantidad de hiatos (a/e/o seguidas): {hiatos}")