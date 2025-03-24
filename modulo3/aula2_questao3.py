'''Você está desenvolvendo um sistema de admissão para um clube juvenil de jogos de tabuleiro. Escreva um programa em Python que pergunte ao usuário sua idade, se já jogou pelo menos 3 jogos de tabuleiro (resposta deve ser True ou False) e quantas vezes venceu um jogo. O programa deve imprimir True se o participante tiver entre 16 e 18 anos, já tiver jogado pelo menos 3 jogos e já ter vencido pelo menos 1 jogo, permitindo seu ingresso no clube. Sua expressão deve imprimir False caso contrário. Aqui está um exemplo de interação com seu código no terminal, com entradas de dados destacadas em laranja e as impressões de seu código em branco.'''

# Solicita a idade do participante
idade = int(input("Qual sua idade? "))

# Solicita se já jogou pelo menos 3 jogos de tabuleiro (responda True ou False)
jogou = input("Você já jogou pelo menos 3 jogos de tabuleiro? (True/False) ")

# Converte a resposta para booleano
if jogou == "True":
    jogou = True
else:
    jogou = False

# Solicita quantas vezes venceu um jogo
vitorias = int(input("Quantas vezes você venceu um jogo? "))

# Verifica se o participante atende a todos os critérios
resultado = (16 <= idade <= 18) and jogou and (vitorias >= 1)

# Imprime o resultado
print(resultado)
