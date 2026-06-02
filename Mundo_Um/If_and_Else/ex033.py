#Highest and lowest values
#33- Write a program that reads three numbers and shows which is the largest and which is the smallest.
first_value = int(input('Enter the first value:'))
second_value = int(input('Enter the second value:'))
third_value = int(input('Enter the tirth value:'))
smallest = first_value
if second_value < first_value and second_value < third_value:
    smallest = second_value
if third_value < first_value  and third_value < second_value:
    smallest = third_value
largest = first_value
if second_value > first_value and second_value > third_value:
    largest = second_value
if third_value > first_value and third_value > second_value:
    largest = third_value
print(f'The smallest value is {smallest}.')
print(f'The largest value is {largest}.')


# Maior e menor valores
#33: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
primeiro = int(input('Digite um número:'))
segundo = int(input('Digite outro número:'))
terceiro = int(input('Digite mais um número:'))
menor = primeiro
if segundo < primeiro and segundo < terceiro:
    menor = segundo
if terceiro < primeiro and terceiro < segundo:
    menor = terceiro
maior = primeiro
if segundo > primeiro and segundo > terceiro:
    maior = segundo
if terceiro > primeiro and terceiro > segundo:
    maior = terceiro
print(f'O maior valor é {maior}.')
print(f'O menor valor é {menor}.')

#PT- Exercícios com uso de condicional.
#EN- Exercises using conditional.