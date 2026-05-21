''' 
#Versão antiga.
#36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do
# comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Qual o valor da casa que deseja comprar?'))
salario = float(input('Qual o seu salário?'))
tempo = float(input('Em quanto tempo você deseja pagar a casa?'))
parcela = casa / (tempo * 12)
condicao = salario * 0.30
if parcela <= condicao:
    print('Empréstimo liberado.')
else:
    print('Tente adicionar mais uma renda')
'''

#versão revisada
casa = float(input('Digite o valor da casa que deseja comprar R$: '))
salario = float(input('Digite o valor do seu salário mensal: '))
tempo = int(input('Em quantos anos você deseja pagar? '))

meses = tempo * 12
parcela = casa / meses
limite = salario * 0.30

if parcela <= salario * 0.30:
    print(f'Seu empréstimo foi aprovado, e a parcela é de {parcela:.2f}')
else:
    print('Empréstimo negado, adicione mais renda.')
