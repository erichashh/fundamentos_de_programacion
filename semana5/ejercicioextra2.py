

def buscar(agenda, nombre):
    return agenda.get(nombre)

agenda = {
    "Ana": "555-0101",
    "Luis": "555-0102",
    "Mía": "555-0103"
}

nuevo_nom = input("Nombre del nuevo:")
nuevo_num = input("Numero del nuevo:")

agenda[nuevo_nom] = nuevo_num
print("Gente registrada:",", ".join(agenda.keys())) 
# el join arma la línea con todos los nombres separados por comas respetando el orden 

buscar_nom = input("A quien buscas?: ")
telefono = buscar(agenda, buscar_nom)

if telefono:
    print(f"El telefono de {buscar_nom} es: {telefono}")
else:
    print(f"{buscar_nom} no está")


