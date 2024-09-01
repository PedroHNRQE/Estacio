from Pessoa import Pessoa

pessoa = Pessoa("João", "2000-01-01", "000.111.222-33", "15975388-1")

attrs = vars(pessoa)

print('Instância da classe Pessoa:')
print(', '.join("%s: %s" % item for item in attrs.items()))
