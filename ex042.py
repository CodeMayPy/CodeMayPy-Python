'''
#Versão antiga
#Analisando Triângulos v2.0
#42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes
primeiro = float(input('Qual o primeiro valor?'))
segundo = float(input('Qual o segundo valor?'))
terceiro = float(input('Qual o terceiro valor?'))
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < primeiro + segundo:
    print('Os dadod informados podem formar um triângulo, ' ,end=' ')
    if primeiro == segundo == terceiro:
        print('Equilátero.')
    elif primeiro != segundo != terceiro != primeiro:
        print('Escaleno')
    else:
        print('isósceles.')
else:
    print('Os dados informados não formaram um triângulo.')
    '''

#Versão revisada

primeiro_valor = float(input('Digite o valor da primeira reta:'))
segundo_valor = float(input('Digite o valor da segunda reta:'))
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
