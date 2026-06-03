import random
primeiro = str(input('Qual o nome do primeiro aluno: '))
segundo = str(input('Qual o nome do segundo aluno: '))
terceiro = str(input('Qual o nome do terceiro aluno: '))
quarto = str(input('Qual o nome do quarto aluno:'))
lista = [primeiro, segundo, terceiro, quarto]
print(f'O aluno escolhido foi: {random.choice(lista)}')