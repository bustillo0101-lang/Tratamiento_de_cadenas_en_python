#7. Una cadena introducida por teclado, eliminar los espacios extremos de la cadena.

cadena = input("Ingrese una cadena: ")

# Eliminar espacios al inicio
inicio = 0
while inicio < len(cadena) and cadena[inicio] == " ":
    inicio += 1

# Eliminar espacios al final
fin = len(cadena) - 1
while fin >= 0 and cadena[fin] == " ":
    fin -= 1

cadena_limpia = cadena[inicio:fin+1]
print(f"Cadena sin espacios extremos: '{cadena_limpia}'")