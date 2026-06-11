matriz = [[0,0,0], [0,0,0], [0,0,0]]
lista_par = []
lista_impar = []

for linha in range(0,3):  #recebe os valores para a matriz
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-=' * 30)

for linha in range(0,3): #imprime a matriz
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

print('-=' * 30)    

for linha in range(0,3): #percorre a matriz para separar os pares dos ímpares
    for coluna in range(0,3):
        if matriz[linha][coluna] % 2 == 0:
            lista_par.append(matriz[linha][coluna])
        else:
            lista_impar.append(matriz[linha][coluna])

print(f'A soma dos valores pares é: {sum(lista_par)}.')
print(f'A soma dos valores da terceira coluna é: {sum([matriz[0][2], matriz[1][2], matriz[2][2]])}.')
print(f'O maior valor da segunda linha é: {max(matriz[1])}.')
