#Drawing an item from the list
#19- A teacher wants to draw one of his four students to erase the board. Make a program that helps him, reading the
# name of the students and writing the name of the chosen one on the screen.
import random
name_one = str(input('First students name:'))
name_two = str(input('Second students name:'))
name_three = str(input('Third students name:'))
name_four = str(input('Fourth students name:'))
list = [name_one, name_two, name_three, name_four]
chosen = random.choice(list)
print(f'The student chosen to erase the board is {chosen}.')


#Sorteando um item na lista
#19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o
#nome dos alunos e escrevendo na tela o nome do escolhido.
'''import random
primeiro = str(input('Qual o nome do primeiro aluno:'))
segundo = str(input('Qual o nome do segundo aluno:'))
terceiro = str(input('Qual o nome do terceiro aluno:'))
quarto = str(input('Qual o nome do quarto aluno:'))
lista = [primeiro, segundo, terceiro, quarto]
print(f'O aluno escolhido foi: {random.choice(lista)}')'''

#PT- Foi preciso importar o ramdom para misturar os dados da lista (e criar a lista) depois pedir ao programa para escolher
#um dos dados informados da lista pelo comando choise.
#EN-It was necessary to import the ramdom to mix the data from the list (and create the list) and then ask the program to
# choose one of the data provided in the list by the choise command.