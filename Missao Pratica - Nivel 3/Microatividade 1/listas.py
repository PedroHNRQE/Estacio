lista_mesclada = [1, 2, 3, 'Olá, Python', True, 12.6]
lista_mesclada.append("Lista aninhada")
print(lista_mesclada)

lista_mesclada.insert(4, 5)
print(lista_mesclada)

print(len(lista_mesclada))

lista_mesclada.pop(4)
print(lista_mesclada)

nova_lista_mesclada = list()
nova_lista_mesclada = lista_mesclada[0:5]
print(nova_lista_mesclada)