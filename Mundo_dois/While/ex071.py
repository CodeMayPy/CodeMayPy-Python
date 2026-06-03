valor = int(input('Qual valor você deseja sacar? R$ '))
total = valor
nota = 50
total_nota = 0
while True:
    if total >= nota:
        total -= nota
        total_nota += 1
    else:
        if total_nota > 0:
            print(f'Total de {total_nota} cédulas de R${nota}.')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        total_nota = 0
        if total == 0:
         break
