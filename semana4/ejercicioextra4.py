

def generartabla(tamano):
    tabla=[]
    for fila in range(1, tamano+1):
        filalista=[]
        for columna in range(1, tamano+1):
           producto = 0
           for i in range(columna):
               producto += fila
           filalista.append(producto)
        tabla.append(filalista)     
    return tabla


def imprimirtabla(tabla):
    for fila in tabla:
        linea = ""
        for numero in fila:
            linea += str(numero) + " "
        print(linea)

tamano = int(input("Tamaño de la tabla: "))
if tamano < 2 or tamano > 5:
    print("debe ser entre 2 y 5")
else:
    tabla = generartabla(tamano)
    imprimirtabla(tabla)

    renglon= int(input("Renglon: "))
    columna= int(input("Columna: "))
    producto = tabla[renglon - 1][columna - 1]
    print(f"El producto de {renglon} y {columna} es: {producto}")



             
       
           