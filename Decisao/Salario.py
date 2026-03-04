salario = float(input("Informe seu sálario mensal para verificar o reajuste: "))

if salario <= 280:
    reajuste = 0.2
elif salario <= 700:
    reajuste = 0.15
elif salario <= 1500:
    reajuste = 0.1
else:
    reajuste = 0.05

valAumento = salario * reajuste
novosal = salario + valAumento
percentual = 100 * reajuste
print(f"Seu sálario era de: R${salario:.2f}")
print(f"Você terá {percentual:.0f}% de aumento")
print(f"O valor do aumento será de: R${valAumento:.2f}")
print(f"Seu novo sálario é de: R${novosal:.2f}")
