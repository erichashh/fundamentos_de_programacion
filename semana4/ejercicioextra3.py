

def multiplicarcolumna(matriz, columna):
    producto =1
    for fila in matriz:
        numero = fila[columna]
        resultado = 0
        for i in range(numero):
            resultado = resultado + producto
        producto = resultado
    return producto

matriz = [[1,2,3],[4,5,6],[7,8,9],[2,4,6]]

col = int(input("Pon el nmumero de columna (0,1,2): "))
resultado = multiplicarcolumna(matriz, col)
print("El producto de la columna "+ str(col)+ " es: "+str(resultado))
