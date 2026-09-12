

def sumar_tupla(tupla):
    suma = 0
    for numero in tupla:
        suma = suma + numero
    return suma


def buscar_telefono(diccionario, nombre):
    if nombre in diccionario:
        return diccionario[nombre]
    else:
        return


def contar_palabras(texto):
    lista_palabras = texto.split()
    return len(lista_palabras)


def menu_tuplas():
    print("Tuplas")


    numeros = (1, 52, 0, 67, 19)
    print("original:", numeros)

    print("tercer elemento de la tupla es:", numeros[2])

    try:
        dato1 = float(input("numero para agregar a la tupla: "))
        dato2 = float(input("numero para agregar a la tupla: "))
    except ValueError:
        print("Solo puedes escribir numeros")
        return

    nueva_tupla = numeros + (dato1, dato2)
    print("nueva tupla:", nueva_tupla)

    lista_numeros = list(nueva_tupla)
    lista_numeros.sort()
    print("Lista ordenada:", lista_numeros)

    resultado = sumar_tupla(nueva_tupla)
    print("La suma de todos los elementos de la tupla es:", resultado)


def menu_diccionarios():
    print("diccionario")

    contactos = {
        "Juan": "1234",
        "maria": "5678",
        "Ppedro": "9012"
    }

    nombre_nuevo = input("nombre del nuevo contacto: ")
    telefono_nuevo = input("telefono del nuevo contacto: ")
    contactos[nombre_nuevo] = telefono_nuevo
    print("Contacto agregado")

    print("\nnombres registrados:")
    for nombre in contactos:
        print("-", nombre)

    nombre_buscar = input("\nescribe el nombre que quieres buscar: ")
    telefono_encontrado = buscar_telefono(contactos, nombre_buscar)

    if telefono_encontrado:
        print("El telefono de", nombre_buscar, "es:", telefono_encontrado)
    else:
        print("no existe")

def menu_excepciones():
    print("\nexcepciones")

    try:

        numero1 = int(input("primer numero entero: "))
        numero2 = int(input("el segundo numero entero: "))

        suma = numero1 + numero2
        print("La suma es:",suma)

        division = numero1 / numero2
        print("la division es:",division)

    except ZeroDivisionError:
        print("no es posible dividir entre 0")

    except ValueError:
        print("escribe unicamente enteros")

    except Exception as error:
        print("error:", error)


def menu_strings():
    print("\nstrings")

    mensaje ="python es un lenguaje de programacion muy versatil"
    print("mensaje original:",mensaje)


    print("La longitud del mensaje es:", len(mensaje))


    mensaje_mayusculas = mensaje.upper()
    print("mensaje en mayusculas:", mensaje_mayusculas)


    mensaje_modificado = mensaje.replace("versatil", "poderoso")
    print("palabra reemplazada:", mensaje_modificado)

    total_palabras = contar_palabras(mensaje)
    print("Palabras en el mensaje:", total_palabras)


def mostrar_menu():
    print("1 tuplas")
    print("2 diccionarios")
    print("3 excepciones")
    print("4 strings")
    print("5 finalizar")

while True:
    mostrar_menu()
    opcion = input("elige(1-5)")

    if opcion == "1":
        menu_tuplas()
    elif opcion == "2":
        menu_diccionarios()
    elif opcion =="3":
        menu_excepciones()
    elif opcion == "4":
        menu_strings()
    elif opcion == "5":
        print("\n...")
        break
    else:
        print("\nelige un numero del 1 al 5.")


