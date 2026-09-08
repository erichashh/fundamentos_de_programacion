

candidatos = {
    "A": 0,
    "B": 0,
    "C": 0
}

cantidad = int(input("¿Cuántos votos serán?: "))

for c in range(1, cantidad + 1):
    voto = input(f"¿Por quién votas?: {c}").upper()

    if voto in candidatos:
        print(f"Voto para {voto}")
        candidatos[voto] += 1
    else:
        print("Inválido")

for candidato, votos in candidatos.items():
    print(f"Opción {candidato}, votos: {votos}")

ganador = max(candidatos.items(), key=lambda elemento: elemento[1])
print(f"El ganador es {ganador[0]} con {ganador[1]} votos.")