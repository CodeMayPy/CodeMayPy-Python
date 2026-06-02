'''
#Versão antiga
#37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de
#conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input('Digite um número inteiro qualquer:'))
print('''Escolha uma das bases de conversão:
      [ 1 ] BINÁRIO'
      [ 2 ] OCTAL'
      [ 3 ] HEXADECIMAL''')
opcao = int(input('Digite sua escolha:'))
if opcao == 1:
    print(f'o número {numero} convertido para binário fica: {bin(numero)[2:]}.')
elif opcao == 2:
    print(f'O número {numero} convertido para octal fica: {oct(numero)[2:]}.')
elif opcao == 3:
    print(f'O número {numero} convertido para hexadecimal fica: {hex(numero)[2:]}.')
else:
    print('Opção inválida, tente novamente.')
'''

#Versão revisada
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
