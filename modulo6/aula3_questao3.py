'''Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del. Você deve imprimir a lista antes e depois da deleção.'''

import random

# Gerar lista com 20 valores inteiros aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]
print("Lista original:", lista)

# Encontrar o intervalo com mais números negativos
max_negativos = 0
melhor_inicio = 0

for i in range(len(lista)):
    for j in range(i + 1, len(lista) + 1):
        sublista = lista[i:j]
        negativos = sum(1 for num in sublista if num < 0)
        if negativos > max_negativos:
            max_negativos = negativos
            melhor_inicio, melhor_fim = i, j

# Deletar o intervalo encontrado
del lista[melhor_inicio:melhor_fim]

# Exibir a lista após a deleção
print("Lista após deleção:", lista)
