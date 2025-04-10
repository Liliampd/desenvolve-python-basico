'''Implemente uma função em Python chamada validador_senha() que verifica se uma senha fornecida atende todos os seguintes critérios:
Pelo menos 8 caracteres de comprimento.
Contém pelo menos uma letra maiúscula e uma letra minúscula.
Contém pelo menos um número.
Contém pelo menos um caractere especial (por exemplo, @, #, $).'''

import re

def validador_senha(senha: str) -> bool:
    """
    Verifica se a senha atende aos seguintes critérios:
    - Pelo menos 8 caracteres de comprimento.
    - Pelo menos uma letra maiúscula.
    - Pelo menos uma letra minúscula.
    - Pelo menos um número.
    - Pelo menos um caractere especial (@, #, $, etc.).
    
    Retorna True se a senha for válida, caso contrário, False.
    """
    if len(senha) < 8:
        return False
    if not re.search(r"[A-Z]", senha):
        return False
    if not re.search(r"[a-z]", senha):
        return False
    if not re.search(r"\d", senha):
        return False
    if not re.search(r"[@#$%^&*!()_+=\-{}\[\]:;'<>,.?/]", senha):
        return False
    
    return True

# Exemplo de uso
senhas = [
    "Senha123!",    # Válida
    "senha123",     # Falta maiúscula e especial
    "SENHA123",     # Falta minúscula e especial
    "Senha@",       # Falta número e tamanho mínimo
    "Senha123"      # Falta caractere especial
]

for s in senhas:
    print(f"'{s}': {validador_senha(s)}")
