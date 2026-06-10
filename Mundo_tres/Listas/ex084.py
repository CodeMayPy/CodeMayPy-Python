pessoas = []
lista = []
maior_peso = menor_peso = 0

while True:
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior_peso = menor_peso = lista[1]
    else:
        if lista[1] > maior_peso:
            maior_peso = lista[1]
        if lista[1] < menor_peso:
            menor_peso = lista[1]
    pessoas.append(lista[:])
    lista.clear()
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resposta == 'N':
        break
print('-='*30)

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')   


print(f'O maior peso foi de {maior_peso:.2f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}] ', end='')

print(f'\nO menor peso foi de {menor_peso:.2f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}] ', end='')