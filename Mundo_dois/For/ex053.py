#Palindrome Detector
#53- Create a program that reads any sentence and says if it is a palindrome, disregarding spaces.
sentence = str(input('Enter a sentence:')).strip().upper()
words = sentence.split()
together = ''.join(words)
reverse = ''
for words in range(len(together)-1, -1, -1):
    reverse += together[words]
print(f'The reverse of {together} is {reverse}.')
if reverse == together:
    print('We have a palindrome.')
else:
    print('The sentence is not a palindrome.')


#Detector de Palíndromo
#53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos
# de palíndromos:APÓS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.
frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for palavras in range(len(junto)-1,-1,-1):
    inverso += junto[palavras]
if inverso == junto:
    print('Nós temos um palíndromo.')
else:
    print('Nós não temos um palíndromo.')


#PT- Estruturas de repetições: For.
#EN- Loop structures: For.