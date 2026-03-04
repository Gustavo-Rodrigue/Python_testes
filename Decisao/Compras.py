print("Vamos descobrir o valor de sua compra com desconto.")
valor = float(input("Qual valor de sua compra? "))

if 100 < valor <= 200 :
    desconto = 0.1
elif 200 < valor <= 500:
    desconto = 0.2
elif valor > 500:
    desconto = 0.3
else:
    print(f"Seu valor final será: {valor:.2f}, nenhum desconto aplicado")

valor_final = valor * (1 - desconto)

print (f"Seu desconto é de: {desconto*100:.0f}%. E o valor a ser pago será: {valor_final:.2f}")