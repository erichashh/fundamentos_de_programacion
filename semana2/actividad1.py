

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
    print("Visitante #", contador +1)

    edad_input = int(input("edad del visitante (o salir para terminar):"))

    if edad_input== "salir":
        break

    edad=int(edad_input)

    if edad < 0:
        print("escribe una edad valida")
        continue

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

        montodescuento = precio * descuento
        pago = precio - montodescuento
        totapagar += pago
        print("pago de este vistitante: ", pago)

        lista_pagos.append((contador +1, edad, tipo, precio, montodescuento, pago))
        contador +=1

print("Resumen de todo")

for numero,edad,tipo,precio,montodescuento,pago  in lista_pagos:
    print(f"\nVisitante {numero}:")
    print(f"Edad: {edad}")
    print(f"tipo de descuento: {tipo}")
    print(f"precio base: ${precio:.2f}")
    print(f"Monto de descuento: ${montodescuento:.2f}")
    print(f"total a pagar: ${pago:.2f}")

print("total de visitantes:", tvisitantes)
print("Total a pagar:", totapagar)