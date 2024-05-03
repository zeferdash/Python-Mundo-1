n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
media = (n1 + n2) // 2
if media >= 6:
    print(f"Sua média foi {media} e voce foi aprovado!")
else:
    print(f"Sua média foi {media} e infelizmente voce nao foi aprovado =/")