qnt = int(input("Informe a quantodade de matriculas: "))
worker = {}
def add():
    for i in range(qnt):
        nome = input("Informe o nome do(a) funcionário(a): ")
        gen = input("Informe o gênero do(a) funcionário(a) (F/M/NB): ")
        dep = input("Informe o departamento do(a) funcionário(a): ")
        time = float(input("Informe o tempo de serviço do(a) funcionário(a): "))
        salario = float(input("Informe o salário do(a) funcionário(a): R$"))
        worker["Matricula"[i]] = nome, gen, dep, time, salario


add()
print(f'\n{worker}')