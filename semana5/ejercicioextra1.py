

calificaciones = (7.5, 9.0, 8.0, 6.5, 10.0)

nuevas_cali = ()

for i in range(0,2):
    dos_cali = float(input("Ingresa dos calificaicones nuevas: "))
    nuevas_cali += (dos_cali,)

print("tercera calificacion", calificaciones[2])

nueva_tupla = calificaciones + nuevas_cali
print("Nueva tupla", nueva_tupla)

lista = sorted(nueva_tupla)
print("Lista ordenada", lista)

def sumar(calificaciones):
    return sum(calificaciones)

print("suma de todo", sumar(nueva_tupla))