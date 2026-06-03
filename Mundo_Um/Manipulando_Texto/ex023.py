numero = int(input('Digite um número inteiro qualquer: '))
print(f'Analizando o numero {numero}....')
print(f'Sua unidade é {numero // 1 % 10}, '
      f'sua dezena é {numero // 10 % 10},'
      f'sua centena é {numero // 100 % 10},'
      f'e seu milhar é {numero // 1000 % 10}')