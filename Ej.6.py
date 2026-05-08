#6. Una cadena introducida por teclado, eliminar los espacios de la cadena

cadena = input("Ingrese una cadena: ")
sin_espacios = ""

for c in cadena:
    if c != " ":
        sin_espacios += c

print(f"Cadena sin espacios: '{sin_espacios}'")