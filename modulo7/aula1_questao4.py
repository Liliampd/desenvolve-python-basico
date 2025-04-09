'''Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente. Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. Adicione o separador "-" na sua impressão.'''

def formatar_numero(numero):
    # Removendo espaços extras e verificando se é um número
    numero = numero.strip()
    
    # Se o número tiver apenas 8 dígitos, adiciona o 9 na frente
    if len(numero) == 8:
        numero = '9' + numero
    
    # Se o número já tiver 9 dígitos, verifica se o primeiro é 9
    elif len(numero) == 9 and numero[0] != '9':
        print("O número não começa com 9, verifique os dados informados.")
        return
    
    # Adicionando separador
    numero_formatado = numero[:5] + '-' + numero[5:]
    print("Número formatado:", numero_formatado)

# Entrada do usuário
numero_input = input("Digite o número de celular (somente os dígitos): ")
formatar_numero(numero_input)