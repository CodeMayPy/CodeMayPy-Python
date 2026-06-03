velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print(f'Você passou {velocidade - 80}Km/h do limite e deverá pagar R${(velocidade - 80)*7:.2f} de multa!')