

def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

frase = input("Escribe una frase: ")
print("Longitud de la frase: ", len(frase), "caracteres")

frase_mayusculas = frase.upper()
print("frase en mayusculas:", frase_mayusculas)

frase_reemplazada = frase.replace("python", "programación")
print("frase reemplazada:", frase_reemplazada)

total_palabras = contar_palabras(frase)
print("cantidad de palabras:", total_palabras)