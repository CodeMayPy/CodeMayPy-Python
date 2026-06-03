import random
primeiro = str(input('Digite o nome do primeiro aluno: '))
segundo = str(input('Digite o nome do segundo aluno: '))
terceiro = str(input('Digite o nome do terceiro aluno: '))
quarto = str(input('Digite o nome do quarto aluno: '))
lista = [primeiro, segundo, terceiro, quarto]
random.shuffle(lista)
print(f'A ordem de apresentação dos trabalhos será: {lista}')