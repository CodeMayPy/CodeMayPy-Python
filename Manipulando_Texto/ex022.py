#Text Analyzer
#22- Create a program that reads a person's full name and displays:
# - The name in all upper and lower case letters.
# - How many letters in total without considering spaces
# - How many letters are in the first name.
name = str(input('Enter your full name:'))
print('Analyzing your name...')
print(f'Your name in capital letters:{name.upper()}.')
print(f'Your name in lower case:{name.lower()}.')
print(f'Your name in total has {len(name)-name.count(' ')} letters.')
separate = name.split()
print(f'Your first name is {separate[0]} and he has {len(separate[0])} letters.')

#Analisador de Textos
# 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.
'''nome = str(input("Qual o seu nome completo?"))
print(f"Seu nome com todas as letras em maiúsculo fica: {nome.upper()}")
print(f"Seu nome em minúsculo fica: {nome.lower()}")
print(f"Seu nome sem espaços tem {len(nome)-nome.count(' ')} letras.")
separado = nome.split()
print(f"Seu primeiro nome {separado[0]}  tem {len(separado[0])} letras.")'''


#PT- treinando a manipulação de strings.
#EN- training string manipulation.