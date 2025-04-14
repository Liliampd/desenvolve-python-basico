'''Vamos fazer o jogo da forca! Antes de programar: 
Crie um arquivo no seu computador chamado "gabarito_forca.txt" com uma lista de 10 palavras de sua escolha (separadas por quebras de linha, "\n"). Essas serão as opções de palavra do jogo.
Crie um arquivo chamado "gabarito_enforcado.txt" com o conteúdo apresentado ao final dessa questão.
Escreva um programa em Python para executar o jogo, de acordo com as definições:
Abra o arquivo "gabarito_forca.txt" e escolha aleatoriamente uma palavra;
Com o arquivo "gabarito_enforcado.txt", crie uma lista de strings com os estágios do enforcado;
No início exiba o número de letras na palavra como underscores;
Permita que o jogador insira letras para adivinhar a palavra;
Em caso de acerto, mostre o progresso do jogador substituindo os underscores correspondentes à letra digitada;
Em caso de erro, crie a função "imprime_enforcado()" que recebe um inteiro indicando o número de erros do jogador e imprime o enforcado correspondente;
Limite o número de tentativas para 6 (as partes do enforcado).'''

import random

# Função para carregar as palavras do arquivo
def carregar_palavras():
    with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
        palavras = [linha.strip().lower() for linha in f if linha.strip()]
    return palavras

# Função para carregar os estágios do enforcado
def carregar_enforcado():
    with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()
        estagios = conteudo.strip().split("\n\n")
    return estagios

# Função para imprimir o enforcado baseado no número de erros
def imprime_enforcado(erros, estagios):
    print(estagios[erros])

# Função principal do jogo
def jogar_forca():
    palavras = carregar_palavras()
    estagios = carregar_enforcado()

    palavra_secreta = random.choice(palavras)
    letras_descobertas = ["_" for _ in palavra_secreta]
    letras_erradas = []
    tentativas = 6
    erros = 0

    print("=== JOGO DA FORCA ===")
    print("Palavra: ", " ".join(letras_descobertas))

    while erros < tentativas and "_" in letras_descobertas:
        chute = input("\nDigite uma letra: ").lower().strip()

        if len(chute) != 1 or not chute.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue

        if chute in letras_descobertas or chute in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        if chute in palavra_secreta:
            for i, letra in enumerate(palavra_secreta):
                if letra == chute:
                    letras_descobertas[i] = chute
            print("\nBoa! A letra está na palavra.")
        else:
            erros += 1
            letras_erradas.append(chute)
            print("\nLetra errada!")
            imprime_enforcado(erros, estagios)

        print("\nPalavra: ", " ".join(letras_descobertas))
        print("Letras erradas: ", ", ".join(letras_erradas))

    # Verifica o resultado final
    if "_" not in letras_descobertas:
        print("\n🎉 Parabéns! Você adivinhou a palavra:", palavra_secreta)
    else:
        print("\n💀 Você perdeu! A palavra era:", palavra_secreta)

# Executa o jogo
jogar_forca()
