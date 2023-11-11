nome = input("Digite o nome do lutador: ")
peso = float(input("Digite o peso do lutador em Kg: "))

categoria = ""
if peso < 65:
    categoria = "Pena"
if peso < 72:
    categoria = "Leve"
if peso < 79:
    categoria = "Ligeiro"
if peso < 86:
    categoria = "Meio-médio"
if peso < 93:
    categoria = "Médio"
if peso < 100:
    categoria = "Meio-pesado"
else:
    categoria = "Pesado"

print(f"\nNOME DO LUTADOR: {nome}")
print(f"PESO: {peso}")
print(f"Frase a ser exibida: 'O lutador {nome} pesa {peso} Kg e se enquadra na categoria {categoria}!'")
