frase = str(input('Digite uma frase: ')).upper()
print(f'A letra A, aparece {frase.count("A")} vezes na frase.')
print(f'A primeira letra "A" apareceu na {frase.find("A")+1} posição da frase.')
print(f'A última letra "A" apareceu na {frase.rfind("A")+1} posição da frase.')
