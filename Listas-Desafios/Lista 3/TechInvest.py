especiais = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '', '{', '|', '}', '~']
i=0
respostas = []
perguntas = ["Digite seu salário mensal \n", "Digite seu gasto mensal \n", "Qual seu Nivel de coragem para investir(Digite um valor de 1 a 10) \n"]
while True:
    while True:
        nome_invalido = False
        nome = str(input("Digite seu nome completo: "))
        
        if not nome:
            print("Por favor, Digite algo")
            continue

        for letra in nome:
            if letra in especiais:
                nome_invalido = True
                break

        if nome_invalido:
            print("Nome inválido, caracteres especiais não são permitidos")
        else:
            print(f"Nome cadastrado")
            break

    while i <= 2:
        respostas.append(float(input(perguntas[i])))
        if not respostas[i]:
            print("Por favor, Digite algo")
            continue
        else:
            print("Resposta cadastrada")
            i += 1

    if respostas[1] > respostas[0]:
        print("Alerta de Emergência Financeira \nSua presença não é permitida em nosso banco!")
    elif respostas[0] > respostas[1]:
        reserva = respostas[0]*6
        sobra = respostas[0] - respostas[1]
        guardar = sobra/2
        meses_reserva = reserva/guardar
        print(f"Olá, {nome}")
        print(f"Sua reserva de segurança deve ser de: R${reserva:.2f}")
        print(f"Caso vc guarde metade de sua sobra, que é igual a: R${guardar:.2f}, você irá ter sua reserva em {meses_reserva:.0f} meses.")


    if respostas[2] < 4:
        taxa = 1.05
        print("Baseado na sua coragem, seu melhor investimento será Tesouro Direto")
    elif respostas[2] > 4 and respostas[2] < 7:
        taxa = 1.20
        print("Baseado na sua coragem, seu melhor investimento será Fundos Imobiliários")
    else:
        taxa = 1.3
        print("Baseado na sua coragem, seu melhor investimento será Ações de Tecnologia")
    
    j = 0
    while j <= 1:
        valor = float(input("Qual valor você gostaria de investir?\n"))

        if not valor:
            print("Por favor, Digite algo")
            continue
        elif valor is letra:
            print("Digite apenas números")
            continue
        elif valor > sobra:
            print(f"Valor de investimento superior a sua sobra mensal, digite outro valor")
            continue
        else: 
            j += 1

        anos = int(input("Por quantos anos você gostaria de investir? \n"))

        if not anos:
            print("Por favor, Digite algo")
            continue
        elif anos is letra:
            print("Digite apenas números")
            continue
        else: 
            j += 1

    investimento = valor * (taxa ** anos)

    print(f"Seu investimento podera render até {taxa*100:.0f}% ao ano \nO valor daqui {anos:.0f} anos será de {investimento:.2f}")
    
    break
