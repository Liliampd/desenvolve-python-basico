'''Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) e escreva uma expressão que imprima True se a pessoa já pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:

A: Para mulheres, ter mais de 60 anos. Para homens, 65.

B: Ou ter trabalhado pelo menos 30 anos

C: Ou ter 60 anos  e trabalhado pelo menos 25.'''



# Solicitar informações do usuário
genero = input("Informe seu gênero (M ou F): ")
idade = int(input("Informe sua idade: "))
tempo_servico = int(input("Informe seu tempo de serviço (em anos): "))

# Verificar se a pessoa pode se aposentar
pode_se_aposentar = (
    (genero == "F" and idade > 60) or
    (genero == "M" and idade > 65) or
    (tempo_servico >= 30) or
    (idade >= 60 and tempo_servico >= 25)
)

# Imprimir o resultado
if pode_se_aposentar:
    print("Você pode se aposentar")
else:
    print("Você não pode se aposentar")