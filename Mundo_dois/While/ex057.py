genero = str(input('Qual é o seu gênero? [F/M] ')).strip().upper()[0]
while genero not in 'MmFf':
    genero = str(input('Informação inválida. Digite novamente: ')).strip().upper()[0]
print(f'Gênero {genero} registrado.')