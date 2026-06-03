#Arithmetic Progression
#51-Develop a program that reads the first term and the ratio of an AP. At the end, show the first 10 terms
# of this progression.
first = int(input('First term:'))
ratio = int(input('Ratio:'))
tenth = first + (10-1) * ratio
for c in range(first,tenth + ratio, ratio):
    print(f'{c}', end=' -> ')
print('He finished')


#Progressão Aritmética
# 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos
# dessa progressão.
primeiro = int(input('Digite o primeiro termo da PA:'))
razao = int(input('Digite a razão da PA:'))
dez = primeiro + (10 - 1) * razao
for contador in range(primeiro, dez + razao, razao):
    print(f'{contador}', end='-')
print('Fim')


#PT- Estruturas de repetições: For.
#EN- Loop structures: For.