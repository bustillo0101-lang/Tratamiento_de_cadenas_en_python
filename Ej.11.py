#11. Dos cadena introducida por teclado, la 1 era cadena de n caracteres y 2da cadena de un carácter, eliminar los caracteres de la 1 era cadena, lo que se repite en la 2da cadena.

cadena1 = input("Ingrese la primera cadena (N caracteres): ")
cadena2 = input("Ingrese la segunda cadena (un solo carácter): ")

if len(cadena2) != 1:
    print("La segunda cadena debe tener exactamente un carácter.")
else:
    caracter = cadena2[0]
    resultado = ""
    for c in cadena1:
        if c != caracter:
            resultado += c
    print(f"Cadena resultante: '{resultado}'")