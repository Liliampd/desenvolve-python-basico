'''A extensão ".csv" significa "comma-separated values" ou "valores separados por vírgula". É a extensão utilizada por sistemas de gerência de tabelas como o Microsoft Excel ou Google Sheets. Nesse exercício vamos criar uma planilha com dados sobre livros que você já leu ou gostaria de ler. Siga as instruções.

Selecione pelo menos 10 livros que você leu ou gostaria de ler. Você deve reunir as seguintes informações: título, autor, ano de publicação e número de páginas.

No Python, crie um arquivo chamado "meus_livros.csv", aberto para escrita.

Na primeira linha escreva os títulos da planilha separados por vírgula (sem espaço em branco). Os títulos são: "Título", "Autor", "Ano de publicação" e "Número de páginas". Lembre de finalizar a linha com uma quebra de linha.

A partir da segunda linha escreva as informações de cada livro que você levantou, separando cada informação por uma vírgula (sem espaço em branco). Lembre de finalizar cada linha com uma quebra de linha.
Feche o arquivo para salvá-lo e abra com a ferramenta de planilhas de sua escolha. Como você já tem conta no Google, sugiro abrir com o Google Sheets.
Seu arquivo deve ser aberto como uma planilha parecida com essa:
Título
Autor
Ano de publicação
Número de páginas
O Caçador de Pipas
Khaled Hosseini
2003
368
Torto Arado
Itamar Vieira Junior
2019
264'''

# Lista com os dados dos livros (corrigido Harold Robbins)
livros = [
    ["O caçador de pipas", "Khaled Hosseini", 2003, 368],
    ["A hora da estrela", "Clarice Lispector", 1977, 88],
    ["Quem tem medo do escuro", "Sidney Sheldon", 2004, 320],
    ["Antes da meia noite", "Sidney Sheldon", 1973, 352],
    ["O outro lado da meia noite", "Sidney Sheldon", 1973, 560],
    ["A redoma de vidro", "Sylvia Plath", 1963, 234],
    ["A cidade do sol", "Khaled Hosseini", 2007, 384],
    ["O silêncio das montanhas", "Khaled Hosseini", 2013, 336],
    ["O dilema do porco espinho", "Leandro Karnal", 2021, 160],
    ["Atire a primeira pedra", "Harold Robbins", 1953, 240]
]

# Cria o arquivo CSV
with open("meus_livros.csv", "w", encoding="utf-8") as f:
    # Cabeçalho da planilha
    f.write("Título,Autor,Ano de publicação,Número de páginas\n")
    # Dados dos livros
    for livro in livros:
        linha = ",".join([str(item) for item in livro])
        f.write(linha + "\n")

print("Arquivo 'meus_livros.csv' criado com sucesso!")
