frase = input(str("Digite um frase qualquer "))
nv = 0
vogais = [
    "A", "a", "Á", "á", "Â", "â", "Ã", "ã", "À", "à",
    "E", "e", "É", "é", "Ê", "ê",
    "I", "i", "Í", "í",
    "O", "o", "Ó", "ó", "Ô", "ô", "Õ", "õ",
    "U", "u", "Ú", "ú", "Ü", "ü"
]
for i in range (len(frase)):
    if frase[i] in vogais:
        nv += 1
i += 1


print(f"Sua frase possui {nv} vogais")