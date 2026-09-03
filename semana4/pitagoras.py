

def tabla():
    matriz = []
    for fila in range(1, tamano +1):
        fila = []
        for columna in range(1, tamano +1):
            fila.append(fila * columna)
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        for numero in fila:
            print(numero, end=' ')

            