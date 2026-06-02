#EN- Loop structure: While
#Guessing Game v2.0
#58- Improve the challenge 28 game where the computer will “think” of a number between 0 and 10. But now the player will
#try to guess until you get it right, showing at the end how many guesses it took to win.
'''from random import randint
computer = randint(0,10)
print('I am your computer. . . I just thought of a number between 0 and 10. ')
print('Can you guess which one it was?')
got_it_right = False
guesses = 0
while not got_it_right:
    player = (int(input('What is your guess?')))
    guesses +=1
    if player == computer:
        got_it_right = True
    else:
        if player < computer:
            print('More. Try again.')
        elif player > computer:
            print('Less. Try again.')
print(f'You got it rigth with {guesses} attempts. Congratulations!')'''


#PT- Estrutura de repetição: While.
#Jogo da Adivinhação v2.0
#58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai
# tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
computador = randint(0,10)
print('Eu estou pensando em um número de 0 a 10, tente adivinhar qual é!')
acerto = False
tentativa = 0
while not acerto:
    jogador = int(input('Qual o seu palpite?'))
    tentativa += 1
    if jogador == computador:
        acerto = True
    else:
        if jogador < computador:
            print('Tente novamente.')
        elif jogador > computador:
            print('Quase, tente denovo.')
print(f'Você acertou na sua {tentativa}ª. Parabéns')
