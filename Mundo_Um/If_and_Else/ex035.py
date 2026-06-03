primeiro = float(input('Digite o valor da primeira reta: '))
segundo = float(input('Digite o valor da segunda reta: '))
terceiro = float(input('Digite o valor da terceira reta: '))
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < segundo + primeiro:
    print('Você terá um triângulo.')
else:
    print('Você não terá um triângulo.')