import random

numbers = []
positive = 0
negative = 0
def gerar(quantidade):
    for i in range(quantidade):
        numbers.append(random.randint(-9999,9999))

def sum():
    global positive, negative
    for number in numbers:
        if number < 0:
            negative += number
        else:
            positive += number
        
quantidade = int(input('Informe a quantidade de números desejados: '))
gerar(quantidade)
sum()
print(f'\nNUMEROS GERADOS AUTOMATICAMENTE: ')
print(*numbers, sep=", ")
print(f'\nSOMA DOS NÚMEROS POSITIVOS: {positive}\nSOMA DOS NÚMEROS NEGATIVOS: {negative}')
