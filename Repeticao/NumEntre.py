n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

for i in range(n1 + 1, n2) or range(n2 + 1, n1):
    print(i, end=' ')