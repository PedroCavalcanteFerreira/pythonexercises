import random

quantidade = int(input("Informe a quantidade de números desejados: "))

numeros = []
for _ in range(quantidade):
    numero = random.randint(-100, 100)
    numeros.append(numero)

print("\nNUMEROS GERADOS AUTOMATICAMENTE:")
print(" ".join(str(numero) for numero in numeros))

soma_positivos = sum(numero for numero in numeros if numero > 0)
soma_negativos = sum(numero for numero in numeros if numero < 0)

print("\nSOMA DOS NÚMEROS POSITIVOS:", soma_positivos)
print("SOMA DOS NÚMEROS NEGATIVOS:", soma_negativos)
