

dinero = 0

while dinero < 100:
    costo = float(input("Costo del boleto (0, 30 o 45) "))

    if costo == 0:
        print("menor de 3 años, sin cargo")
        continue

    dinero +=costo

    if dinero >= 100:
        break
 
print("dinero que se acumulo:", dinero)


