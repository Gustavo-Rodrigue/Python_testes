dados_originais = [10, 20, 30]

dados_referencias = dados_originais

copia_dados = [10, 20, 30]

print("Se os dados originais e os dados referencias forem iguais a resposta abaixo deverá ser true")
print(dados_originais is dados_referencias)

print("Se os dados originais e os dados cópia forem iguais a resposta abaixo deverá ser true")
print(dados_originais is copia_dados)

print("Se os dados cópia e os dados referencias forem iguais a resposta abaixo deverá ser true")
print(dados_referencias is copia_dados)