lista = []

while True:
    numero = int(input('Digite um valor: '))
    lista.append(numero)
    resposta = str(input('Deseja continuar? [Sim/Não]' )).upper().strip()[0]
    
    if resposta in 'N':
        break   
print(f'Você digitou {len(lista)} números.')

lista.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {lista}.')

if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não está na lista.')