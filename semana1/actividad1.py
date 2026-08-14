

usuario = input("Cual es su nombre de usuario?: ")

youtube = float(input("Cuantas horas ves youtube al dia?: "))
netflix = float(input("Cuantas horas ves netflix al dia?:"))
tiktok = float(input("Cuantas horas haces doomscrolling en tiktok al dia?:"))
videojuegos = float(input("Cuantas horas juegas videojuegos al dia?: "))
vscode = float(input("Cuantas horas programas en vscode al dia?: "))

ttotal_horas = youtube + netflix + tiktok + videojuegos + vscode
porcentajedia = (ttotal_horas/24)*100


print("Resumen de", usuario)

print(f"youtube: {youtube:.2f} horas diarias")
print(f"netflix: {netflix:.2f} horas diarias")
print(f"tiktok: {tiktok:.2f} horas diarias")
print(f"videojuegos: {videojuegos:.2f} horas diarias")
print(f"vscode: {vscode:.2f} horas diarias")

print(f"Tiempo total: {ttotal_horas:.2f} horas diarias")
print(f"Porcentaje de tiempo al dia: {porcentajedia:.2f}%")















"""
print(usuario,"tu tiempo total es de",ttotal_horas,"horas al dia")
print(usuario,"tu porcentaje de tiempo al dia es de ",porcentajedia,"%")

"""




