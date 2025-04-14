musicas_por_ano = {}

with open('meu_projeto_spotify/spotify-2023.csv', 'r', encoding='latin-1') as arquivo:

    next(arquivo)  # pula o cabeçalho
    for linha in arquivo:
        # Ignorar linhas com aspas (muito complexas para esse exercício)
        if '"' in linha:
            continue

        colunas = linha.strip().split(',')

        try:
            track_name = colunas[0]
            artist_name = colunas[1]
            artist_count = int(colunas[2])
            released_year = int(colunas[3])
            streams = int(colunas[8])
        except (IndexError, ValueError):
            continue  # pula se houver erro de conversão ou campos faltando

        # Considera apenas músicas de 2012 a 2022
        if 2012 <= released_year <= 2022:
            atual = musicas_por_ano.get(released_year)
            if atual is None or streams > atual[3]:
                musicas_por_ano[released_year] = [track_name, artist_name, released_year, streams]

# Criar a lista final
resultado = []
for ano in sorted(musicas_por_ano):
    resultado.append(musicas_por_ano[ano])

# Imprimir o resultado
print("\nMúsicas mais populares de 2012 a 2022:\n")
for musica in resultado:
    print(musica)
