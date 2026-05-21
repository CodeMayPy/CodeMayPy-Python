'''
# Versão antiga
#Classificando Atletas
#041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
#sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER
from datetime import date
nascimento = int(input('Qual o seu ano de nascimento?'))
ano = date.today().year
idade = ano - nascimento
if idade <= 9:
    print(f'Sua idade é {idade} então sua categoria é a mirim.')
if idade > 9 and idade <= 14:
    print(f'Sua idade é {idade} então sua categoria é a infantil.')
if idade  > 14 and idade <= 19:
    print(f'Sua idade é {idade} então sua categoria é a junior.')
if idade > 19 and idade <= 25:
    print(f'Sua idade é {idade} então sua categoria é a sênior.')
elif idade >= 26:
    print(f'Sua idade é {idade} e sua categoria é a master.')

'''

# Versão revisada

from datetime import date 

ano_nascimento = int(input('Digite o ano do seu nascimento com 4 digitos: '))
ano_atual = date.today().year

idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f'Você tem {idade} anos, sua categoria é a MIRIM.')
elif idade > 9 and idade <= 14:
    print(f'Você tem {idade} anos, sua categoria é a INFANTIL.')
elif idade > 14 and idade <= 19:
    print(f'Você tem {idade} anos, sua categoria é a JÚNIOR.')
elif idade > 19 and idade <= 25:
    print(f'Você tem {idade} anos, sua categoria é a SÊNIOR.')
else:
    print(f'Você tem {idade} anos, sua categoria é a MASTER.')
