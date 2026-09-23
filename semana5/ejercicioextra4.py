


def conteo(texto):
    palabras = texto.split()
    return len(palabras)

mensaje = "python es un lenguaje poderoso"
print("Longitud: ", len(mensaje))

mayusuclas = mensaje.upper()
print("En mayusculas: ", mayusuclas)

reemplazo = mensaje.replace("python", "programacion")
print("Reemplazado: ", reemplazo)

total = conteo(mensaje)
print("total de palabras: ", total)