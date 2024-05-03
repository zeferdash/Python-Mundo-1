salario = float(input("Digite o valor do seu salário atual: "))
if salario <= 1250:
    novoSalario = salario + (salario * 0.15)
else:
    novoSalario = salario + (salario * 0.10)
print(f"Quem ganhava R${salario:.2f} passa a ganhar R${novoSalario:.2f}")
