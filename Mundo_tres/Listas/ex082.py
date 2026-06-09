numeros = list()
numeros_pares = list()
numeros_impares = list()

while True:
    dados = (int(input('Digite um número:')))
    numeros.append(dados)

    resposta = str(input('Quer continuar? [Sim/Não]')).upper().strip()[0]
    if resposta in "N":
        break

for i, v in enumerate(numeros):
    if v % 2 == 0:
        numeros_pares.append(v)
    elif v % 2 == 1:
        numeros_impares.append(v)

print(f'A lista completa ficou: {numeros}.')
print(f'A lista de pares ficou: {numeros_pares}.')
print(f'A lista de ímpares ficou: {numeros_impares}.')