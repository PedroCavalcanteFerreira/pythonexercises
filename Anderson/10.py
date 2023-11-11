N = int(input("Informe um número inteiro entre 1 e 50: "))

if N < 1 or N > 50:
    print("Número inválido. O número deve estar entre 1 e 50.")
else:
    A = []
    for _ in range(N):
        numero = random.uniform(-100, 100)
        A.append(numero)

    NEG = []
    POS = []
    for numero in A:
        if numero < 0:
            NEG.append(numero)
        elif numero > 0:
            POS.append(numero)

    print("Lista A:", A)
    print("Lista NEG:", NEG)
    print("Quantidade de elementos em NEG:", len(NEG))
    print("Lista POS:", POS)
    print("Quantidade de elementos em POS:", len(POS))
