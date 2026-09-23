

votos = {"rojo": 0, "azul": 0, "verde": 0}

for i in range(5):
    color = input("Por quien votas? (rojo, azul o verde)")
    if color in votos:
        votos[color] += 1
    else:
        print("Invalido")

ganador = max(votos, key=votos.get)

print("Resultados")
for color, cantidad in votos.items():
    print(color, ":", cantidad)

print("El color que gano es", ganador, "con", votos[ganador], "votos")