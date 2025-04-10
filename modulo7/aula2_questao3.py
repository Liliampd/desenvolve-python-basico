'''Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo (ou seja, lida da mesma forma de trás para frente). Ignore espaços em branco ou sinais de pontuação, e considere maiúsculas e minúsculas da mesma forma. Seu programa deve continuar rodando até que o usuário digite "Fim".'''

import string

def limpar_texto(texto):
    """Remove espaços, pontuação e converte para minúsculas."""
    return ''.join(caractere.lower() for caractere in texto if caractere.isalnum())

def eh_palindromo(frase):
    """Verifica se a frase é um palíndromo."""
    frase_limpa = limpar_texto(frase)
    return frase_limpa == frase_limpa[::-1]

def main():
    while True:
        entrada = input("Digite uma frase (ou 'Fim' para sair): ")
        if entrada.lower() == "fim":
            print("Encerrando o programa...")
            break
        
        if eh_palindromo(entrada):
            print("É um palíndromo!")
        else:
            print("Não é um palíndromo.")

if __name__ == "__main__":
    main()