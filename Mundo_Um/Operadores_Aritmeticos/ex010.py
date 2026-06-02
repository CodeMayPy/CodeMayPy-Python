#Currency Converter.
#10- Create a program that reads how much money a person has in their wallet and shows how many dollars they can buy.
#  Considering US$1.00 = R$5.45
real = float(input('How much many do you have in R$:'))
dollar = real/5.45
print('So if you have R${} you can buy US${:.2f}.'.format(real, dollar))

#Conversor de Moedas.
#10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considerando
# o dolar U$ 6.29
'''carteira = float(input('Quando dinheiro você tem na sua carteira em R$'))
print(f'Se você possui R${carteira}, logo poderemos converter para U${carteira/6.29:.2f}')'''

#PT- usei o comando ":.2f" para formatar as casas decimais do valor.
#EN- I used the command ":.2f" to format the decimal places of the value.