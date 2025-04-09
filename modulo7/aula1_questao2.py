'''Escreva um programa que solicite ao usuário inserir seu primeiro nome e sobrenome separadamente. Em seguida, concatene essas duas strings e exiba a mensagem de boas-vindas.'''

# Solicita ao usuário que insira seu primeiro nome e sobrenome
primeiro_nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")

# Concatena as strings com um espaço entre elas
nome_completo = primeiro_nome + " " + sobrenome

# Exibe a mensagem de boas-vindas
print(f"Bem-vindo(a), {nome_completo}!")
