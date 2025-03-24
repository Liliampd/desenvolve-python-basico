'''Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. O preço dos produtos é calculado multiplicando a quantidade pelo preço unitário. Escreva um programa em Python que solicite do usuário o nome, o preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra. Note no exemplo a seguir que:
Cada entrada de dados tem uma mensagem indicando o dado solicitado (mensagens em itálico, dado de entrada em negrito)
A saída deve estar formatada exatamente como indicado (a string "Total: R$" e o preço com um separador de milhar e duas casas decimais).
'''

# Solicta o nome do produto, preço e quantidade.

nome_1 = input( "Digite o nome do produto 1: ")
preço_1 = float(input("Digite o preço do produto 1: "))
qntd_1 = int(input("Digite a quantidade do produto 1: "))

nome_2 = input( "Digite o nome do produto 2: ")
preço_2 = float(input("Digite o preço do produto 2: "))
qntd_2 = int(input("Digite a quantidade do produto 2: "))

nome_3 = input( "Digite o nome do produto 3: ")
preço_3 = float(input("Digite o preço do produto 3: "))
qntd_3 = int(input("Digite a quantidade do produto 3: "))

# Calcula o valor total

valor_total= (preço_1*qntd_1) + (preço_2*qntd_2) + (preço_3*qntd_3)

# Exibição do resultado na tela

print(f"Total R$ {valor_total:,.2f}")