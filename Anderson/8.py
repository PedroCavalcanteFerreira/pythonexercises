def obtem_dadosFuncionarios():
    dados = {}

    matricula = input("Informe a matrícula do funcionário: ")
    nome = input("Informe o nome do funcionário: ")
    genero = input("Informe o gênero do funcionário: ")
    departamento = input("Informe o departamento do funcionário: ")
    tempo_servico = int(input("Informe o tempo de serviço do funcionário: "))
    salario = float(input("Informe o salário do funcionário: "))

    dados['Matricula'] = matricula
    dados['Nome'] = nome
    dados['Gênero'] = genero
    dados['Departamento'] = departamento
    dados['Tempo de Serviço'] = tempo_servico
    dados['Salário'] = salario

    return dados

# Exemplo de uso da função
funcionario = obtem_dadosFuncionarios()
print(funcionario)
