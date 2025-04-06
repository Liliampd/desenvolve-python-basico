'''Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. Crie uma terceira lista interseccao contendo apenas os valores que se repetem nas duas listas. Ao final imprima:
Ambas as listas
A lista intersecção ordenada
A quantidade de vezes que cada elemento aparece em cada lista
Atenção, a lista de intersecções não pode ter duplicatas. '''

import random
from collections import Counter


lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

interseccao = sorted(set(lista1) & set(lista2))

contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista interseccao ordenada:", interseccao)
print("Frequência dos elementos na Lista 1:", dict(contagem_lista1))
print("Frequência dos elementos na Lista 2:", dict(contagem_lista2))


