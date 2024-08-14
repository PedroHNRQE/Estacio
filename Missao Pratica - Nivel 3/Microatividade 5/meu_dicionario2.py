meu_dicionario = {1: {'nome': 'Maria', 'idade': 26, 'nacionalidade': 'brasileira'}}

meu_dicionario.update({2: {'nome': 'João', 'idade': 30, 'nacionalidade': 'português'},3: {'nome': 'Ana', 'idade': 22, 'nacionalidade': 'espanhola'}})
print(meu_dicionario)

dicionario_copia = meu_dicionario.copy()
meu_dicionario.pop(1)
print(meu_dicionario)

meu_dicionario.popitem()
print(meu_dicionario)

meu_dicionario.clear()
dicionario_copia.clear()

chaves = [10, 20, 30]
novo_dicionario = dict.fromkeys(chaves, 'valor padrão')
print(novo_dicionario.items())
print(novo_dicionario.keys())
print(novo_dicionario.values())