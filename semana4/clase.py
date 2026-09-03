
lista = []
contador = 0

while contador < 10:
    valor = int(input("Ingresa un numero entre -10 y 10: "))
    if valor >= -10 and valor <= 10:
        contador += 1
        lista.append(valor)
    else:
        print("rango incorrecto")

print(lista)

for numero in lista:
    if numero < 0:
        print(f"{'*' * abs(numero):>10} |")
    elif numero > 0:
        print(f"{'':>10} | {'*' * numero}")
    else:
        print(f"{'':>10} 0")
