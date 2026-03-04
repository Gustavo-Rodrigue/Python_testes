x = []

for i in range(5):
    x.append(float(input(f"Digite o {i+1}º número : ")))

maior_num = max(x)


print(f"O maior número da lista é: {maior_num}")