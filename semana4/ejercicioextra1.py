
def suma_matriz(matriz):
    total = 0

    for fila in matriz:
        for valor in fila:
            total += valor
    return total

def imprimir_matriz(matriz):
    for fila in matriz:
        for valor in fila:
            print(valor, end=' ')
        print()

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

imprimir_matriz(matriz)
print("suma de todos los numeros:", suma_matriz(matriz))