# Lê a quantidade de experimentos registrados
N = int(input("Digite a quantidade de experimentos registrados: "))

# Inicializa os contadores
total_cobaias = 0
total_sapos = 0
total_ratos = 0
total_coelhos = 0

# Processa os experimentos
for _ in range(N):
    entrada = input("Digite a quantidade e o tipo de cobaia (Ex: 10 C): ").split()
    quantia = int(entrada[0])
    tipo = entrada[1].upper()

    total_cobaias += quantia  # Soma ao total geral

    if tipo == 'S':  # Sapo
        total_sapos += quantia
    elif tipo == 'R':  # Rato
        total_ratos += quantia
    elif tipo == 'C':  # Coelho
        total_coelhos += quantia

# Calcula os percentuais
percent_sapos = (total_sapos / total_cobaias) * 100 if total_cobaias > 0 else 0
percent_ratos = (total_ratos / total_cobaias) * 100 if total_cobaias > 0 else 0
percent_coelhos = (total_coelhos / total_cobaias) * 100 if total_cobaias > 0 else 0

# Exibe os resultados
print(f"\nTotal de cobaias: {total_cobaias}")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {percent_coelhos:.2f} %")
print(f"Percentual de ratos: {percent_ratos:.2f} %")
print(f"Percentual de sapos: {percent_sapos:.2f} %")
