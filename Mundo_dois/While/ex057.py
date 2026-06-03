#EN- Loop structure: While
#Data Validation
#57- Make a program that reads a person's gender, but only accepts the values ​​'M' or 'F'. If it's wrong, ask
# typing again until you have a correct value.
gender = str(input('What is your gender?[F/M]:')).strip().upper()[0]
while gender not in 'MmFf':
    gender = str(input('Invalid data!! Please enter your gender:')).strip().upper[0]
print(f'Gender {gender} successfully registered.')


#PT- Estrutura de repetição: While
#Validação de Dados
# 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a
# digitação novamente até ter um valor correto.
sexo = str(input('Qual é o seu gênero? [F/M]')).strip().upper[0]
while sexo not in 'MmFf':
    sexo = str(input('Informação inválida. Digite novamente:')).strip().upper[0]
print(f'Gênero {sexo} registrado.')