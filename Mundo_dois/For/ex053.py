frase = str(input('Digite uma frase:')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for palavras in range(len(junto)-1,-1,-1):
    inverso += junto[palavras]
if inverso == junto:
    print('Nós temos um palíndromo.')
else:
    print('Nós não temos um palíndromo.')