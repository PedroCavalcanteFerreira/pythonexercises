import random

n = int(input("Informe a quantidade de elementos que a lista deve conter (1-50): "))
while not (1 <= n <= 50):
    print("Você deve informar um valor entre 1 e 50!")
    n = int(input("Tente novamente: "))

listaA = []
for i in range(n):
    listaA.append(random.randint(-100, 100))

neg = []
pos = []
for i in listaA:
    if i < 0:
        neg.append(i)
    else:
        pos.append(i)

print(listaA)
print(f'\nA lista de números negativos tem {len(neg)} elementos, sendo eles: \n{neg}')
print(f'\nA lista de números positivos tem {len(pos)} elementos, sendo eles: \n{pos}')