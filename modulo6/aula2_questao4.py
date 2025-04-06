'''Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.
Exemplo de interação via terminal (entradas em laranja): '''

import itertools

# Receber as listas do usuário
lista1 = list(map(int, input("Digite os elementos da primeira lista separados por espaço: ").split()))
lista2 = list(map(int, input("Digite os elementos da segunda lista separados por espaço: ").split()))

# Combinar as listas de forma alternada
lista_intercalada = [item for pair in itertools.zip_longest(lista1, lista2) for item in pair if item is not None]

# Exibir o resultado
print("Lista intercalada:", lista_intercalada)
