numero = int(input('Digite um número: '))
total = 0
for contador in range(1,numero,+1):
    if numero % contador == 0:
        print(end='')
        total += 1
    else:
        print(end='')
if total == 2:
    print('O número é primo.')
else:
    print('O número é impar.')