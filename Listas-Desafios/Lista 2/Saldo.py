saldo = float(500)

resp = int(0)
while resp != 3:

    print(f"Seu saldo é de R${saldo:.2f}")
    print("O que você deseja fazer?")
    resp = int(input("(1)Depositar \n(2)Sacar \n(3)Sair \n"))

    if resp == 1 :
        deposito = float(input("Digite o valor que deseja adicionar: \n"))
        saldo += deposito
        print(f"Você depositou R${deposito:.2f} \n")
    elif resp == 2:
        i = 0
        while i == 0: 
            sacar = float(input("Digite o valor que deseja sacar: \n"))
            if sacar <= saldo:
                saldo -= sacar
                print(f"Você sacou R${sacar:.2f} \n")
                i += 1
            else:
                print("Saldo Insuficiente")

    elif resp > 3:
        print("Digite uma opção válida")



    while resp == 3:
        print("Tem certeza que deseja sair? ")
        certeza = int(input("(1)Sair \n(2)Retornar \n"))
        if certeza == 1:
            resp = 3
        elif certeza == 2:
            resp = 0
        else :
            print("Digite uma opção válida")

print("Você saiu!")