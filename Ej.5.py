#5. Una cadena introducida por teclado, contar los espacios entre medio de una cadena.

cadena = input("Ingrese una cadena: ")
contador = 0

for c in cadena:
    if c == " ":
        contador += 1

print(f"Cantidad de espacios: {contador}")