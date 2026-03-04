
i = int(0)

sim = ["sim","Sim","sIm","siM","SIM","SIm","sIM","SiM","S","s"]

resposta = str(input("Telefonou para a vítima? "))

if resposta in sim:
    i += 1

resposta = str(input("Esteve no local do crime? "))

if resposta in sim:
    i += 1

resposta = str(input("Mora perto da vítima? "))

if resposta in sim:
    i += 1

resposta = str(input("Devia para a vítima? "))

if resposta in sim:
    i += 1

resposta = str(input("Já trabalhou com a vítima? "))

if resposta in sim:
    i += 1

if i == 5:
    print("Você é o Assasino")
elif i >= 3 :
    print("Você é cúmplice do crime")
elif i >= 1:
    print("Você é um suspeito")
else:
    print("Você é inocente")