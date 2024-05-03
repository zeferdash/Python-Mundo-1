distancia = float(input("Qual é a distancia da sua viagem? "))
print(f"Voce está prestes a fazer uma viagem de {distancia}Km")
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f"E o preco da sua passagem será de R${preco:.2f}")