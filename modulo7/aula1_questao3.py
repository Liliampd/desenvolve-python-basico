'''Escreva um script que dado uma frase conta os espaços em branco.'''
def contar_espacos(frase):
    return frase.count(" ")

# Solicita uma frase ao usuário
frase = input("Digite uma frase: ")

# Conta os espaços em branco
quantidade_espacos = contar_espacos(frase)

# Exibe o resultado
print(f"A frase contém {quantidade_espacos} espaços em branco.")
