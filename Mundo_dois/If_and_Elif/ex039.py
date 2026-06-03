from datetime import date

ano_nascimento = int(input('Digite o ano do seu nascimeto com 4 digitos: '))

ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print(f'Você tem {idade} anos.')

if idade < 18:
    print(f'Você é novo, faltam {18 - idade} anos para você se alistar.')
elif idade == 18:
    print('Esse ano você fez ou já tem 18 anos, bora se alistar!')
else:
    print(f'Onde você estava? Passaram {idade -18} anos do tempo de se alistar.')
