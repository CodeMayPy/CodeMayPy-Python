primeiro_numero = int(input('Digite um número inteiro: '))
segundo_numero = int(input('Digite outro número inteiro: '))
print(f'Vou comparar os números {primeiro_numero} e {segundo_numero} informados...')

if primeiro_numero > segundo_numero:
    print(f'O número {primeiro_numero} é maior que o {segundo_numero}.')
elif primeiro_numero < segundo_numero:
    print(f'O número {segundo_numero} é maior que {primeiro_numero}.')
else:
    print('Não existe número maior ou menor, os dois são iguais.')
