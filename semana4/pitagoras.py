



# UTILICE EL ASTERISCO PARA CONSTRUIR LA TABLA, NO PARA SACAR EL RESULTADO :D

def hacer_cuadro(n):
    datos = []
    for a in range(1, n+1):
        temp=[]
        for b in range(1, n+1):
            temp.append(a*b)
        datos.append(temp)
    return datos

def mostrar_cuadro(datos):
    for grupo in datos:
        for valor in grupo:
            print(str(valor).rjust(4), end="")
        print()

def buscar_valor(datos, x, y):
    return datos[x-1][y-1]

n = int(input("Tamanño de la tabla: "))
datos = hacer_cuadro(n)
mostrar_cuadro(datos)

x = int(input("Renglon: "))
y = int(input("Columna: "))

print(buscar_valor(datos, x, y))

