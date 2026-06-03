#Complete analyzer
##56-Develop a program that reads the name, age and sex of 4 people. At the end of the program, show: the average age
#of the group, what is the name of the oldest man and how many women are under 20?
amount_age = average_age = older_man = 0
name_older = ' '
total_woman = 0
for p in range (1,5):
    name = str(input("Name:")).strip()
    age = int(input("Age:"))
    gender = str(input("Gender [M/F]:")).strip()
    amount_age += age
    if p == 1 and gender in "Mm":
        older_man = age
    if gender in "Mm" and idade > amount_age:
        amount_age = age
        name_older = name
    if gender in "Ff" and age < 20:
        total_woman += 1
average_age = amount_age  / 4
print(f'The average age of the group is {average_age} years.')
print(f'The oldest man is {older_man} and is called {name}')
print(f'In total there are {total_woman} women under 20 years old.')


#Analisador completo
#56-Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade
#do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ' '
tot_mulher20 = 0
for p in range(1, 5):
    print(f'---- {p}ª pessoa ----')
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo: [M/F]:')).strip()
    soma_idade += idade
    if p == 1 and sexo in "Mm":
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
            tot_mulher20 += 1
media_idade = soma_idade / 4
print(f'A média de idade do grupo é de {media_idade} anos.')
print(f'O homem mais velho tem {maior_idade_homem} e se chama {nome_velho}.')
print(f'Ao todo são {tot_mulher20} mulheres com menos de 20 anos.')

#PT- Estruturas de repetições: For.
#EN- Loop structures: For.
