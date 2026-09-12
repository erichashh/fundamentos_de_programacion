


while True:
    try:
        num1 = int(input("Primer numero entero: "))
        break
    except ValueError:
        print("error, ingresa un numero entero valido")


while True:
    try:
        num2 = int(input("Segundo numero entero: "))
        break
    except ValueError:
        print("error, ingresa un numero entero")


try:
    resultado= num1/num2
    print("El resultado de", num1, "entre", num2, "=", resultado)
except ZeroDivisionError:
    print("error, no se puede dividir entre 0")


    