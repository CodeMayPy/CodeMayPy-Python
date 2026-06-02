#EN- Loop structure: While
#Arithmetic Progression v2.0
#61-  Redo CHALLENGE 51, reading the first term and the reason of an AP,showing the first 10 terms of the progression
#  using the while structure.
print("Arithmetic progression generator")
print("-=-" * 20)
first_term = int(input("Enter the first term:"))
reason = int(input("Enter the reason of the arithmetic progression:"))
term = first_term
counter = 1
while counter <= 10:
    print(f"{term}", end=' ')
    term += reason
    counter += 1
print("End")

#PT- Estruturas de repetição: While.
#Progressão Aritmética v2.0
#61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.
primeiro_termo = int(input('Digite o primeiro valor:'))
razao = int(input('Qual a razão da PA?'))
termo = primeiro_termo
contador = 1
while contador <= 10:
    print(f'{termo}', end=' ')
    termo += razao
    contador += 1

