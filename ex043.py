'''
#Versão antiga
#Índice de Massa Corporal
# 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre
#seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida
peso = float(input('Qual é o seu peso em KG:'))
altura = float(input('Qual é a sua altura em metros?'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f} e você está abaixo do peso.')
elif imc >= 18.5 and imc <25:
    print(f'Seu IMC é {imc:.2f} e você está no seu peso ideal.')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é de {imc:.2f} e você está com sobrepeso.')
elif imc >= 30 and imc <= 40:
    print(f'Seu IMC é de {imc:.2f} e você está com obesidade.')
elif imc > 40:
    print(f'Seu IMC é de {imc:.2f} e você está com obesidade mórbida.')
'''

#Versão revisada

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
