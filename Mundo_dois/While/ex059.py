primeiro_numero = int(input('Digite um valor: '))
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