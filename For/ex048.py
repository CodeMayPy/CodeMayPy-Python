#Sum of odd multiples of three
#48- Make a program that calculates the sum of all numbers that are multiples of three and that are in the
# range from 1 to 500.
soma = 0
counter = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        counter = counter + 1
        soma = soma + c
print(f'The sum of all {counter} requested values is {soma}.')


#Soma ímpares múltiplos de três
# 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no
# intervalo de 1 até 500.
soma = contador = 0
for c in range(1,501,2):
    if c % 3 == 0:
        contador = contador + 1
        soma = soma + c
print(f'Ao todo existem {contador} números multiplos de 3 em um intervalo de 1 a 500 e sua soma é {soma}.')


#PT- Estruturas de repetições: For.
#EN- Loop structures: For.