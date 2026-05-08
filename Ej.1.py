#1. Una cadena introducida por teclado, contar los caracteres de la cadena sin usar la función length() o len()

cadena = input("Ingrese una cadena: ")

contador = 0
for _ in cadena:
    contador += 1

print(f"La cadena tiene {contador} caracteres.")