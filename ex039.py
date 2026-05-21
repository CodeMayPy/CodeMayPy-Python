'''
#Versão antiga
#Alistamento Militar
#39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se
#alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também
#deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano_nascimento = int(input('Qual o seu ano de nascimento?'))
ano = date.today().year
idade = ano - ano_nascimento
print(f'Se você nasceu em {ano_nascimento} a sua idade é {idade}.')
if idade == 18:
    print('Você deve se alistar.')
elif idade < 18:
    print(f'Você ainda tem {18 - idade} aos até se alistar.')
elif idade > 18:
    print(f'Já passou {idade - 18} do prazo de alistamento')
'''


# Versão revisada
from datetime import date

ano_nascimento = int(input('Digite o ano do seu nascimeto com 4 digitos:'))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print(f'Você tem {idade} anos.')

if idade < 18:
    print(f'Você é novo, faltam {18 - idade} anos para você se alistar.')
elif idade == 18:
    print('Esse ano você fez ou já tem 18 anos, bora se alistar!')
else:
    print(f'Onde você estava? Passaram {idade -18} anos do tempo de se alistar.')
