arquivo = open('loremipsum.txt', 'r')

conteudo = arquivo.read()
print(conteudo)

arquivo.seek(0)

primeira_linha = arquivo.readline()
print(primeira_linha)

arquivo.seek(0)

primeiros_tres_caracteres = arquivo.read(3)
print(primeiros_tres_caracteres)

arquivo.close()

with open('loremipsum.txt', 'r') as arquivo_com_with:
    conteudo_with = arquivo_com_with.read()
    print(conteudo_with)

