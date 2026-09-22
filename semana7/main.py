
import time


#DEFINICION DE FUNCIONES
#-----------------------


def bienvenida():
    nombre = input("¿Cual es tu nombre?")

    #linea para llevar orden y que se vea bonito
    linea = "-" * 40 
    mensaje = "Bienvenido al sistema para pedir " + nombre

    #mostrar la bienvenida
    print(linea)
    print(mensaje)
    print(linea)

    return nombre


def pantalla_carga():
    for i in range(5):
        print("cargando"+ "." * (i+1))
        time.sleep(1)


def pedir_fecha():
    dia = int(input("Día del pedido: "))
    mes = int(input("Mes del pedido"))
    anio = int(input("Año del pedido"))

    fecha = dia, mes, anio


def imprimir_menu(matriz):
    for fila in matriz:
        print(fila[0]+ "." + fila[1])


def leer_archivo():
    archivos_disponibles = {
        "1": "data/menu.txt",
        "2": "data/colonias.txt",
        "3": "data/clientes.txt",
        "4": "data/historial.txt"
    }
    print("archivos que puedes ver:")
    for clave, valor in archivos_disponibles.items():
        print(clave + ". "+ valor)

    eleccion = input("Cual quieres abrir? (numero): ")
    camino = archivos_disponibles[eleccion]

    with open(camino, "r") as archivo: 
        contenido = archivo.read
        print(contenido)



def registrar_pedido():
    nombre_cliente = input("Nombre del cliente: ")
    hora = int(input("Hora del pedido: "))

    if hora >= 8 and hora <= 16:
        direccion = input("Direccion: ") # usar en recibo reporte
        cantidad = int(input("Cuantos platos?"))

        subtotal = 0
        for i in range(cantidad):
            plato = input("Nombre del plato: ")
            precio = float(input("Precio del plato:"))
            subtotal = subtotal + precio

        colonia = input("Esta en la colonia? (s/n)")
        if colonia == "s":
            envio = 0
        else:
            envio = 40

        total = subtotal + envio
        print("total a pagar:", total)

        pago = input("Pago en efectivo (s/n)")
        if pago == "s":
            print("pedido enviado a cocina")
        else:
            confirmado = input("Transferencia confirmada (s/n): ")
            if confirmado == "s":
                print("pedido enviado a cocina")
            else:
                cola_notificaciones.append(nombre_cliente)
                print("pedido pendiente de pago")

        return total

    else:
        cola_diferidos.append(nombre_cliente)
        print("Fuera de horario, pedido para mañana")
        return 0


# FLUJO PRINCIPAL DEL PROGRAMA
#-----------------------------

matriz_menu = [
    ["1", "Registar pedido"],
    ["2", "Ver el menu de platos"],
    ["3", "Leer archivo"],
    ["4", "Escribir o anexar archivo"],
    ["5", "Revisar reporte de cierre"],
    ["6", "Ver pendientes/diferidos"],
    ["7", "Salir"],
]

cola_diferidos = []
cola_notificaciones = []

nomre_usuario = pantalla_carga()
pantalla_carga

opcion = ""

while opcion != 7:
    imprimir_menu(matriz_menu)
    opcion = input("¿Que quieres hacer?: ")

    if opcion == "1":
        print("()")
    elif opcion == "2":
        print("()")
    elif opcion == "3":
        print("()")
    elif opcion == "4":
        print("()")
    elif opcion == "5":
        print("()")
    elif opcion == "6":
        print("()")
    elif opcion == "7":
        print("Saliendo")
    else:
        print("error, invalido")       








