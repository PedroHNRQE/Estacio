class Pessoa:
    def __init__(self, nome, dataNascimento, cpf, rg, status=False):
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.cpf = cpf
        self.rg = rg
        self.status = status

    def alterarStatus(self, status):
        self.status = status

        