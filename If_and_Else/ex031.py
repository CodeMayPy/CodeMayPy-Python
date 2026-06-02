#Travel Cost
#31- Develop a program that asks the distance of a trip in km. Calculate the ticket price, charging R$0.50 per
#  km for trips up to 200km and R$0.45 for longer trips.
distance = float(input('What is the distance of your travel?'))
print(f'You wil stard a travel of {distance}km.')
if distance <= 200:
    price = distance * 0.50
else:
    price = distance * 0.45
print(f'And the price of your ticket will be R${price}.')

#Custo da Viagem
# 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
distancia = float(input('Qual a distância em Km que você vai viajar?'))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print(f'O preço da passagem será de R${preco:.2f}.')

#PT- Exercícios com uso de condicional.
#EN- Exercises using conditional.