#  078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o
#  menor valor digitado e as suas respectivas posições na lista.
lista_numeros = []
mai = 0
men = 0
for c in range(0,5):
    lista_numeros.append(int(input(f'Digite um valor para a posição {c}:')))
    if c == 0:
        mai = men = lista_numeros[c]
    else:
        if lista_numeros[c] > mai:
            mai = lista_numeros[c]
        if lista_numeros[c] < men:
            men = lista_numeros[c]
print(f'Você informou os valores {lista_numeros}.')
print(f'O maior valor digitado foi {mai}, nas posições: ', end='')
for i, v in enumerate(lista_numeros):
    if v == mai:
        print(f'{i}..', end='')
print()
print(f'O menor valor digitado foi {men}, nas posições: ', end='')
for i, v in enumerate(lista_numeros):
    if v == men:
        print(f'{i}..', end='')
print()
