print("Analisador de Triangulos")
r1 = float(input("Digite a primeira reta: "))
r2 = float(input("Digite a segunda reta: "))
r3 = float(input("Digite a terceira reta: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("As retas digitadas podem formar um triangulo!")
else:
    print("As retas digitadas não podem formar um triangulo!")