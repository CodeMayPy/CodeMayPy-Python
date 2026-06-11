numeros = [[], []]
lista = 0

print('Vamos criar uma lista com 7 números e separar os pares dos ímpares.')

for n in range(0,7):
    lista= int(input(f'Digite o {n + 1}º número: da lista: '))
    if lista % 2 == 0:
        numeros[0].append(lista)
    else:
        numeros[1].append(lista)

print(f'Os números pares digitados foram: {sorted(numeros[0])}.')
print(f'Os números ímpares digitados foram: {sorted(numeros[1])}.')
 