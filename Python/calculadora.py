###Por ser um codigo muito simples, fiz esse pequeno detalhe para deixa-lo visualmente melhor, ate pensei tentar usar html e css, mas nao acho que é a proposta do desafio.
print("==================================")
print("==== Calculadora ==== Simples ====")
print("==================================")

###Comecei declarando duas variaveis para armazenar os dois numeros, dei o nome mais obvio possivel para facilitar o entendimento do codigo.
primeiroNumero = input("Digite o primeiro número: ")
segundoNumero = input("Digite o segundo número: ")

###Depois, criei mais quatro novas variaveis para cada operação, tive alguns problemas nessa parte por nao ter um dominio bom em python, na questao de declarar o tipo da variavel.
adicao = int(primeiroNumero) + int(segundoNumero)
multi = int(primeiroNumero) * int(segundoNumero)
divi = int(primeiroNumero) / int(segundoNumero)
sub = int(primeiroNumero) - int(segundoNumero)

###Mais uma vez, apenas decorativo
print("==================================")
print("=========== Resultados ===========")
print("==================================")

###Por fim, foi só usar o "print" para mostrar no console o resultado da operação.
print("Resultado da adição: " + str(adicao))
print("Resultado da multiplição: " + str(multi))
print("Resultado da divisão: " + str(divi))
print("Resultado da subtração: " + str(sub))
