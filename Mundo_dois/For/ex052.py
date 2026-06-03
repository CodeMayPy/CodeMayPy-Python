#Prime numbers
#52- Write a program that reads an integer and tells whether or not it is a prime number.
number = int(input('Enter a integer number:'))
tot = 0
for c in range(1, number, +1):
    if number % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[m The number {number} was divisible {tot} times.')
if tot == 2:
    print('And that is why he is a prime number.')
else:
    print('And that is why it is not a prime number.')


#Números primos
#52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero = int(input('Digite um número:'))
total = 0
for contador in range(1,numero,+1):
    if numero % contador == 0:
        print(end='')
        total += 1
    else:
        print(end='')
if total == 2:
    print('O número é primo.')
else:
    print('O número é impar.')

# PT- Estruturas de repetições: For.
# EN- Loop structures: For.