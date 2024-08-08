# Inicializando contadores
votos_candidato = [0, 0, 0, 0]  # índices 0 a 3 para candidatos 1 a 4
votos_nulos = 0
votos_branco = 0
total_votos = 0

# Entrada de votos
while True:
    voto = int(input("Digite o voto (1 a 4 para candidatos, 5 para nulo, 6 para branco, 0 para encerrar): "))

    if voto == 0:
        break

    if 1 <= voto <= 4:
        votos_candidato[voto - 1] += 1
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_branco += 1
    else:
        print("Voto inválido. Tente novamente.")

    total_votos += 1

# Calculando percentagens
percentual_nulos = (votos_nulos / total_votos) * 100 if total_votos > 0 else 0
percentual_branco = (votos_branco / total_votos) * 100 if total_votos > 0 else 0

# Determinando o candidato vencedor
indice_max_votos = votos_candidato.index(max(votos_candidato))
candidato_vencedor = indice_max_votos + 1

# Exibindo resultados
print("\nResultados da Eleição:")
print("======================")
print(f"Total de votos para cada candidato:")
for i in range(len(votos_candidato)):
    print(f"Candidato {i + 1}: {votos_candidato[i]} votos")
print(f"Votos nulos: {votos_nulos}")
print(f"Votos em branco: {votos_branco}")
print(f"Percentual de votos nulos sobre o total de votos: {percentual_nulos:.2f}%")
print(f"Percentual de votos em branco sobre o total de votos: {percentual_branco:.2f}%")
print(f"Candidato vencedor: Candidato {candidato_vencedor}")



