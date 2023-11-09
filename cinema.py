#if idade <= 12: ingresso = 25.00
# if 12 < idade < 61: ingresso = 40.00 if day == "segunda": ingresso = 25.00
#if idade >= 61: ingresso = 20.00
data = input("\nDatas disponíveis:\n     Domingo | Segunda | Terça | Quarta | Quinta | Sexta | Sábado\nInforme o dia da semana para a compra do(s) ingresso(s): ")
quantidade = int(input("Informe a quantidade de ingressos: "))
tipos = []
print("Tipos de ingressos:\n     Junior: R$25.00 | Standart: R$40.00 | Senior: R$ 20.00\n")
for i in range(quantidade):
    tipos.append(input(f"Informe o tipo do ingresso {i+1}: "))
valor = {"Junior": 25.00, "Standart": 40.00, "Senior": 20.00}

total_ingressos = sum([valor[t] for t in tipos]) * quantidade
print(total_ingressos)