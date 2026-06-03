casa = float(input('Digite o valor da casa que deseja comprar R$: '))
salario = float(input('Digite o valor do seu salário mensal: '))
tempo = int(input('Em quantos anos você deseja pagar? '))

meses = tempo * 12
parcela = casa / meses
limite = salario * 0.30

if parcela <= limite:
    print(f'Seu empréstimo foi aprovado, e a parcela é de {parcela:.2f}')
else:
    print('Empréstimo negado, adicione mais renda.')
