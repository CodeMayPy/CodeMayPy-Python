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