#First and last occurrence of a string
#26- Write a program that reads a sentence from the keyboard and shows how many times the letter "a" appears and in what position it is
# appears the first time and in what position it appears last time.
sentence = input('Enter a sentence:').upper()
print(f'The letter A shows {sentence.count('A')} times.')
print(f'The first letter A shows in position {sentence.find('A')+1}.')
print(f'The last letter A shows in position {sentence.rfind('A')+1}.')


# Primeira e última ocorrência de uma string
#26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a
# primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase:')).upper()
print(f'A letra A, aparece {frase.count('A')} vezes na frase.')
print(f'A primeira letra "A" apareceu na {frase.find('A')+1} posição da frase.')
print(f'A última letra "A" apareceu na {frase.rfind('A')+1} posição da frase.')

#PT- treinando a manipulação de strings.
#EN- training string manipulation.