numero = int(input('Digite um número inteiro qualquer: '))
print(f'Perfeito, você digitou: {numero}.\nAgora vamos transformar ele, escolha uma opção:')

escolha = int(input('Transforme em:\n[1]- Binário;\n[2]- Octal;\n[3]- Hexadecimal.\nOpção: '))

if escolha == 1:
    print(f'O número {numero} convertido para binário é {bin(numero)[2:]}')
elif escolha == 2:
    print(f'O número {numero} convertido para octal fica {oct(numero)[2:]}')
elif escolha == 3:
    print(f'O número {numero} convertido para hexadecimal fica {hex(numero)[2:]}')
else:
    print('Escolha errada, tente novamente!')    
