'''Implemente uma função chamada embaralhar_palavras() que recebe uma frase como entrada e retorna uma nova frase com as letras internas de cada palavra embaralhadas. Mantenha sempre o primeiro e último caractere da palavra no lugar. 
Dica: use a biblioteca random.'''

import random

def embaralhar_palavras(frase):
    def embaralhar_palavra(palavra):
        if len(palavra) > 3:
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            return palavra[0] + ''.join(meio) + palavra[-1]
        return palavra
    
    palavras = frase.split()
    palavras_embaralhadas = [embaralhar_palavra(palavra) for palavra in palavras]
    return ' '.join(palavras_embaralhadas)

# Solicita a frase ao usuário
frase = input("Digite uma frase: ")
print(embaralhar_palavras(frase))
