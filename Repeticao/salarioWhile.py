salario = float(input("Digite seu salário mensal: "))
print("")

ano = 1995
taxa = 0.015

while ano <= 2025:
    if ano == 1995:
        taxa_exibicao = 0
    elif ano == 1996:
        taxa_exibicao = taxa
        salario *= (1 + taxa_exibicao)
    else:
        taxa *= 2
        taxa_exibicao = taxa
        salario *= (1 + taxa_exibicao)

    print(f"No ano de {ano}, seu aumento será de {taxa_exibicao * 100:.1f}%")
    print(f"E seu salário com aumento será: R${salario:.2e}")
    print("")
    ano += 1