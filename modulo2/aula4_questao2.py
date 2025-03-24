'''Leia um valor inteiro correspondente a uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. 
Fórmula de conversão: C = (F - 32) * (5/9), sendo C o valor em graus Celsius e F o valor em Fahrenheit. Antes de imprimir, converta o valor em Celsius para inteiro. A mensagem deve estar formatada da seguinte maneira:
86 graus Fahrenheit são 30 graus Celsius.'''

# Solicita ao usuário o valor da temperatura para a conversão.
fahrenheit = int(input("Digite o valor da temperatura em Fahrenheit:"))

# Calcula os valores para a realizar a conversão.
celsius = int((fahrenheit - 32) * (5/9))

# Exibe o resultado na tela.
print(f"{fahrenheit} graus Fahrenheith são {celsius} graus Celsius. ")