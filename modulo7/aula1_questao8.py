'''Desenvolva um validador de CPF. Solicite do usuário um CPF na forma XXX.XXX.XXX-XX (lido como string) e imprima "Válido" ou "Inválido". 

O primeiro passo é calcular o primeiro dígito verificador. Separamos os primeiros 9 dígitos do CPF (ex: 111.444.777) e multiplicamos cada um dos números, da direita para a esquerda por números crescentes a partir do número 2, como no exemplo abaixo:'''

import re

def calcular_digito(cpf_parcial, multiplicadores):
    soma = sum(int(cpf_parcial[i]) * multiplicadores[i] for i in range(len(cpf_parcial)))
    resto = soma % 11
    return '0' if resto < 2 else str(11 - resto)

def validar_cpf(cpf):
    # Remover caracteres não numéricos
    cpf_numerico = re.sub(r'\D', '', cpf)
    
    # Verificar se o CPF tem 11 dígitos
    if len(cpf_numerico) != 11:
        return "Inválido"
    
    # Obter os 9 primeiros dígitos e os dois dígitos verificadores informados
    cpf_base = cpf_numerico[:9]
    digitos_verificadores = cpf_numerico[9:]
    
    # Calcular os dígitos verificadores
    primeiro_digito = calcular_digito(cpf_base, range(10, 1, -1))
    segundo_digito = calcular_digito(cpf_base + primeiro_digito, range(11, 1, -1))
    
    # Comparar com os dígitos fornecidos
    return "Válido" if digitos_verificadores == primeiro_digito + segundo_digito else "Inválido"

# Entrada do usuário
cpf_usuario = input("Digite um CPF (XXX.XXX.XXX-XX): ")
print(validar_cpf(cpf_usuario))