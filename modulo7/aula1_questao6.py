'''Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são palavras com os mesmos caracteres rearranjados.'''

def encontrar_anagramas(texto, palavra):
    tamanho = len(palavra)
    anagramas = []
    palavra_ordenada = sorted(palavra)  # Ordenamos a palavra objetivo

    for i in range(len(texto) - tamanho + 1):
        if sorted(texto[i:i+tamanho]) == palavra_ordenada:  # Comparação direta das substrings ordenadas
            anagramas.append(i)
    
    return anagramas

# Exemplo de uso:
texto = "cbaebabacd"
palavra = "abc"
print(encontrar_anagramas(texto, palavra))  # Saída: [0, 6]
