'''Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. Dica: usando listas você não precisa fazer um "if" para cada mês.'''

def data_por_extenso(data):
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
             "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    
    try:
        dia, mes, ano = data.split('/')
        mes_extenso = meses[int(mes) - 1]  # Obtém o nome do mês
        return f"Você nasceu em {dia} de {mes_extenso} de {ano}."
    except (ValueError, IndexError):
        return "Data inválida! Certifique-se de usar o formato dd/mm/aaaa."

# Solicita a data de nascimento do usuário
data_nascimento = input("Digite uma data de nascimento (dd/mm/aaaa): ")
print(data_por_extenso(data_nascimento))
