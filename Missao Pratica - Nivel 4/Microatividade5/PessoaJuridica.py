from Pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, nome, numero_conta, data_abertura_conta, status, data_abertura_empresa, cnpj):
        super().__init__(nome, numero_conta, data_abertura_conta, status)
        self.__data_abertura_empresa = data_abertura_empresa
        self.__cnpj = cnpj

    # Getters
    @property
    def data_abertura_empresa(self):
        return self.__data_abertura_empresa

    @property
    def cnpj(self):
        return self.__cnpj

    # Setters
    @data_abertura_empresa.setter
    def data_abertura_empresa(self, data_abertura_empresa):
        self.__data_abertura_empresa = data_abertura_empresa

    @cnpj.setter
    def cnpj(self, cnpj):
        if len(cnpj) == 18:
            self.__cnpj = cnpj
        else:
            raise ValueError("CNPJ deve ter 18 caracteres.")
