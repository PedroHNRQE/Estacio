import time

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

with open('kdd.txt', 'r') as arquivo:
    palavras = []
    for linha in arquivo:
        palavras.extend(linha.split())

palavras_bubble = palavras.copy()
start_time = time.time()
bubble_sort(palavras_bubble)
end_time = time.time()
print("Bubble Sort:")
print(palavras_bubble)
print(f"Tempo de execução: {end_time - start_time:.6f} segundos")

palavras_selection = palavras.copy()
start_time = time.time()
selection_sort(palavras_selection)
end_time = time.time()
print("\nSelection Sort:")
print(palavras_selection)
print(f"Tempo de execução: {end_time - start_time:.6f} segundos")

palavras_sort = palavras.copy()
start_time = time.time()
palavras_sort.sort()
end_time = time.time()
print("\nMétodo sort:")
print(palavras_sort)
print(f"Tempo de execução: {end_time - start_time:.6f} segundos")

with open('palavras_ordenadas.txt', 'w') as arquivo_saida:
    for palavra in palavras_sort:
        arquivo_saida.write(palavra + '\n')
