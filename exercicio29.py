import random
velocidadeCarro = random.randint(1,210)
if velocidadeCarro > 80:
    multa = 7.00 * (velocidadeCarro - 80)
    print(f"Voce acaba de ser multado por ter ultrapassado o limite de velocidade permitido. Valor da multa: {multa} Velocidade registrada: {velocidadeCarro}")