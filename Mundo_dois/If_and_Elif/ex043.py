print('Vamos ver se seu IMC está ideal...')
peso = float(input('Digite seu peso KG: '))
altura = float(input('Digite a sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f'Você está ABAIXO do peso, seu IMC é de {imc:.2f}.')
elif imc < 25:
    print(f'Você está no seu peso IDEAL e seu IMC é de {imc:.2f}.')
elif imc < 30:
    print(f'Você está com SOBREPESO e seu IMC é de {imc:.2f}.')
elif imc <= 40:
    print(f'Você está com OBESIDADE e seu IMC é de {imc:.2f}.')
else:
    print(f'Você esta com OBESIDADE MÓRBIDA e seu IMC é de {imc:.2f}.')