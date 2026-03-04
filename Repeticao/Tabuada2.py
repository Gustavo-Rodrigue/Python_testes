tabuada = []

# Gerando os dados
for i in range(1, 11):
    for j in range(1, 11):
        tabuada.append(i * j)

# Mostrando os dados
for t in range(1, 11):
    print(f"\n--- A tabuada de {t} é: ---")
    for y in range(10):
        # O pulo do gato: (t-1)*10 desloca o índice para o bloco correto
        indice = ((t - 1) * 10) + y
        print(f"{t} x {y + 1} = {tabuada[indice]}")

