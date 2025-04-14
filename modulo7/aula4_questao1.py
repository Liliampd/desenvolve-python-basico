'''Escreva um script Python que solicita uma frase do usuário e a salve em um arquivo chamado "frase.txt" no mesmo local do seu script. Imprima em seguida o caminho completo do arquivo salvo.'''

import os

# Solicita uma frase do usuário
frase = input("Digite uma frase: ")

# Define o nome do arquivo
nome_arquivo = "frase.txt"

# Salva a frase no arquivo
with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
    arquivo.write(frase)

# Obtém o caminho completo do arquivo salvo
caminho_completo = os.path.abspath(nome_arquivo)

# Imprime o caminho completo
print(f"O arquivo foi salvo em: {caminho_completo}")
