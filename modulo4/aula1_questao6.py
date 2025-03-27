n = int(input("Digite a quantidade de experimentos registrados: "))
cont = 0
soma_sapo, soma_rato, soma_coelho = 0,0,0


while cont < n:
    quantia = int(input("Digite a quantidade de cobaias utlizadas: "))
    tipo = input(("Digite o tipo s, r ou c: "))

    if tipo == 's':
        soma_sapo += quantia
    elif tipo == 'r':
        soma_rato += quantia
    elif tipo == 'c':
        soma_coelho += quantia
    else:
        print("tipo {tipo}não reconhecido!")

    cont += 1

print("Total de cobaias: ", soma_sapo + soma_rato + soma_coelho)
print("Total de sapos: ", soma_sapo)
print("Total de ratos:", soma_rato)
print("Total de coelhos: ",soma_coelho)