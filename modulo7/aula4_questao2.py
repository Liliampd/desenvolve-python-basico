'''Escreva um script que leia o arquivo salvo no exercício anterior e salva em um novo arquivo "palavras.txt", removendo todos os espaços em branco e caracteres não alfabéticos, e separando cada palavra em uma linha. Ao final, imprima o conteúdo do arquivo "palavras.txt".'''

import re

# Nome dos arquivos
arquivo_entrada = "frase.txt"
arquivo_saida = "palavras.txt"

# Lê o conteúdo do arquivo frase.txt
with open(arquivo_entrada, "r", encoding="utf-8") as f:
    conteudo = f.read()

# Usa expressão regular para encontrar apenas palavras com letras (ignorando números e símbolos)
palavras = re.findall(r'\b[a-zA-ZáéíóúâêîôûãõçÁÉÍÓÚÂÊÎÔÛÃÕÇ]+\b', conteudo)

# Salva cada palavra em uma linha no arquivo palavras.txt
with open(arquivo_saida, "w", encoding="utf-8") as f:
    for palavra in palavras:
        f.write(palavra + "\n")

# Lê e imprime o conteúdo do arquivo palavras.txt
with open(arquivo_saida, "r", encoding="utf-8") as f:
    print("Conteúdo do arquivo palavras.txt:\n")
    print(f.read())
