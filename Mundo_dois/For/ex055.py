#Largest and smallest of the sequence
#55-Make a program that reads the weight of five people. At the end, show which was the largest and smallest weight read.
bigger = smaller = 0
for p in range(1, 6):
    weight = float(input(f"What's the weight of person {p}"))
    if p == 1:
        bigger = weight
        smaller = weight
    else:
        if weight > bigger:
            bigger = weight
            if weight < smaller:
                smaller = weight
print(f"The largest weight read was {bigger}kg")
print(f"The smallest weight read was {smaller}Kg")


#Maior e menor da sequência
#55-Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for p in range (1,6):
    peso = float(input(f'Qual o pesso da {p}ª pessoa:'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}kg.')
print(f' O menor peso lido foi de {menor}Kg,')


#PT- Estruturas de repetições: For.
#EN- Loop structures: For.