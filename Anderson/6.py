import random

a = int(input("Infore o tamanho da lista A: "))
lista_a = []
for i in range(a):
    lista_a.append(random.randint(-9999,9999))
print(f'listaA = {lista_a}\n')
b = int(input("Infore o tamanho da lista B: "))
lista_b = []
for i in range(b):
    lista_b.append(random.randint(-9999,9999))
print(f'listaB = {lista_b}\n')

result = []
for i in range(min(a, b)):
    result.append(lista_a[i])
    result.append(lista_b[i])
if a > b:
    result.extend(lista_a[b:])
else:
    result.extend(lista_b[a:])

print(f'Lista resultante: {result}')