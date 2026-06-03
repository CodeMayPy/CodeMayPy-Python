primeiro_valor = float(input('Digite o valor da primeira reta: '))
segundo_valor = float(input('Digite o valor da segunda reta: '))
terceiro_valor = float(input('Digite o valor da terceira reta:'))

if primeiro_valor < segundo_valor + terceiro_valor and segundo_valor < primeiro_valor + terceiro_valor and terceiro_valor < primeiro_valor + segundo_valor: #valida a existência do triângulo

    if primeiro_valor == segundo_valor == terceiro_valor:
        print('Todos os lados são iguais e você tem um triângulo EQUILÁTERO.')
    elif primeiro_valor != segundo_valor != terceiro_valor != primeiro_valor: 
        print('Todos os lados são diferentes e você tem um triângulo ESCALENO.')
    else:
        print('Você possui dois lados iguais e um diferente e tem um triângulo ISÓSCELES.')
else:
    print('Os valores informados não podem formar um triângulo.')
