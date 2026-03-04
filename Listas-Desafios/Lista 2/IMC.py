
print("Vamos calcular seu IMC")

peso = float(input("Digite seu peso(em Kg) "))
alt = float(input("Digite sua Altura(em M) "))

imc = peso/alt**2

if imc < 18.5:
    print(f"Seu IMC é: {imc:.2f}. Você está abaixo do peso")
elif 18.5 <= imc <= 24.99 :
    print(f"Seu IMC é: {imc:.2f}. Você está com o peso normal")
elif 25 <= imc <= 29.99 :
    print(f"Seu IMC é: {imc:.2f}. Você está com sobrepeso")
else:
    print(f"Seu IMC é: {imc:.2f}. Você possui obesidade") 