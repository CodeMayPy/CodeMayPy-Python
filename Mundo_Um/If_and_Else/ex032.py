#Leap year
#32- Make a program that reads any year and shows whether it is a leap year.
year = int(input('Which year do you want to analize?'))
if year % 4 == 0 and year % 100 !=0 or year % 400 ==0:
    print(f"The year {year} it's a leap year")
else:
    print(f"The year {year} it's not a leap year")

# Ano Bissexto
#32: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
ano = int(input('Digite o ano que você quer que seja analizado:'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')

    
# PT- Exercícios com uso de condicional.
# EN- Exercises using conditional.
