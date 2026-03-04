x = []

for i in range(5):
    x.append(float(input(f"Digite o {i+1}º número: ")))

soma = sum(x)
quant = len(x)
média = soma / quant

print(f"O resultado da soma dos itens é: {soma:.2f}")
print(f"A média é: {média:.2f}")