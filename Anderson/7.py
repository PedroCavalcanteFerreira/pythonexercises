preco_crianca = 25.00
preco_padrao = 40.00
preco_senior = 20.00

dia_semana = input("Informe o dia da semana para a compra dos ingressos: ")
quantidade_crianca = int(input("Informe a quantidade de ingressos para crianças: "))
quantidade_padrao = int(input("Informe a quantidade de ingressos padrão: "))
quantidade_senior = int(input("Informe a quantidade de ingressos para idosos: "))

subtotal_crianca = preco_crianca * quantidade_crianca
subtotal_padrao = preco_padrao * quantidade_padrao
subtotal_senior = preco_senior * quantidade_senior

if dia_semana.lower() == "segunda":
    subtotal_padrao = preco_crianca * quantidade_padrao

total_descontos = 0
if dia_semana.lower() == "segunda":
    total_descontos = (preco_padrao - preco_crianca) * quantidade_padrao

total_geral = subtotal_crianca + subtotal_padrao + subtotal_senior

print("\nSubtotal para ingressos de crianças: R$", subtotal_crianca)
print("Subtotal para ingressos padrão: R$", subtotal_padrao)
print("Subtotal para ingressos de idosos: R$", subtotal_senior)

if total_descontos > 0:
    print("Total de descontos: R$", total_descontos)

print("Total geral a ser pago: R$", total_geral)
