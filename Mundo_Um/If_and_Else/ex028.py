#Guessing Game v.1.0
#28- Write a program that makes the computer "think" of an integer between 0 and 5 and ask the user to try
# find out which number was chosen by the computer. The program should write on the screen whether the user won or
# it lost.
from random import randint
computer = randint(0, 5)
print('-=-' * 20)
print('I will think of a number from 0 to 5, try guess...')
print('-=-' * 20)
player = int(input('What number did I think of?'))
if player == computer:
    print('CONGRATULATIONS! You beat me.')
else:
    print(f'I WON!!!!! I thought about the number {computer} and not in {player}!')


#Jogo da Adivinhação v.1.0
#28: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
computador = randint(0,5)
print('Estou pensanem em um número de 0 a 5, tente adivinhar qual é...')
jogador = int(input('Qual número eu pensei?'))
if jogador == computador:
    print('Parabéns você acertou!')
else:
    print(f'Você perdeu. Eu pensei no {computador} e não no {jogador}.')

#PT- Exercícios com uso de condicional.
#EN- Exercises using conditional.