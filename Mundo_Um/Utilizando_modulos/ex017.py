import math
cateto_oposto = float(input('Digite o valor do cateto oposto: '))
cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
print(f'O cateto oposto é {cateto_oposto} e o cateto adjacente é {cateto_adjacente} logo a hipotenusa é {math.hypot(cateto_oposto,cateto_adjacente):.2f}')