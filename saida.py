idade: int
nome: str
salario: float
sexo: str

idade = 22
nome = "Ademir"
salario = 6.130
sexo = "Masculino"

print(f"O funcionario {nome},do sexo {sexo}, e recebe {salario:.2f}, de salario e tem {idade} anos. ")
print(" O funcionario {:s}, do sexo {:s}, recebe {:f} de salario, e tem {:d} anos".format(nome, sexo, salario, idade))