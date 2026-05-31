salario1: float
salario2: float

nome1: str
nome2: str

idade1: int
idade2: int

sexo: str

idade1: int
idade2: int



nome1 = input("Nome da primeira pessoa: ")
salario1 = float(input("Salario da primeiro pessoa: "))
idade1 = int(input("Idade da primeira pessoa: "))


nome2 = input("Nome da segunda pessoa: ")
salario2 = float(input("Salario da segunda pessoa: "))
idade2 = int(input("Idade da segunda pessoa: "))


sexo = input("Sexo das duas pessoas: ")

print(f"O nome da primeira pessoa: {nome1}")
print(f"O Sexo da primeira pessoa: {sexo}")
print(f"A idade da primeira pessoa: {idade1}")
print(f"O salario da primeira pessoa: {salario1}")

print(f"O nome da segunda pessoa: {nome1}")
print(f"O sexo das pessoas: {sexo}")
print(f"A idade da segunda pessoa: {idade1}")
print(f"O salario da segunda pessoa: {salario1}")






# nomes = []
idades = []
sexos = []
salarios = []

# REPETE 3 VEZES
for i in range(3):

    print(f"\nPessoa {i + 1}")

    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo: ")
    salario = float(input("Salário: "))

    # GUARDANDO NAS LISTAS
    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)
    salarios.append(salario)

# MOSTRANDO OS DADOS
print("\n--- DADOS CADASTRADOS ---")

for i in range(3):

    print(f"\nPessoa {i + 1}")
    print(f"Nome: {nomes[i]}")
    print(f"Idade: {idades[i]}")
    print(f"Sexo: {sexos[i]}")
    print(f"Salário: R${salarios[i]:.2f}")  ok entao me explique 100% e de forma didatica isso#