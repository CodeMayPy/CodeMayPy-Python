#Electronic radar
#29- Write a program that reads the speed of a car. If it exceeded 80km/h, show a message saying that it
# was fined. The fine will cost R$7.00 for each km above the limit.
speed = float(input('Enter the speed of your car:'))
if speed > 80:
    print('FINED!!!! You have exceeded the 80Km/h limit.')
    fined = (speed - 80) * 7
    print(f'You will need for a fine of U${fined:.2f}.')
print(f'Have a nice day! Drive safely!')


# Radar eletrônico
#29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que
# ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade = float(input('Qual a velocidade do carro?'))
if velocidade > 80:
    print(f'Você passou {velocidade - 80}Km/h do limite e deverá pagar R${(velocidade - 80)*7:.2f}')


#PT- Exercícios com uso de condicional.
#EN- Exercises using conditional.