def passo1(passos):
    while True:
        passos +=  int(input("Quantos passos a tripulação irá prosseguir? \n>>"))
        passo2(passos)

  
def passo2(passos):
    while True:
        if passos > 67 :
            print("\nMontanha avistada a frente")
            print("\nIniciando medida de superação de obstaculos")
            passo3(passos)
        else:
            passo1(passos)
    
def passo3(passos):
    while True:
        passos = passos
        meio = int(input("\nComo gostaria de tentar ultrapassar a montanha? \nEscalando(4) \nContornando(5) \n>>"))
        if meio == 4:
            passo4(passos)
        elif meio == 5:
            passo5(passos)
        else:
            print("Digite algo valido")
            continue

def passo4(passos):
    sorteio = (passos + 18)* 25 / 10
    if sorteio > 270:
        print("\nParabéns vocês conseguiram escalar a montanha!!")
        passo6(passos)
    else:
        print("\nOH NÃO, Um deslizamento aconteceu e todos cairam, vocês voltaram a estaca zero!")
        passos += 15
        passo3(passos)
    
def passo5(passos):
    sorteio = (passos - 13)* 15 / 12
    if sorteio > 72:
        print("\nSe passaram algumas horas e vocês contornaram a montanha!!")
        passo6(passos)
    else:
        print("\nOH NÃO, O entorno da montanho estava coberto de ameaças e todos decidiram voltar, vocês estão na estaca zero!")
        passos += 15
        passo3(passos)

def passo6(passos):
    resp = str(input("\nVocê gostaria de explorar a área montanhosa?(S/N) \n>>"))
    if resp == "S" or resp == "s":
        sorteio = (passos - 29)*30 / 4
        if sorteio > 450:
            print("\nVocês encontraram uma área rica em minerais, iniciem os estudos")
            passo7(passos)
        elif sorteio > 340:
            print("\nVocês encontraram sinal de vida alienígena, iniciem os estudos")
            passo7(passos)
        else:
            print("\nPOXA! Era apenas uma área rochosa, voltem a andar")
            passo1()
    else:
        print("Já que não irá explorar, volte a andar pelo planeta")
        passo1(0)
        
def passo7(passos):
    tempo = int(input("\nGostaria de analisar suas descobertas por quantos dias? \n>>"))
    if tempo > 60:
        pontos = passos * tempo/2
        passo8(pontos)
    elif tempo > 30:
        pontos = passos * tempo/4
        passo8(pontos)
    else:
        pontos = passos * tempo/6
        passo8(pontos)

def passo8(pontos):
    resultado = pontos
    resposta = input("\nGostaria de terminar sua jornada?S/N \n>>")
    if resposta == "N" or resposta == "n":
        print("\nRetornando a exploração...")
        passo2(0)
    elif resposta == "S" or resposta == "s":
        passo9(resultado) 

def passo9(pontos):
    if pontos > 10000:
        qualificacao = "Jogador expert em exploração"
    elif pontos > 5000:
        qualificacao = "Jogador excelente, falta pouco para se tornar um expert"
    elif pontos > 1000:
        qualificacao = "Jogador muito bom, mas da para melhorar"
    else:
        qualificacao = "Continue jogando para se tornar um jogador melhor"
    
    print(f"Sua pontuação final foi de {pontos:.0f}")
    print(f"Você foi qualificado como {qualificacao}")
    print("RETORNANDO A TERRA COM DESCOBERTAS INCRIVEIS")
    quit()

passo1(0)