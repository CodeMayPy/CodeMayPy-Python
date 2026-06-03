brasileirao = ('Palmeiras', 'Flamengo', 'Fluminense', 'Athletico-PR', 'Bragantino', 'Coritiba', 'São Paulo', 'Bahia', 'Cruzeiro', 'Botafogo', 'EC Vitória', 'Atlético-MG', 'Internacional', 'Grêmio', 'Corinthians', 'Vasco da Gama', 'Santos', 'Mirassol', 'Remo', 'Chapecoense')

print(f'Os cinco primeiros colocados em ordem são: {brasileirao[0:5]}')
print()

print(f'Os 4 últimos colocados são: {brasileirao[-4:]}')
print()

tupla_ordem = tuple(sorted(brasileirao))

print(f'Os 20 times classificados no Brasileirão em ordem alfbética será: {tupla_ordem}.')
print()

print(f' O time Chapeco se encontra na posição: {brasileirao.index("Chapecoense")+1} da classificação')