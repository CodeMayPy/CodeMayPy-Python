import time
cidade = str(input('Digite o nome de uma cidade: ')).strip()
print('Tem Santo no nome?')
time.sleep(1)
print(cidade[:5].upper() == 'SANTO')