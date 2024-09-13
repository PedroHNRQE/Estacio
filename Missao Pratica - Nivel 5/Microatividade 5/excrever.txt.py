arquivo = open('texto.txt', 'w')

texto = list()

texto.append("1° linha do arquivo.")
texto.append("2° linha do arquivo.")
texto.append("3° linha do arquivo.")

for linha in texto:
    arquivo.write(linha)

