

tminutos =int(input("tiempo en minutos: "))
dias = tminutos // 1440
mrestantes= tminutos % 1440
horas = mrestantes // 60
minutos = mrestantes % 60

print(f"\nDias: {dias}")
print(f"Horas: {horas}")
print(f"Minutos: {minutos}")


