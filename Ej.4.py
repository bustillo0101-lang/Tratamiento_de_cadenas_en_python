#4. Una cadena introducida por teclado, contar los caracteres especiales (@#%$)

cadena = input("Ingrese una cadena: ")
especiales = "@#/$%_-.:,;"
contador = 0

for c in cadena:
    if c in especiales:
        contador += 1

print(f"Cantidad de caracteres especiales (@#%$): {contador}")