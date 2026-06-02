#EN- Loop structure: While
#Creating an Options Menu
#59-Create a program that reads two values and displays a menu on the screen:
#[ 1 ] add
#[ 2 ] multiply
#[ 3 ] bigger
#[ 4 ] new numbers
#[ 5 ] exit the program
#Your program must perform the requested operation in each case.
first_value = int(input('Enter a number:'))
second_value = int(input('Enter other number:'))
while True:
    print('''Choose an option...
         [1] Add
         [2] Multiply
         [3] Bigger
         [4] New numbers
         [5] Exit the program ''')
    choice = int(input('Enter your choice:'))
    if choice == 1:
       add = first_value + second_value
       print(f'The sum of {first_value} + {second_value} is {add}')
    elif choice == 2:
       multiply = first_value * second_value
       print(f'The product of {first_value} and {second_value} is {multiply}')
    elif choice == 3:
        if first_value > second_value:
            bigger = first_value
        else:
            bigger = second_value
        print(f'Between {first_value} and {second_value} the largest value is {bigger}.')
    elif choice == 4:
        print('Enter the numbers again:')
        first_value = int(input('Enter a number:'))
        second_value = int(input('Enter other number:'))
    elif choice == 5:
         print('Finishing...')
         break
    else:
        print('Invalid option. Try again.')
print('End of program.')


#PT- Estrutura de repetição: While.
#Criando um Menu de Opções
#059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
primeiro_numero = int(input('Digite um valor:'))
segundo_numero = int(input('Agora digite outro valor:'))
while True:
    print('''Escolha uma opção:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    escolha = int(input('Digite sua escolha:'))
    if escolha == 1:
        print(f'A soma do {primeiro_numero} + {segundo_numero} é igual a {primeiro_numero+segundo_numero}.')
    elif escolha == 2:
        print(f"O produto entre {primeiro_numero} e {segundo_numero} é {primeiro_numero*segundo_numero}.")
    elif escolha == 3:
        if primeiro_numero > segundo_numero:
            maior = primeiro_numero
        else:
            maior = segundo_numero
        print(f"Entre {primeiro_numero} e o {segundo_numero} o maior é {maior}.")
    elif escolha == 4:
        print('Digita os novos números:')
        primeiro_numero = int(input('Digite o novo valor:'))
        segundo_valor = int(input('Digite um segundo valor:'))
    elif escolha == 5:
        print("Fim do programa")
        break