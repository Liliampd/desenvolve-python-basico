'''Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string. Dica: letra in "aeiou". Exemplo:'''

def contar_vogais(frase):
    vogais = "aeiouAEIOU"
    contador = 0
    indices = []

    for i, letra in enumerate(frase):
        if letra in vogais:
            contador += 1
            indices.append(i)

    print(f"Quantidade de vogais: {contador}")
    print(f"Índices das vogais: {indices}")

# Entrada do usuário
frase = input("Digite uma frase: ")
contar_vogais(frase)
