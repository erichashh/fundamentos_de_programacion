Algoritmo Sistema_Pedidos_Capricho
	Definir continuar Como Lógico
	Definir nombre_cliente, direccion, nombre_plato Como Cadena
	Definir hora_pedido, cantidad_platos, i Como Entero
	Definir precio_plato, subtotal, costo_envio, total_pagar Como Real
	Definir en_colonia, cancelar, es_efectivo, pago_confirmado Como Lógico
	Definir contador_diferidos, contador_notif Como Entero
	Dimensionar cola_diferidos(50)
	Dimensionar cola_notificaciones(50)
	Definir cola_diferidos, cola_notificaciones Como Cadena
	contador_diferidos <- 0
	contador_notif <- 0
	continuar <- Verdadero
	Mientras continuar Hacer
		Escribir 'Nuevo pedido'
		Escribir 'Nombre del cliente:'
		Leer nombre_cliente
		Escribir 'Hora del pedido (0-23):'
		Leer hora_pedido
		Si hora_pedido>=8 Y hora_pedido<=16 Entonces
			Escribir 'Direccion de entrega:'
			Leer direccion
			Escribir 'Cuantos platos tiene el pedido?'
			Leer cantidad_platos
			subtotal <- 0
			Para i<-1 Hasta cantidad_platos Hacer
				Escribir 'Nombre del plato:'
				Leer nombre_plato
				Escribir 'Precio del plato:'
				Leer precio_plato
				subtotal <- subtotal+precio_plato
			FinPara
			// monto minimo
			Si subtotal<100 Entonces
				Escribir 'El pedido no llega al minimo de $100 '
			SiNo
				// rgla_1
				Escribir 'Esta dentro de la colonia? (Verdadero/Falso)'
				Leer en_colonia
				Si en_colonia==Falso Entonces
					costo_envio <- 40
				SiNo
					costo_envio <- 0
				FinSi
				total_pagar <- subtotal+costo_envio
				Escribir 'Total a pagar: $', total_pagar
				Escribir 'Desea cancelar el pedido? (Verdadero/Falso)'
				Leer cancelar
				Si cancelar==Verdadero Entonces
					Escribir 'Pedido cancelado'
				SiNo
					Escribir 'Pago en efectivo? (Verdadero/Falso)'
					Leer es_efectivo
					Si es_efectivo==Verdadero Entonces
						Escribir 'Pedido enviado a cocina'
					SiNo
						Escribir 'Transferencia confirmada? (Verdadero/Falso)'
						Leer pago_confirmado
						Si pago_confirmado==Verdadero Entonces
							Escribir 'Pedido enviado a cocina'
						SiNo
							Si contador_notif<50 Entonces
								contador_notif <- contador_notif+1
								cola_notificaciones[contador_notif] <- nombre_cliente
								Escribir 'Pedido pendiente de pago, agregado a la cola'
							SiNo
								Escribir 'Cola de notificaciones llena, avisar al administrador'
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		SiNo
			Si contador_diferidos<50 Entonces
				contador_diferidos <- contador_diferidos+1
				cola_diferidos[contador_diferidos] <- nombre_cliente
				Escribir 'Fuera de horario, el pedido guardado para el siguiente dia'
			SiNo
				Escribir 'Cola llena, avisar al administrador'
			FinSi
		FinSi
		Escribir 'Otro pedido? (Veerdadero/Falso)'
		Leer continuar
	FinMientras
	Escribir 'Pedidos pendientes de pago'
	Para i<-1 Hasta contador_notif Hacer
		Escribir cola_notificaciones[i]
	FinPara
	Escribir 'Pedidos diferidos'
	Para i<-1 Hasta contador_diferidos Hacer
		Escribir cola_diferidos[i]
	FinPara
	Escribir 'Fin del programa'
FinAlgoritmo
