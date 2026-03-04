especiais = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '', '{', '|', '}', '~']

valores = []
descarte = []

resp = 1
def validar():

    while True:
        nome_invalido = False
        nome = str(input("Digite o nome da Filial(sem caracteres especiais): \n"))
        
        if not nome:
            print("Por favor, Digite algo \n")
            continue

        for letra in nome:
            if letra in especiais:
                nome_invalido = True
                break

        if nome_invalido:
            print("Filial inválida, caracteres especiais não são permitidos \n")
        else:
            print(f"\nFilial cadastrada \n")
            break

    return nome
def separar():
    if resp <= 0 or resp > 10000:
        descarte.append(resp)
    else:
        valores.append(resp)


def analise(lista):

    soma = sum(lista)

    if len(lista) > 0:
        media = soma / len(lista)
    else:
        media = 0 
    return soma, media

def status():

    media = results[1]

    if media > 5000:
        return "Alta performance"
    elif media < 2000 and media < 5000:
        return "Performance Estável"
    else:
        return "Performance Crítica"
    
def listagem():
    for i in range(len(valores)):
        lista = i + 1
        print(f"{lista}- {valores[i]}")
while True:
    
    nome = validar()

    while resp != 0:

        resp = (float(input("Digite o valor da sua venda(caso queira cancelar digite 0): \n")))
        separar()
        results = analise(valores)
    
    print(f"Seja bem-vindo responsável pela Filial: {nome}")
    print(f"Seu nivel de performance é: {status()}")
    print(f"O valor total das vendas será de: R${results[0]}")
    print(f"A média das vendas será de: R${results[1]}")
    print("Abaixo você verá uma listagem de vendas:")
    print(listagem())

    break
