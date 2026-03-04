# EXERCICIO FIXACAO - FOR 1


numero = int(input("Digite um número inteiro: "))

print(f"Tabuada do {numero}:\n")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
