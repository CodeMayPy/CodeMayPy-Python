from random import randint
computador = randint(0,5)
print('Estou pensanem em um número de 0 a 5, tente adivinhar qual é...')
jogador = int(input('Qual número eu pensei? '))
if jogador == computador:
    print('Parabéns você acertou!')
else:
    print(f'Você perdeu. Eu pensei no {computador} e não no {jogador}.')
