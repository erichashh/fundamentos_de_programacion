

import pdb

pnino = 0
pmenor = 30
pmayor= 45

descuentomayor = .12
descuentoprofe = .10
descuentoestudiante = .10

tvisitantes = int(input("Cuantos visitantes son?"))

lista_pagos = []
totapagar =0
contador = 0

while contador < tvisitantes:
    contador += 1
    print("Visitante #", contador)

    edad = int(input("edad del visitante:"))

    if edad== "salir":
        break

    if edad < 3:
        precio = pnino
    elif edad < 18:
        precio = pmenor
    else:
        precio = pmayor

    tipo = "n"
    if edad >= 18:
        tipo = input("descuento? a=adulto, p=profesor, e=estudiante, n=ni uno: ")

        if tipo == "a":
            descuento = descuentomayor
        elif tipo == "p":
            descuento = descuentoprofe
        elif tipo == "e":
            descuento = descuentoestudiante
        else:
            descuento = 0

        pago = precio - (precio * descuento)
        totapagar += pago
        print("pago de este vistitante: ", pago)

        lista_pagos.append(pago)

print("Resumen de todo")

for pago in lista_pagos:
    print("Pago:", pago)

print("Total de visitantes:", tvisitantes)
print("Total a pagar:", totapagar)