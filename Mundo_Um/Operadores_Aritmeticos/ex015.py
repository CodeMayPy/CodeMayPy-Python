kilometros = float(input('Quantos Km você rodou com o carro? '))
dias = int(input('Quandos dias você ficou com o carro alugado? '))
valor_km = kilometros * 0.15
valor_dia = dias * 60
print(f'Se você rodou {kilometros}km e ficou {dias} dias com o carro, logo você deverá pagar R${valor_dia + valor_km} de locação do carro.')

