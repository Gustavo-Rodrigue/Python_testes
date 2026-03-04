vendas_brutas = [(101, "Monitor", 5, 1200.0), (102, "Mouse", 50, 80.0), (103,
"Teclado", 8, 150.0), (104, "Case", 3, 50.0)]

itens = len(vendas_brutas)

i = 0
j = 0

estoque_baixo = []
reajuste = []

valor_total = 0

print("<< Sistema de Vendas >>")

while i < itens:
    valor_total += vendas_brutas[i][2] * vendas_brutas[i][3]
    if vendas_brutas[i][2] < 10:
        estoque_baixo.append(vendas_brutas[i][1])
        i += 1
    else:
        i += 1

print("Os itens abaixo estão com estoque baixo:")
print(f"{estoque_baixo} \n")

print(f"O valor de seu inventário é de: R${valor_total:.2f} \n")

while True:
    resp = str(input("Gostaria de fazer um reajuste?(S/N) \n"))
    if resp == "S" or "s":
        while j < itens:
            novo_valor = float(input(f"\nDigite o novo valor para o {vendas_brutas[j][1]}(valor atual: {vendas_brutas[j][3]}): \n"))
            reajuste.append((vendas_brutas[j][0], vendas_brutas[j][1], vendas_brutas[j][2], novo_valor))
            valor_total += reajuste[j][2]*reajuste[j][3]
            j += 1
    elif resp == "N" or "n":
        print("Operação cancelada \n")
        break
    else :
        print("Digite S ou N!! \n")
        continue

    print(f"\nO valor do seu inventário após o reajuste será de {valor_total:.2f} \n")
    print(f"Sua nova lista de Tuplas será {reajuste}")
    break
    

