nota1 = float(input("Digite uma das notas do aluno: "))
nota2 = float(input("Digite a outra nota do aluno: "))

media = (nota1 + nota2)/2

if media >= 7:
    print(f"Sua média é {media:.2f}, você está aprovado")
else:
    print(f"Sua média é {media:.2f}, você está reprovado")