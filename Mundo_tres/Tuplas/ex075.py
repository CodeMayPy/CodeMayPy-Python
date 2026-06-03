lista = []

for c in range(4):
    numeros = int(input(f'Digite o {c+1}º número: '))
    lista.append(numeros)

numeros_tupla = tuple(lista)

print(f'Sua tupla ficou assim: {numeros_tupla}.')
print(f'O número 9 apareceu {numeros_tupla.count(9)} vezes.')

if 3 in numeros_tupla:
    print(f'O número 3 apareceu primeiro na posição {numeros_tupla.index(3)+1}º informada.')
else:
    print('O número 3 não foi digitado em nenhuma posição.')

lista_par = []

for par in numeros_tupla:
    if par % 2 == 0:
        lista_par.append(par)

if lista_par:
    print(f'Os números pares digitados foram: {tuple(lista_par)}.')
else:
    print('Nenhum número par foi digitado.')