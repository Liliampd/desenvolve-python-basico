'''Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".'''

def substituir_vogais(frase):
    vogais = "aeiouAEIOU"
    nova_frase = "".join("*" if char in vogais else char for char in frase)
    return nova_frase

# Solicita a entrada do usuário
frase_usuario = input("Digite uma frase: ")
frase_modificada = substituir_vogais(frase_usuario)

# Exibe o resultado
print("Frase modificada:", frase_modificada)
