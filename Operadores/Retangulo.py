
print("Iremos calcular a Área e o perimetro em Metros")

alt = float(input("Digite o valor da altura em metros "))
lado = float(input("Digite o valor do lado em metros "))

perimetro = alt*2 + lado*2
area = alt*lado

print(f"Os valores obtidos foram")
print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")