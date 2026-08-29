

cola_diferidos = []
cola_notificaciones = []
continuar = "s"

while continuar == "s":
    nombre = input("Nombre del cliente: ")
    hora = int(input("Hora del pedido: "))

    if hora >= 8 and hora <= 16:
        dirrecion = input("Direccion: ")
        cantidad = int(input("¿Cuantos platos? "))

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
                cola_notificaciones.append(nombre)
                print("pedido pendiente de pago")

    else:
        cola_diferidos.append(nombre)
        print("Fuera de horario, pedido para mañana")

    continuar = input("otro pedido? (s/n)")


print("pedidos pendientes de pago: ", cola_notificaciones)
print("pedidos diferidos:", cola_diferidos)





