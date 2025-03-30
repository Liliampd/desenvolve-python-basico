import random
import math

n = int(input("Digite a quantidade de números aleatórios: "))
valores = [random.randint(0, 100) for _ in range(n)]
soma = sum(valores)
raiz_quadrada = math.sqrt(soma)

print(f"Os valores gerados foram: {valores}")
print(f"A raiz quadrada da soma dos valores é: {raiz_quadrada}")
