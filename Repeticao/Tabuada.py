x = int(input("Digite um valor: "))

tabuada = []
for i in range(10):
    tabuada.append((i+1)* x)


print(f"A tabuada de {x} é:")
for t in range(10):
    print(f"{x}*{t+1} = {tabuada[t]} ")
