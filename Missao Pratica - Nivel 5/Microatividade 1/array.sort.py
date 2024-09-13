from random import randint

inteiros = [randint(1, 100) for i in range(15)]
inteiros.sort()
print(inteiros)

inteiros.sort(reverse=True, key=None)
print(inteiros)

dados = ["nome", "dataNascimento", "cpf", "rg",]

dados.sort()
print(dados)

dados.sort(reverse=True, key=None)
print(dados)
