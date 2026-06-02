'''
#Versão antiga
#GAME: Pedra Papel e Tesoura
#45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
print('Vamos jogar jokenpô')
items= ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual a sua jogada?'))
print(f'computador jogou {items[computador]}.')
print(f'Você jogou {items[jogador]}.')
if computador == 0:
   if jogador == 0:
      print('Empate.')
   elif jogador == 1:
       print('Você ganhou!')
   elif jogador == 2:
        print('Computador ganhou!')
   else:
       print('Jogada inválida!')
elif computador == 1:
    if jogador == 0:
      print('Computador ganhou!')
    elif jogador == 1:
      print('Empate!')
    elif jogador == 2:
      print('Você ganhou!')
    else:
        print('Jogada inválida!')
elif computador == 2:
    if jogador == 0:
       print('Você ganhou!')
    elif jogador == 1:
         print('Computador ganhou!')
    elif jogador == 2:
         print('Empate!')
    else:
        print('Jogada inválida!')
'''

#Versão revisada

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
