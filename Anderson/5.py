numeros = []
divisiveis_por_2_ou_3 = []

while True:
    numero = input("Digite um número inteiro positivo (ou 'X' para sair): ")
    if numero.lower() == "x":
        break
    numero = int(numero)
    numeros.append(numero)
    if numero % 2 == 0 or numero % 3 == 0:
        divisiveis_por_2_ou_3.append(numero)

print("\nNúmeros digitados pelo usuário:")
for numero in numeros:
    print(numero)

print("\nNúmeros divisíveis por 2 ou 3:")
for numero in divisiveis_por_2_3:
    print(numero)
