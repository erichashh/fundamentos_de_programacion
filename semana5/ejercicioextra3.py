


try:
    num1 = int(input("1er numero entero: "))
    num2 = int(input("2do numero entero: "))

    resultado = num1/num2
    print(f"{num1} entre {num2} es: {resultado}")

except ValueError:
    print("error, debes ingresar numeros enteros")

except ZeroDivisionError:
    print("error, no puedes dividir entre cero")
