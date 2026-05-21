'''
# Versão antiga
#Comparando números
#38: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais
primeiro = int(input('Digite um número:'))
segundo = int(input('Digite outro número:'))
if primeiro > segundo:
    print(f'O número {primeriro} é maior que {segundo}.')
elif segundo > primeiro:
    print(f'O número {segundo} é maior que {primeiro}.')
else:
    print('Os dois números são iguais.')
'''

# Versão revisada
primeiro_numero = int(input('Digite um número inteiro: '))
segundo_numero = int(input('Digite outro número inteiro: '))
print(f'Vou comparar os números {primeiro_numero} e {segundo_numero} informados...')

if primeiro_numero > segundo_numero:
    print(f'O número {primeiro_numero} é maior que o {segundo_numero}.')
elif primeiro_numero < segundo_numero:
    print(f'O número {segundo_numero} é maior que {primeiro_numero}.')
else:
    print('Não existe número maior ou menor, os dois são iguais.')
