'''Baixe o arquivo contendo o roteiro do filme brasileiro "Estômago" e salve em seu computador com o nome "estomago.txt". Em seguida crie um script em Python que abra o arquivo para leitura e imprima: 
O texto das primeiras 25 linhas
O número de linhas do arquivo
A linha com maior número de caracteres
O número de menções aos nomes dos personagens "Nonato" e "Íria" (inclua todas as variações de maiúsculas e minúsculas e atenção para não incluir a substring "iria" se ela fizer parte de outras palavras).'''

import re

# Nome do arquivo
arquivo = "estomago.txt"

# Abrir o arquivo para leitura
with open(arquivo, "r", encoding="utf-8") as f:
    linhas = f.readlines()

# 1. Mostrar as primeiras 25 linhas
print("== Primeiras 25 linhas do roteiro ==\n")
for linha in linhas[:25]:
    print(linha.strip())

# 2. Número total de linhas
num_linhas = len(linhas)
print(f"\n== Número total de linhas: {num_linhas} ==")

# 3. Linha com o maior número de caracteres
linha_maior = max(linhas, key=len)
print("\n== Linha com maior número de caracteres ==\n")
print(linha_maior.strip())

# 4. Contar menções a "Nonato" e "Íria" (com variações de maiúsculas/minúsculas)
conteudo = ''.join(linhas)

# Encontrar "Nonato" (case insensitive)
menções_nonato = re.findall(r'\bnonato\b', conteudo, flags=re.IGNORECASE)
# Encontrar "Íria" (case insensitive, e evitar a palavra "iria")
menções_iria = re.findall(r'\bíria\b', conteudo, flags=re.IGNORECASE)

print(f"\n== Menções aos personagens ==")
print(f"Nonato: {len(menções_nonato)} menções")
print(f"Íria: {len(menções_iria)} menções")
