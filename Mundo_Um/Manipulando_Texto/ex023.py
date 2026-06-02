#Separating digits from a number
#23- Write a program that reads a number from 0 to 9999 and displays each of the separate digits on the screen.
number = int(input('Informe um número:'))
unit = number // 1 % 10
ten = number // 10 % 10
hundred = number // 100 % 10
thousand = number // 1000 % 10
print(f'Analyzing your number: {number}.')
print(f'Your unit is {unit}.')
print(f'Your ten is {ten}.')
print(f'Your hundred is {hundred}.')
print(f'Your thousand is {thousand}.')


#Separando dígitos de um número
# 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''numero = int(input('Digite um número qualquer:'))
print(f'Analizando o numero {numero}....')
print(f'Sua unidade é {numero // 1 % 10}, '
      f'sua dezena é {numero // 10 % 10},'
      f'sua centena é {numero // 100 % 10},'
      f'e seu milhar é {numero // 1000 % 10}')'''

#PT- treinando a manipulação de strings.
#EN- training string manipulation.
