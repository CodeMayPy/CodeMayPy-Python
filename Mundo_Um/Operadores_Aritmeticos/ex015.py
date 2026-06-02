#Car Rental.
#15- Write a program that asks the number of km traveled by a rented car and the number of days for which
# it was rented. Calculate the price to pay, knowing that the car costs R$60 per day and R$0.15 per km driven.
'''km = int(input(' Enter how many Km you have driven the car:'))
day = int(input('How many days did you keep the car:'))
value_day = day * 60
value_km = km * 0.15
print('If you stayed {} days with the carand it ran {}Km with him, then you must pay R${}.'.format(day, km, (value_day +value_km)))'''


# Aluguel de Carros.
#15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Quantos Km você rodou com o carro?'))
dias = int(input('Quandos dias você ficou com o carro alugado?'))
valor_km = km * 0.15
valor_dia = dias * 60
print(f'Se você rodou {km}km e ficou {dias} dias com o carro, logo você deverá pagar R${valor_dia + valor_km} de locação do carro.')

#PT- mais um treino de operadores aritméticos.
#EN- another training in arithmetic operators