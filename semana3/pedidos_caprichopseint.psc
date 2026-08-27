Proceso Sistema_Pedidos_Capricho

	Definir continuar Como Logico
	Definir nombre_cliente, telefono_cliente, direccion Como Cadena
	Definir hora_pedido, cantidad_comida, i Como Entero
	Definir nombre_plato Como Cadena
	Definir precio_plato, subtotal, costo_envio, total_pagar Como Real
	Definir en_colonia, es_efectivo, pago_confirmado, pedido_atendido Como Logico
	Definir contador_diferidos, contador_notif Como Entero

	Dimension cola_diferidos[50]
	Dimension cola_notificaciones[50]
	Definir cola_diferidos, cola_notificaciones Como Cadena

	contador_diferidos <- 0
	contador_notif <- 0
	continuar <- Verdadero

	Mientras continuar Hacer

		Escribir "=== Nuevo pedido entrante ==="
		Escribir "Nombre del cliente:"
		Leer nombre_cliente
		Escribir "Telefono del cliente:"
		Leer telefono_cliente
		Escribir "Hora del pedido (formato 24h):"
		Leer hora_pedido

		Si hora_pedido >= 8 Y hora_pedido <= 16 Entonces

			Escribir "Direccion de entrega:"
			Leer direccion

			Escribir "Cuantos platos tiene el pedido?"
			Leer cantidad_comida

			subtotal <- 0

			Para i <- 1 Hasta cantidad_comida Hacer
				Escribir "Nombre del plato ", i, ":"
				Leer nombre_plato
				Escribir "Precio del plato:"
				Leer precio_plato
				subtotal <- subtotal + precio_plato
			FinPara

			Escribir "La direccion esta dentro de Lomas del Marques? (Verdadero/Falso)"
			Leer en_colonia

			Si en_colonia == Falso Entonces
				costo_envio <- 40
			SiNo
				costo_envio <- 0
			FinSi

			total_pagar <- subtotal + costo_envio
			Escribir "Total a pagar: $", total_pagar

			Escribir "El cliente pagara en efectivo? (Verdadero/Falso)"
			Leer es_efectivo

			Si es_efectivo == Verdadero Entonces
				pedido_atendido <- Verdadero
			SiNo
				Escribir "La transferencia esta confirmada? (Verdadero/Falso)"
				Leer pago_confirmado
				Si pago_confirmado == Verdadero Entonces
					pedido_atendido <- Verdadero
				SiNo
					pedido_atendido <- Falso
				FinSi
			FinSi

			Si pedido_atendido == Verdadero Entonces
				Escribir "Pedido enviado a cocina"
			SiNo
				contador_notif <- contador_notif + 1
				cola_notificaciones[contador_notif] <- nombre_cliente
				Escribir "Aviso: pedido pendiente de pago, se agrego a la cola de notificaciones"
			FinSi

		SiNo
			contador_diferidos <- contador_diferidos + 1
			cola_diferidos[contador_diferidos] <- nombre_cliente
			Escribir "Fuera de horario. Pedido guardado para el siguiente dia"
		FinSi

		Escribir "Desea recibir otro pedido? (Verdadero/Falso)"
		Leer continuar

	FinMientras

	Si contador_notif > 0 Entonces
		Escribir "Pedidos pendientes de pago:"
		Para i <- 1 Hasta contador_notif Hacer
			Escribir cola_notificaciones[i]
		FinPara
	FinSi

	Si contador_diferidos > 0 Entonces
		Escribir "Pedidos diferidos para el siguiente dia:"
		Para i <- 1 Hasta contador_diferidos Hacer
			Escribir cola_diferidos[i]
		FinPara
	FinSi

	Escribir "Fin del programa"

FinProceso
