


def sumafila(fila):
   suma = 0
   for numero in fila:
      suma = suma + numero
   return suma

def mostrartabla(matriz):
   for fila in matriz:
      linea = ""
      for numero in fila:
         linea = linea +str(numero) + " "
      print(linea)

matriz = [[3,1,4],[1,5,9],[2,6,5]]
mostrartabla(matriz)

for i in range(len(matriz)):
   resultado = sumafila(matriz[i])
   print("suma de la fila"+ str(i)+": "+str(resultado))