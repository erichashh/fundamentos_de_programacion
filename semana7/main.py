
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
    mes = int(input("Mes del pedido: "))
    anio = int(input("Año del pedido: "))

    fecha = dia, mes, anio
    return fecha


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

    #aqui agregare try-except, me gusta porque tiene dos puntos de falla
    try:
        camino = archivos_disponibles[eleccion]
        with open(camino, "r") as archivo: 
            contenido = archivo.read()
            print(contenido)
    except KeyError:
            print("esa opcion no existe, intenta con un numero valido")
    except FileNotFoundError:
        print("El archivon no se encontro en la ruta esperada")

def consultar_menu():
    with open("data/menu.txt", "r") as archivo:
        contenido = archivo.read()
        print("-Menu de platos disponible-")
        print(contenido)

def pendientes():
    print("-Pedidos diferidos-")
    print(cola_diferidos)
    print("-Pedidos pendientes de pago-")
    print(cola_notificaciones)


def escribir_archivo(Fecha):
    archivos_disponibles = {
        "1": "data/menu.txt",
        "2": "data/colonias.txt",
        "3": "data/clientes.txt",
        "4": "data/historial.txt"
    }

    print("archivos disponibles") 
    for numeros, nombre_archivo in archivos_disponibles.items():
        print(numeros + ". " + nombre_archivo)

    eleccion= input("En que archivo quieres escribir?: ")
    ruta = archivos_disponibles[eleccion]

    texto_usuario = input("Que quieres escribir? ")
    dia, mes, anio = Fecha
    fecha_texto = str(dia) + "/" + str(mes) +"/"+ str(anio)

    try:
        ruta = archivos_disponibles[eleccion]
        with open(ruta,"a") as archivo:
            archivo.write(fecha_texto + "-"+texto_usuario +"\n") 
    except KeyError:
        print("esa opcion no existe, intenta con un numero valido")
    except FileNotFoundError:
        print("El archivo no se encontro en la ruta esperada")



    with open(ruta, "a") as archivo:
        archivo.write(fecha_texto + "-"+ texto_usuario+ "\n") 


def reporte_cierre(Fecha):
    dia, mes, anio = Fecha
    fecha_texto = str(dia) + "/" + str(mes) +"/"+ str(anio)

    contenido_reporte = "Reporte de cierre" + fecha_texto + "\n"
    contenido_reporte = contenido_reporte + "Total vendido dia: " + str(total_dia) + "\n"
    contenido_reporte = contenido_reporte + "Pedidos diferidos: " + str(cola_diferidos)+ "\n"
    contenido_reporte = contenido_reporte + "Pedidos pendientes de pago: " + str(cola_notificaciones)+ "\n"

    with open("data/reporte_cierre.txt", "w") as archivo:
        archivo.write(contenido_reporte)
    print(contenido_reporte)
    



def registrar_pedido(Fecha):
    nombre_cliente = input("Nombre del cliente: ")

    #aqui uso otro try para asegurarnos que la hora introducida sea la correcta
    try:
        hora = int(input("Hora del pedido: "))
    except ValueError:
        print("La hora debe de ser un numero entre las 8 y las 16 horas (formato 24 hrs), intenta de nuevo")
        return 0
    
    if hora >= 8 and hora <= 16:
        direccion = input("Direccion: ") # usar en recibo reporte
        try:
            cantidad = int(input("Cuantos platos?"))
        except ValueError:
            print("la cantidad de platos debe de ser un numero, intenta de nuevo")
            return 0

        subtotal = 0
        for i in range(cantidad):
            plato = input("Nombre del plato: ")
            try:
                precio = float(input("Precio del plato:"))
            except ValueError:
                print("El precio debe de ser un numero, intenta de nuevo")
                return 0
            subtotal = subtotal + precio

        colonia = input("Esta en la colonia? (s/n)")
        if colonia == "s":
            envio = 0
        else:
            envio = 40

        total = subtotal + envio
        print("total a pagar:", total)

        #aqui ira el recibo
        dia, mes, anio = Fecha
        fecha_texto = str(dia) + "/" + str(mes) +"/"+ str(anio)

        contenido_recibo = "Fecha:" + fecha_texto +"\n"
        contenido_recibo = contenido_recibo + "Cliente: " + nombre_cliente +"\n"
        contenido_recibo = contenido_recibo + "Direccion: " + direccion +"\n"
        contenido_recibo = contenido_recibo + "Total: " + str(total)

        #el nombre va a cambiar siempre
        nombre_recibe = "data/recibo_" + nombre_cliente + "_" + str(hora) + ".txt"
        with open (nombre_recibe, "w") as archivo:
            archivo.write(contenido_recibo)


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
    ["1", "Registrar pedido"],
    ["2", "Ver el menu de platos"],
    ["3", "Leer archivo"],
    ["4", "Escribir o anexar archivo"],
    ["5", "Revisar reporte de cierre"],
    ["6", "Ver pendientes/diferidos"],
    ["7", "Salir"],
]



total_dia = 0
cola_diferidos = []
cola_notificaciones = []

nombre_usuario = bienvenida()
pantalla_carga()
Fecha = pedir_fecha()

opcion = ""

while opcion != "7":
    imprimir_menu(matriz_menu)
    opcion = input("¿Que quieres hacer?: ")

    if opcion == "1":
        total_pedido = registrar_pedido(Fecha)
        total_dia = total_dia + total_pedido
    elif opcion == "2":
        consultar_menu()
    elif opcion == "3":
        leer_archivo()
    elif opcion == "4":
        escribir_archivo(Fecha)
    elif opcion == "5":
        reporte_cierre(Fecha)
    elif opcion == "6":
        pendientes()
    elif opcion == "7":
        print("Saliendo")
    else:
        print("error, invalido")       








