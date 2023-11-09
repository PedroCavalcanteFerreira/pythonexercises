import random

cod = '10123'#str(random.randint(10000, 99999))
scod = []
peso = [2, 3, 4, 5, 6, 7]

for i in cod:
    scod.append(int(i))

def calc():
    soma = 0
    for i in range(0, len(scod)):
        soma += (scod[i] * peso[i])
    return soma % 7
    
print(f'Resultado: {cod}-{calc()}')