autenticator = True

numbers = []
div = set()
while autenticator == True:
    number = input("Digite um numero (para parar a execução, digite X): ")
    if number == 'X':
        autenticator = False
    else:
        numbers.append(int(number))

    for number in numbers:
        if number % 2 == 0 or number % 3 == 0:
            div.add(number)

print(f'Os numeros que sao divisiveis por 2 ou 3 entre os números informados são: ', *div)