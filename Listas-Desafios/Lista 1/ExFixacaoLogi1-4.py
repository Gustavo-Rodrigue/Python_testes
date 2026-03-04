# EXERCICIO FIXACAO - OPERADORES LÓGICOS 1

presenca = float(input("Digite a sua nota de presença: "))
media = float(input("Digite a sua média: "))

if media >= 7 and presenca >= 75:
    print(f"O Aluno foi aprovado! Com presença igual á {presenca}, e com média igual á {media}")
else:
    print(f"O Aluno foi reprovado! Presença: {presenca} e Média: {media}")