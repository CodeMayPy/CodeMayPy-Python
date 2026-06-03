soma = contador = 0
for c in range(1,501,2):
    if c % 3 == 0:
        contador = contador + 1
        soma = soma + c
print(f'Ao todo existem {contador} números multiplos de 3 em um intervalo de 1 a 500 e sua soma é {soma}.')