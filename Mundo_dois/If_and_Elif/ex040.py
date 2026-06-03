primeira_nota = float(input('Digite sua primeira nota: '))
segunda_nota = float(input('Digite sua segunda nota: '))

media = (primeira_nota + segunda_nota) / 2

if media < 5.0:
    print(f'Sua média é de {media}, você está REPROVADO(A)!')
elif media >= 5.0 and media <= 6.9:
    print(f'Sua média é {media} te vejo na RECUPERAÇÃO!')
else:
    print(f'Parabéns, sua média é de {media} você está APROVADO(A)!') 