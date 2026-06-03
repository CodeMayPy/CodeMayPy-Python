from random import randint
computador = randint(0,10)
print('Eu estou pensando em um número de 0 a 10, tente adivinhar qual é!')
acerto = False
tentativa = 0
while not acerto:
    jogador = int(input('Qual o seu palpite? '))
    tentativa += 1
    if jogador == computador:
        acerto = True
    else:
        if jogador < computador:
            print('Tente novamente.')
        elif jogador > computador:
            print('Quase, tente denovo.')
print(f'Você acertou na sua {tentativa}ª. Parabéns')
