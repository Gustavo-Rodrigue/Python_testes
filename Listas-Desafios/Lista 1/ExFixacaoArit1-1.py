# EXERCICIO FIXACAO - OPERADORES ARITMÉTICOS 1
num1 = float(input(f"Digite o primeiro número: "))
num2 = float(input(f"Digite o segundo número: "))

soma = num1 + num2
diferenca = num1 - num2
produto = num1 * num2

if num2 != 0:
    divisaoReal = num1 / num2
    resto = num1 % num2

print(f"A soma é {soma}")
print(f"A diferença é {diferenca}")
print(f"O produto é {produto}")
print(f"A divisão real é {divisaoReal:.2f}")
print(f"O Resto é {resto}")