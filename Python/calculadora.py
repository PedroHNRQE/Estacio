print("==================================")
print("==== Calculadora ==== Simples ====")
print("==================================")

primeiroNumero = input("Digite o primeiro número: ")
segundoNumero = input("Digite o segundo número: ")

adicao = int(primeiroNumero) + int(segundoNumero)
multi = int(primeiroNumero) * int(segundoNumero)
divi = int(primeiroNumero) / int(segundoNumero)
sub = int(primeiroNumero) - int(segundoNumero)

print("==================================")
print("=========== Resultados ===========")
print("==================================")

print("Resultado da adição: " + str(adicao))
print("Resultado da multiplição: " + str(multi))
print("Resultado da divisão: " + str(divi))
print("Resultado da subtração: " + str(sub))