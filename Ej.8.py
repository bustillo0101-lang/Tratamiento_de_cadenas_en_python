#8. Una cadena introducida por teclado, contar los diptongo de una cadena.

cadena = input("Ingrese una cadena: ").lower()
vocales = "aeiou"
cerradas = "iu"
diptongos = 0
i = 0

while i < len(cadena) - 1:
    c1 = cadena[i]
    c2 = cadena[i+1]
    if c1 in vocales and c2 in vocales:
        # Diptongo si al menos una es cerrada
        if c1 in cerradas or c2 in cerradas:
            diptongos += 1
            i += 1  # saltar la siguiente vocal para no solapar
    i += 1

print(f"Cantidad de diptongos (simplificado): {diptongos}")