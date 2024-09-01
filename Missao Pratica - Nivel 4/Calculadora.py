class Calculadora:
    def __init__(self, valorA, valorB, operacao):
        self.__valorA = valorA
        self.__valorB = valorB
        self.__operacao = operacao

    @property
    def valorA(self):
        return self.__valorA
    @property
    def valorB(self):
        return self.__valorB
    @property
    def operacao(self):
        return self.__operacao

    @valorA.setter
    def valorA(self, valorA):
        self.__valorA = valorA
    @valorB.setter
    def valorB(self, valorB):
        self.__valorB = valorB
    @operacao.setter
    def operacao(self, operacao):
        self.__operacao = operacao

    def validarOperacao(self, simbolo):
        operacoes_validas = ['+', '-', '*', '/']
        return simbolo in operacoes_validas

    def calcular(self):
        if not self.validarOperacao(self.__operacao):
            print("Operação inválida! Programa encerrado.")
            return None

        if self.__operacao == '+':
            return self.__valorA + self.__valorB
        elif self.__operacao == '-':
            return self.__valorA - self.__valorB
        elif self.__operacao == '*':
            return self.__valorA * self.__valorB
        elif self.__operacao == '/':
            if self.__valorB == 0:
                print("Não é possível realizar divisão por zero! Programa encerrado.")
                return None
            else:
                return self.__valorA / self.__valorB

    def mostrarResultado(self):
            resultado = self.calcular()
            if resultado is not None:
                print(str(self.valorA) + ' ' + self.operacao + ' ' + str(self.valorB) + ' = ' + str(resultado))