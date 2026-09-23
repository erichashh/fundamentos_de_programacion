

numeros = (8, 3, 15, 1, 9, 4)
contactos = {"María": "12345", "José": "54321", "Carlos": "098765", "Lucía": "08092"}

def dividir():
    try:
        a = int(input("primer numero: "))
        b = int(input("segundo numero: "))
        print("resultado:", a/b)
    except ValueError:
        print("ingresa numeros enteros validos.")
    except ZeroDivisionError:
        print(" no se puede dividir entre cero.")

def analizar():
    texto = input("Ingresa una frase: ")
    print("Longitud:", len(texto))
    print("Mayúsculas:", texto.upper())
    print("Reemplazo:", texto.replace("Python", "programación"))
    print("Palabras:", len(texto.split()))

while True:
    print("\n1. Números ordenados\n2. Buscar teléfono\n3. Dividir\n4. Analizar texto\n5. Salir")
    op = input("Opción: ")

    if op == "1":
        print(sorted(numeros))
    elif op == "2":
        nombre = input("Nombre: ")
        print(contactos.get(nombre, "No encontrado"))
    elif op == "3":
        dividir()
    elif op == "4":
        analizar()
    elif op == "5":
        print("Adiós")
        break
    else:
        print("Opción no válida")