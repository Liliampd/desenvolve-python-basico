import random

n_aleatório = random.randint(0, 10)
print(n_aleatório)


while True:
    palpite = int(input("Digite um número entre 1 e 10: "))
    if palpite < n_aleatório: 
        print("Muito baixo, tente novamente!") 
    elif palpite > n_aleatório:
        print("Muito alto, tente novamente!")
    else:
        print("Parabéns, você acertou!")
        break









       
