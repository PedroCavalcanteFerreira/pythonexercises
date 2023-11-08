def tabuada(numero):
    print(f"A tabuada do número {numero} é:")
    for i in range(11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")


repeat = "S"
while repeat == "S":
    numero = int(input("forneça um número: "))
    tabuada(numero)
    repeat = input("\ndeseja continuar? [S/N]: ")
    
