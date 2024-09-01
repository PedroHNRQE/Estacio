from Pessoa import Pessoa

pessoa = Pessoa("João", "2000-01-01", "000.111.222-33", "15975388-1", False)

attrs = vars(pessoa)
print('Instância inicial da classe Pessoa:')
print(', '.join("%s: %s" % item for item in attrs.items()))

pessoa.nome = "Ana"
pessoa.dataNascimento = "1995-05-20"
pessoa.rg = "SP-12.345.678"
pessoa.status = True

try:
    pessoa.cpf = "123.456.780-00"
except ValueError as e:
    print(e)

attrs = vars(pessoa)
print('Instância final da classe Pessoa:')
print(', '.join("%s: %s" % item for item in attrs.items()))

