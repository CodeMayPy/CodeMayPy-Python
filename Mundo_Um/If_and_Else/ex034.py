#Multiple increases
#34- Write a program that asks for an employee's salary and calculates the amount of his raise. For salaries
# above R$1,250.00, calculate an increase of 10% for those below or equal, the increase is 15%
salary = float(input('What is your salary in U$?'))
if salary <= 1250:
    new = salary + (salary * 0.15)
else:
    new = salary + (salary * 0.10)
print(f'Who won U${salary:.2f} starts to win U${new:.2f} now.')


#Aumentos múltiplos
#34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual o seu salário em R$:'))
if salario <= 1250:
    novo = salario + (salario * 0.15)
else:
    novo = salario + (salario * 0.10)
    print(f'Seu antigo salário de {salario:.2f} recebeu um reajuste e ficou R${novo:.2f}.')

#PT- Exercícios com uso de condicional.
#EN- Exercises using conditional.