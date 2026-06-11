from random import randint

lista = list()
jogos = list()

print('--' * 20)
print('          JOGO DA MEGA SENA')
print('--' *20)
quantidade = int(input('Quantos jogos você quer que eu sorteie? '))
total_jogos = 1
while total_jogos <= quantidade:
    cont = 0
    while True:
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total_jogos += 1
print('++' * 3,f'SORTEANDO {quantidade} JOGOS', '++' * 3 )    
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
