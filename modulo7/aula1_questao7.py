'''Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave da criptografia. Regras:

Chave de criptografia: gere um valor n aleatório entre 1 e 10

Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de caracteres visíveis (entre 33 e 126 na tabela Unicode)'''

import random

def encrypt(names):
    n = random.randint(1, 10)  # Gera um valor aleatório entre 1 e 10
    encrypted_names = []
    
    for name in names:
        encrypted_name = "".join(chr(ord(c) + n) for c in name)
        encrypted_names.append(encrypted_name)
    
    return encrypted_names, n

# Exemplo de uso
names_list = ["Alice", "Bob", "Charlie"]
encrypted_list, key = encrypt(names_list)
print("Nomes criptografados:", encrypted_list)
print("Chave de criptografia:", key)
