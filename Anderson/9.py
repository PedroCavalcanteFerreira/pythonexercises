import random

def calcular_digito_verificador(codigo):
    soma = 0
    peso = 2

    for digito in reversed(codigo):
        soma += int(digito) * peso
        peso += 1

    resto = soma % 7
    digito_verificador = 7 - resto

    return digito_verificador

codigo = random.randint(10000, 99999)
digito_verificador = calcular_digito_verificador(str(codigo))

codigo_completo = str(codigo) + "-" + str(digito_verificador)
print("Código de produto: " + codigo_completo)
