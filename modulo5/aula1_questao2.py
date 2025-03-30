import random
import math
soma = 0
n = int(input("Digite a quantidade de números que deseja gerar:"))

for i in range(n):
     valor_aleatório = random.randint(0,100)#gera os valores aleatórios e guarda na variável valor_aleatório
     print(valor_aleatório)
     soma += valor_aleatório #Soma cada cada valor de cada iteração

print(f"A soma dos números gerados aleatóriamente é: {soma}")
print(f"A raiz quadrada da soma destes números é: {math.sqrt(soma)}")