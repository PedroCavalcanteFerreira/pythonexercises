import random

a = int(input("Informe o tamanho da lista A: "))
b = int(input("Informe o tamanho da lista B: "))
lista_a = []
lista_b = []
result = []

while a == b:
    print ("A e B devem ser diferentes")
    a = int(input("Informe o tamanho da lista A: "))
    b = int(input("Informe o tamanho da lista B: "))
def gerar(a, b):
    for i in range(a):
        lista_a.append(random.randint(-9999, 9999))
    for i in range(b):
        lista_b.append(random.randint(-9999, 9999))
def mesclar(lista_a, lista_b):
    for i in range(min(a, b)):
        result.append(lista_a[i])
        result.append(lista_b[i])
    if a > b:
        result.extend(lista_a[b:])
    else:
        result.extend(lista_b[a:])



gerar(a, b)
print(f"\nLista A: {lista_a}")
print(f"\nLista B: {lista_b}")
mesclar(lista_a, lista_b)
print(f'\nLista resultante: {result}\n')