


dinero = 0

while dinero < 100:
    edad = int(input("edad? "))

    if edad < 3:
        costo = 0
        print("menor de 3 años, sin cargo")
        continue
    elif edad >= 3 and edad <= 17:
        costo = 30
    else:
        costo = 45

    dinero += costo
    if dinero >= 100:
        break

print("dinero que se acumulo:", dinero)


