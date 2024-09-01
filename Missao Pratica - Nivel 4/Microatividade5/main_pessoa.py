from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

pessoa = Pessoa("João", "12345", "01/01/2020", "Ativa")
pessoa.imprimir_dados()

pessoa_fisica = PessoaFisica("Maria", "54321", "02/02/2021", "Ativa", "15/05/1990", "12345678901", "MG1234567")
pessoa_fisica.imprimir_dados()

pessoa_juridica = PessoaJuridica("Empresa X", "67890", "03/03/2022", "Inativa", "10/10/2000", "00.000.000/0001-00")
pessoa_juridica.imprimir_dados()

pessoa.nome = "Carlos"
pessoa.numero_conta = "67890"
pessoa.data_abertura_conta = "04/04/2023"
pessoa.status = "Inativa"
pessoa.imprimir_dados()

pessoa_fisica.cpf = "10987654321"
pessoa_fisica.imprimir_dados()

pessoa_juridica.cnpj = "11.111.111/0001-11"
pessoa_juridica.imprimir_dados()
