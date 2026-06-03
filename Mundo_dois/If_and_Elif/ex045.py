import time
import random

print('Vamos jogar pedra, papel ou tesoura!')
time.sleep(1)

print('''Escolha:
         [1]- Pedra;
         [2]- Papel;
         [3]- Tesoura.''')

jogador = int(input('Qual a sua jogada? '))
opcoes = 'Pedra', 'Papel', 'Tesoura'
jogada_computador = random.choice(opcoes)

if jogador != 1 and jogador != 2 and jogador != 3:
    print('Jogada inválida, tente novamente.')
else:
    time.sleep(2)
    print('JO')
    time.sleep(2)
    print('Ken')
    time.sleep(2)
    print('PÔ\n')
    print()
print(jogada_computador)
print()

if jogada_computador == 'Pedra':
    if jogador == 1:
        print('Deu EMPATE, haha vamos de novo.')
    elif jogador == 2:
        print('Eu joguei PEDRA e você jogou PAPEL...\nPerdi, vamos denovo?')
    elif jogador == 3:
        print('Eu joguei PEDRA e você TESOURA... \nGanhei, quer revanche?')


if jogada_computador == 'Papel':
    if jogador == 1:
        print('Eu joguei PAPEL e você jogou PEDRA...\nGanhei, quer revanche?')
    elif jogada_computador == 'Papel' and jogador == 2:
        print('Deu EMPATE, haha vamos de novo.')
    elif jogada_computador == 'Papel' and jogador == 3:
        print('Eu joguei PAPEL e você jogou TESOURA...\nPerdi, vamos denovo?')
     

if jogada_computador == 'Tesoura':
    if jogador == 1:
        print('Eu joguei TESOURA e você jogou PEDRA...\nPerdi, vamos denovo?')
    elif jogador == 2:
        print('Eu joguei TESOURA e você jogou PAPEL...\nGanhei, quer revanche?')
    elif jogador == 3:
        print('Deu EMPATE, haha vamos de novo.')