def tabuada():
    numero = int(input("FORNEÇA UM NÚMERO: "))
    print(f"A tabuada do número {numero} é:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Chamando a função para gerar a tabuada
tabuada()
