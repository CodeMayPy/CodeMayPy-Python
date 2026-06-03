# 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são as suas vogais.
frutas = ('banana', 'maça', 'abacaxi', 'abacate',
          'limao', 'pera', 'maracuja', 'melancia',
          'kiwi', 'bergamota', 'ameixa', 'melao')
for p in frutas:
    print(f'\n Na palavra {p.upper()} temos ' ,end='')
    for letra in p:
        if letra.lower() in "aeiou":
            print(letra, end=' ')
