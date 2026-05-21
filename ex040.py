'''
# versão antiga
#Aquele clássico da Média.
# 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
# com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO
nota = float(input('Digite sua primeira nota:'))
segunda_nota = float(input('Digite sua segunda nota:'))
media = (nota + segunda_nota) / 2
if media < 5.0:
    print('Você está reprovado.')
if media >= 5.0 and media < 6.9:
    print('Você está de recuperação.')
if media >= 7.0:
    print('Parabéns você passou.')
'''

# Versão revisada

primeira_nota = float(input('Digite sua primeira nota: '))
segunda_nota = float(input('Digite sua segunda nota:'))

media = (primeira_nota + segunda_nota) / 2

if media < 5.0:
    print(f'Sua média é de {media}, você está REPROVADO(A)!')
elif media >= 5.0 and media <= 6.9:
    print(f'Sua média é {media} te vejo na RECUPERAÇÃO!')
else:
    print(f'Parabéns, sua média é de {media} você está APROVADO(A)!') 
