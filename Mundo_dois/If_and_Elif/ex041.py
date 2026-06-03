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
