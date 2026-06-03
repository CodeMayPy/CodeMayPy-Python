# 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Grêmio.
times = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza',
         'Internacional', 'São Paulo', 'Corinthians', 'Bahia',
         'Cruzeiro', 'Vasco da Gama', 'Ec Vitória', 'Atlético-MG',
         'Fluminense', 'Grêmio', 'Juventude', 'Bragantino', 'Athletico-PR',
         'Criciúma', 'Atlético-GO', 'Cuiabá')
print(f'A lista dos times do Brasileirão é {times}.')
print(f'Os cinco primeiros times são: {times[0:5]}.')
print(f'Os quatro últimos são: {times [-4:]}.')
print(f'Os times em ordem alfabética ficam: {sorted(times)}.')
print(f'O Grêmio se encontra na posição {times.index("Grêmio")+1}º.')