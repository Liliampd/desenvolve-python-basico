'''Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado da região em ponto flutuante. Calcule o valor do terreno e imprima o resultado como mostra o exemplo a seguir:'''

# Pergunta ao usuário as dimensões do terreno.
comprimento = int(input("Digite o comprimento do terreno em metros:"))
largura = int(input("Digite a largura do terreno em metros:"))

# Pergunta ao usuário o preço do metro quadrado.
preço_m2 = float(input("Digite o preço do metro quadrado em R$:"))

# Calcula a area e o preço total
area = comprimento * largura
preço_total = preço_m2 * area

# Exibe o resultado
print(f" O terreno possui {area} m2 e custa R$ {preço_total:.2f} reais,")