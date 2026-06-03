primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA:'))
dez = primeiro + (10 - 1) * razao
for contador in range(primeiro, dez + razao, razao):
    print(f'{contador}', end='-')
print('Fim')