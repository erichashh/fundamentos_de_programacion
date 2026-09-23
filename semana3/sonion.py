

filas = int(input("Cuantas filas quieres: "))

for i in range(1, filas + 1):
    for espacio in range(filas - i):
        print(" ", end="")

    for asterisco in range(2 * i - 1):
        print("*", end="")

    print()