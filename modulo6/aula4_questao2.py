'''Solicite uma frase do usuário e usando compreensão de listas imprima:
A lista de vogais da frase, ordenada alfabeticamente
A lista de consoantes da frase (remova espaços em branco)'''

frase = input("Digite uma frase:")

vogais = sorted([c for c in frase if c.lower() in "aeiou"])
consoantes = [c for c in frase if c.lower() in "bcdfghjklmnpqrstvwxyz"]

print ("A lista de vogais em ordem alfabética é: ", vogais)
print("A lista de consoantes é: ", consoantes)