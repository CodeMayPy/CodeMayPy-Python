#Sorting an order in the list
#20- The same teacher from challenge 19 wants to draw the order in which the students' work will be presented. Make a program that
# read the names of the four students and show the order drawn.
'''import random
first_name = str(input('First students name:'.strip()))
second_name = str(input('Second students name:'.strip()))
third_name = str(input('Third students name:'.strip()))
fourth_name = str(input('Fourth students name:'.strip()))
list = [first_name, second_name, third_name, fourth_name]
random.shuffle(list)
print('The order of presentation of students will be:')
print(list)'''


#Sorteando uma ordem na lista
#20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa
#que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
primeiro = str(input('Digite o nome do primeiro aluno:'))
segundo = str(input('Digite o nome do segundo aluno:'))
terceiro = str(input('Digite o nome do terceiro aluno:'))
quarto = str(input('Digite o nome do quarto aluno:'))
lista = [primeiro, segundo, terceiro, quarto]
random.shuffle(lista)
print(f'A ordem de apresentação dos trabalhos será: {lista}')