frase = str(input("Digite uma frase: ")).strip().upper()
print("A letra A aparece {} vezes na frase.".format(frase.count("A")))
print("A letra A aparece a primeira vez na posicao: {}".format(frase.find("A")+1))
print("A letra A aparece a ultima vez na posicao: {}".format(frase.rfind("A")+1))