#Categoria = {"Pena": <65; "Leve"

nome = input("Digite o nome do lutador: ")
peso = float(input("Digite o peso do lutador: "))

if peso < 65:
  categoria = "Pena"
elif 65 <= peso < 72:
  categoria = "Leve"
elif 72 <= peso < 79:
  categoria = "Ligeiro"
elif 79 <= peso < 86:
  categoria = "Meio-médio"
elif 86 <= peso < 93:
  categoria = "Médio"
elif 93 <=  peso < 100:
  categoria ="Meio-pesado"
elif peso >= 100:
  categoria = "Pesado"
else:
  print("ERROR")

print(f'O lutador {nome} pesa {peso} Kg e se enquadra na categoria {categoria}')
