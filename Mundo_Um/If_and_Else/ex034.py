salario = float(input('Qual o seu salário em R$: '))
if salario <= 1250:
    novo = salario + (salario * 0.15)
else:
    novo = salario + (salario * 0.10)
print(f'Seu antigo salário de {salario:.2f} recebeu um reajuste e ficou R${novo:.2f}.')