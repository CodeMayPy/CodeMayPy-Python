frutas = ('banana', 'maça', 'abacaxi', 'abacate',
          'limao', 'pera', 'maracuja', 'melancia',
          'kiwi', 'bergamota', 'ameixa', 'melao')
for p in frutas:
    print(f'\n Na palavra {p.upper()} temos ' ,end='')
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=' ')
