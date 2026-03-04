preco = []
while preco != 0 :
    while preco > 0:
        preco.append(float(input("Digite o Valor do seu produto(Use . para centavos): ")))
    
    print("Valor Invalido")
    preco.append(float(input("Digite o Valor do seu produto(Use . para centavos): ")))

total = sum(preco)
quanti = len(preco)

media = total / quanti

print(f"Sua compra possui {quanti} itens.")
print(f"O valor total de sua compra é: R${total:.2f}")
print(f"A média de valor por item é: R${media}")
