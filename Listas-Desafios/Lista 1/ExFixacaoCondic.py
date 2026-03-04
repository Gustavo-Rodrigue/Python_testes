# EXERCICIO FIXACAO - CONDICIONAL 1

idade = float(input("Digite qual a sua idade: "))

if idade >= 18:
    print("Adulto")
elif idade >= 5 and idade <= 12:
    print("Infantil")
elif idade >= 13 and idade <= 17:
    print("Juvenil")
else:
    print("Invalido")