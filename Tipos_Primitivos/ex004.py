#Dissecting a variable.
#04- Write a program that reads something from the keyboard and shows its primitive type and all the
#possible information about him.
'''value = input('Type something:')
print('The primitive type of this value is:', type(value))
print('Is alphabetical?', value.isalpha())
print('Is a number?', value.isnumeric())
print('There are only spaces?', value.isspace())
print('Is alphanumeric?', value.isalnum())
print('Is upper?', value.isupper())
print('is lower?', value.islower())
print('Only the first letter is capitalized?', value.istitle())'''

#Dissecando uma variável.
#Escreva um programa que leia algo pelo teclado e mostre seu tipo primitivo e todas as informações possíveis sobre ele.
valor = input('Digite algo para eu analisar:')
print('O tipo primitivo desse dado é:', type(valor))
print('É alfabetico? ' ,valor.isalpha())
print('É um número? ',valor.isnumeric())
print('Só tem espaços? ',valor.isspace())
print('É alphanumérico? ',valor.isalnum())
print('Está em caixa alta? ',valor.isupper())
print('Está em caixa baixa? ',valor.islower())
print('A primeira letra está em maiúsculo?',valor.istitle())

#PT- nesse exercício testamos algumas formas de verificar os tipos de um dado informado.
#EN- in this exercise we tested some ways to check the types of an informed data.