#Sum of pairs
#50- Develop a program that reads six integers and displays the sum of only those that are even. If the value
# entered is odd, disregard it.
sum_numbers = 0
counter = 0
for c in range (1, 7):
    numbers = int(input(f'Enter the {c} value:'))
    if numbers % 2 == 0:
        sum_numbers += numbers
        counter += 1
print(f"You informed {counter} even numbers and their sum is {sum_numbers}.")


#Soma dos pares
#50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o.
soma_numeros = contador = 0
for c in range(1,7):
    numero = int(input(f'Digite o {c}ª número:'))
    if numero % 2 == 0:
        soma_numeros += numero
        contador += 1
print(f'Você informou {contador} números pares e a soma deles é {soma_numeros}.')

#PT- Estruturas de repetições: For.
#EN- Loop structures: For.