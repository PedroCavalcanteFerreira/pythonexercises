inicio = int(input("Informe o valor de início: "))
fim = int(input("Informe o valor de fim: "))

if fim <= inicio:
    print("O valor de fim deve ser maior do que o valor de início. Invertendo os valores...")
    inicio, fim = fim, inicio

print(f"\nValores divisíveis por 5 no intervalo de {inicio} a {fim}:")
for num in range(inicio, fim + 1):
    if num % 5 == 0:
        print(num)
