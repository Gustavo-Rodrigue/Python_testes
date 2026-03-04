# EXERCICIO FIXACAO - OPERADORES IDENTIDADE 1

a = [1, 2]
b = [1, 2]

c = a
if a is b:
    print(a is b)
else:
    print("False")
if a is c:
    print(a is c)
else:
    print("False")