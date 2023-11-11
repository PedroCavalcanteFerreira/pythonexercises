ini = int(input("informe o valor de incio: "))
end = int(input("informe o valor de fim: "))

if end < ini:
    print("O valor de fim deve ser maior que o valor de inicio! Invertendo os valores...")
    ini, end = end, ini

print(f"os valores divisiveis por 5 entre {ini} e {end} são: ")
for i in range(ini, end+1):
    if (i % 5) == 0:
        print(i)