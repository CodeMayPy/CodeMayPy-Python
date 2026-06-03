contagem = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nova', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    numero = int(input('Digite um número de 0 a 20: '))

    if 0 <= numero <= 20:
        print(f'O número informado foi: {contagem[numero]}.')
        break

    else:
        print('Tente novamente.')