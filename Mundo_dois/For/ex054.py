atual = date.today().year
total_maior = 0
total_menor = 0
for pessoas in range(1, 8):
    nascimento = int(input(f'Em que ano a {pessoas}ª pessoa nasceu?'))
    idade = atual - nascimento
    if idade >= 21:
        total_maior += 1
    else:
        total_menor += 1
print(f' Ao todo tivemos {total_maior} pessoas maiores de idade.')
print(f'E {total_menor} pessoas menores de idade.')