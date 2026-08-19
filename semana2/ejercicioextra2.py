

adultos = 0
tedades = 0

visitas = int(input("Cuantas visitas son?"))

for i in range(visitas):
    edad = int(input("Que edad tiene esa persona?: "))
    tedades += edad

    if edad >= 18:
        adultos += 1

promedio = tedades / visitas

print("promedio de edad: ", promedio)
print("Hay ", adultos, " adultos")



