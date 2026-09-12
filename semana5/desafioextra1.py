

tupla = ("Maria", "Jose", "Carlos","Lucia", "Pedro")
print("tercer elemento", tupla[2])

nuevo1= input("Primer nombre: ")
nuevo2= input("Segundo nombre: ")

tupla_actualizada = tupla + (nuevo1, nuevo2)

lista = list(tupla_actualizada)
lista.sort()

print("Lista ordenada en orden alfabetico: ")
for persona in lista:
    print(persona)

print("\nTotal de personas en la lista de espera:", len(lista))