lista = []

while True:
    numero = int(input('Digite um número: '))
    if numero not in lista:
        lista.append(numero)
        print('Número adicionado com sucesso!')   
    else:
        print('Número duplicado! Não será adicionado.')
    resposta = input('Deseja continuar? [S/N] ').strip().upper()        
    if resposta == 'N':
        break

print(f'Os números digitados foram: {sorted(lista)}')