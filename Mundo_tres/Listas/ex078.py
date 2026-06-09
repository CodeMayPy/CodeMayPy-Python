print('Vamos ver o maior e o menor número de uma lista de 5 números.')

lista = []    

for c in range(0,5):
    numero = int(input(f'Digite o {c+1}º valor inteiro: '))
    lista.append(numero)

print(f'Os valores digitados foram: {lista}')
print(f'O maior valor digitado foi: {max(lista)} e está na {lista.index(max(lista))+1}º posição.')
print(f'O menor valor digitado foi: {min(lista)} e está na {lista.index(min(lista))+1}º posição.')