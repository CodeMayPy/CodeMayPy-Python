ficha = list()

while True: 
    nome = str(input('Nome: '))
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2

    ficha.append([nome, [nota_1, nota_2], media])
    resposta = str(input('Deseja continuar? [Sim/Não] ')).upper().strip()[0]
    if resposta == 'N':
        break

print('-=' * 20)
print(f'{'No.':<4}{'NOME:':<10}{'MÉDIA':>8}') 
print('--' * 20)   
for i, aluno in enumerate(ficha):
    print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
    print('--' * 25)
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opcao == 999:
        print('Finalizando...')
        break
    if opcao <= len(ficha) -1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')     
