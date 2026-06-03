total_maior = total_homem = total_mulher = 0
while True:
    idade = int(input('Qual a sua idade? '))
    genero = ' '
    while genero not in "FM":
        genero = str(input('Qual o seu gênero? [F/M] ')).strip().upper()[0]
    if idade >= 18:
        total_maior += 1
    if genero == "M":
        total_homem += 1
    if genero == "F" and idade < 20:
        total_mulher += 1
    resposta = ' '
    while resposta not in "SN":
        resposta = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resposta == "N":
        break
print(f"O total de pessoas com mais de 20 anos é {total_maior}.")
print(f'Ao total temos {total_homem} homens cadastrados.')
print(f'Ao total temos {total_mulher} mulheres com menos de 20 anos de idade.')