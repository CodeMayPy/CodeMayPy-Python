print('Vamos calcular quantos litros de tinta você vai precisar para pintar uma parede?')
largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros:'))
print(f'A área que você quer pintar é de {largura*altura} metros, logo você precisará de {(largura*altura)/ 2} litros para pintar ela.')