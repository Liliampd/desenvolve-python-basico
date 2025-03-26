n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

m = (n1 + n2 + n3) /3

if m >= 60:
    print(f"Nota = {m:.2f} Aprovado")
elif m >= 40:
     print(f"Nota = {m:.2f} Recuperação")

else:
      print(f"Nota = {m:.2f} Reprovado")
print("Fim")