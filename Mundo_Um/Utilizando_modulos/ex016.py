#Breaking down a number.
#16- Create a program that reads any real number from the keyboard and displays its entire portion on the screen.
import math
number = float(input('Enter a value:'))
print('The value typed was {} and its entire part is {}.'.format(number, math.trunc(number)))


#Quebrando um número.
#16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
'''import math
numero = float(input('Digite um número com parte fracionária:'))
print(f'O número informado foi {numero} e sua parte inteira é {math.trunc(numero)}')'''

#PT- Treinando o uso de modulos, no caso math.
#EN- Training the use of modules, in this case math.