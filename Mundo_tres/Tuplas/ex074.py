import random
cinco_numeros_aleatorios = tuple(random.sample(range(1,100), 5))
print(f'Os números gerados foram: {cinco_numeros_aleatorios}.')
print(f'O menor número foi: {min(cinco_numeros_aleatorios)}.')
print(f'E o maior número foi: {max(cinco_numeros_aleatorios)}.')