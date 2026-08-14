
tcuenta = float(input("total cuenta: "))
ppropina = float(input("porcentaje de la propina: "))
npersonas = int(input("numero de personas: "))

propina = tcuenta * (ppropina / 100)
totalcpropina = tcuenta + propina
ppp = totalcpropina / npersonas

print(f"\npropina: {propina:.2f}")
print(f"total: {totalcpropina:.2f}")
print(f"Cada quien paga: {ppp:.2f}")