soma_numeros = contador = 0
for c in range(1,7):
    numero = int(input(f'Digite o {c}ª número: '))
    if numero % 2 == 0:
        soma_numeros += numero
        contador += 1
print(f'Você informou {contador} números pares e a soma deles é {soma_numeros}.')