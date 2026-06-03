primeiro_termo = int(input('Digite o primeiro valor:'))
razao = int(input('Qual a razão da PA?'))
termo = primeiro_termo
contador = 1
while contador <= 10:
    print(f'{termo}', end=' ')
    termo += razao
    contador += 1