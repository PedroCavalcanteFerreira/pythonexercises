#if idade <= 12: ingresso = 25.00
# if 12 < idade < 61: ingresso = 40.00 if day == "segunda": ingresso = 25.00
#if idade >= 61: ingresso = 20.00
data = input("\nDatas disponíveis:\n     Domingo | Segunda | Terça | Quarta | Quinta | Sexta | Sábado\nInforme o dia da semana para a compra do(s) ingresso(s): ")
quantidade = int(input("Informe a quantidade de ingressos: "))
tipos = []
print("Tipos de ingressos:\n     Junior: R$25.00 | Standart: R$40.00 | Senior: R$ 20.00\n")
for i in range(quantidade):
    tipos.append(input(f"Informe o tipo do ingresso {i+1}: "))

valor = {"junior": 25.00, "standart": 40.00, "senior": 20.00}
desconto = 0
sub_ju = 0
sub_stan = 0
sub_sen = 0
def sub():
    global sub_ju, sub_stan, sub_sen
    for i in tipos:
        if i.lower() == 'junior':
            sub_ju += valor["junior"]
        if i.lower() == "standart":
            sub_stan += valor["standart"]
        if i.lower() == "senior":
            sub_sen += valor["senior"]
if data.lower() == "segunda":
    desconto = 20 * tipos.count("standart")

sub()
print(f"\nSubtotal Junior: R${sub_ju:.2f}")
print(f"Subtotal Standart: R${sub_stan:.2f}")
print(f"Subtotal Senior: R${sub_sen:.2f}")

if desconto > 0:
    print(f"\nTotal de desconto: R${desconto:.2f}")
else:
    print('\nNão há descontos')

total = sub_ju + sub_stan + sub_sen - desconto
print(f"\nTotal geral a ser pago: R${total:.2f}")