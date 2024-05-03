import random

numeroAleatorio = random.randint(0,5)
chute = int(input("Qual número inteiro de 0 a 5 voce acha que o computador pensou? "))
if chute == numeroAleatorio:
    print(f"Parabéns, voce acertou e o número pensado foi: {numeroAleatorio}")
else:
    print(f"Infelizmente voce errou, o numero pensado foi: {numeroAleatorio}")