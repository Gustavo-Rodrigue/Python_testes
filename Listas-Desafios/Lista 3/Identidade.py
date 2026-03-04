saldo_inicial = 1000

checkpoint = saldo_inicial 

if checkpoint is saldo_inicial :
    print("São iguais")
else:
    print("Não são iguais")

especiais = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '', '{', '|', '}', '~']
i=0
while True:
    while True:
        nome_invalido = False
        auditor = str(input("Digite o nome do Auditor: "))
        
        if not auditor:
            print("Por favor, Digite algo")
            continue

        for letra in auditor:
            if letra in especiais:
                nome_invalido = True
                break

        if nome_invalido:
            print("Nome inválido, caracteres especiais não são permitidos")
        else:
            print(f"Auditor {auditor} registrado com sucesso!")
            break

    while i < 4:
        print("Deseja realizar uma transação de débito ou de crédito?")
        resp = int(input("(1)Débito \n(2)Crédito \n"))
        if resp == 1:
            valor = float(input("Digite o valor da transação de débito: \n"))
            if valor <= 500:
                saldo_inicial += valor
                i +=1
            else:
                print("Valor alto para transação")
        elif resp == 2:
            valor = float(input("Digite o valor da transação de crédito: \n"))
            if valor <= 500:
                saldo_inicial -= valor
                i +=1
            elif saldo_inicial < valor:
                print("Saldo insuficiente")
                continue
            else:
                print("Valor alto para transação")
                continue
                
    print(f"Seu novo saldo é de {saldo_inicial:.2f}")
    break

if checkpoint is saldo_inicial :
    print("São iguais")
else:
    print("Não são iguais")