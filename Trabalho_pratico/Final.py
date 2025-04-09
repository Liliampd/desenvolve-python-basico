import csv
import os

# Definição de estruturas de dados
usuarios = []  # Lista para armazenar usuários
produtos = []  # Lista para armazenar produtos

# Arquivos de armazenamento
darq_usuarios = "usuarios.csv"
darq_produtos = "produtos.csv"

# Função para carregar dados de usuários
def carregar_usuarios():
    if os.path.exists(darq_usuarios):
        with open(darq_usuarios, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for linha in reader:
                usuarios.append({"id": linha[0], "nome": linha[1], "senha": linha[2], "permissao": linha[3]})

# Função para salvar usuários
def salvar_usuarios():
    with open(darq_usuarios, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for usuario in usuarios:
            writer.writerow([usuario["id"], usuario["nome"], usuario["senha"], usuario["permissao"]])

# Função para adicionar um novo usuário
def criar_usuario():
    id_usuario = input("ID: ")
    nome = input("Nome: ")
    senha = input("Senha: ")
    permissao = input("Permissão (gerente, funcionário, etc.): ")
    usuarios.append({"id": id_usuario, "nome": nome, "senha": senha, "permissao": permissao})
    salvar_usuarios()
    print("Usuário cadastrado com sucesso!")

# Função para listar usuários
def listar_usuarios():
    for usuario in usuarios:
        print(f"ID: {usuario['id']}, Nome: {usuario['nome']}, Permissão: {usuario['permissao']}")

# Função para atualizar um usuário
def atualizar_usuario():
    id_usuario = input("Digite o ID do usuário a ser atualizado: ")
    for usuario in usuarios:
        if usuario["id"] == id_usuario:
            usuario["nome"] = input("Novo nome: ")
            usuario["senha"] = input("Nova senha: ")
            usuario["permissao"] = input("Nova permissão: ")
            salvar_usuarios()
            print("Usuário atualizado com sucesso!")
            return
    print("Usuário não encontrado!")

# Função para remover um usuário
def remover_usuario():
    id_usuario = input("Digite o ID do usuário a ser removido: ")
    global usuarios
    usuarios = [u for u in usuarios if u["id"] != id_usuario]
    salvar_usuarios()
    print("Usuário removido com sucesso!")

# Funções para CRUD de produtos
def carregar_produtos():
    if os.path.exists(darq_produtos):
        with open(darq_produtos, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for linha in reader:
                produtos.append({"id": linha[0], "nome": linha[1], "preco": float(linha[2]), "quantidade": int(linha[3])})

def salvar_produtos():
    with open(darq_produtos, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for produto in produtos:
            writer.writerow([produto["id"], produto["nome"], produto["preco"], produto["quantidade"]])

def criar_produto():
    id_produto = input("ID: ")
    nome = input("Nome: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))
    produtos.append({"id": id_produto, "nome": nome, "preco": preco, "quantidade": quantidade})
    salvar_produtos()
    print("Produto cadastrado com sucesso!")

def listar_produtos():
    for produto in produtos:
        print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

def buscar_produto():
    nome_busca = input("Digite o nome do produto: ")
    encontrados = [p for p in produtos if nome_busca.lower() in p["nome"].lower()]
    for produto in encontrados:
        print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

def listar_produtos_ordenados_por_nome():
    for produto in sorted(produtos, key=lambda p: p["nome"]):
        print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

def listar_produtos_ordenados_por_preco():
    for produto in sorted(produtos, key=lambda p: p["preco"]):
        print(f"ID: {produto['id']}, Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

def menu():
    carregar_usuarios()
    carregar_produtos()
    while True:
        print("\n1. Criar usuário")
        print("2. Listar usuários")
        print("3. Atualizar usuário")
        print("4. Remover usuário")
        print("5. Criar produto")
        print("6. Listar produtos")
        print("7. Buscar produto")
        print("8. Listar produtos ordenados por nome")
        print("9. Listar produtos ordenados por preço")
        print("10. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            criar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            atualizar_usuario()
        elif opcao == "4":
            remover_usuario()
        elif opcao == "5":
            criar_produto()
        elif opcao == "6":
            listar_produtos()
        elif opcao == "7":
            buscar_produto()
        elif opcao == "8":
            listar_produtos_ordenados_por_nome()
        elif opcao == "9":
            listar_produtos_ordenados_por_preco()
        elif opcao == "10":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
