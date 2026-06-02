#Analyzing Triangle v1.0
#35-Develop a program that reads the length of three straight lines and tells the user whether or not they can form a
# triangle.
print('-=-' * 20)
print('               Triangle analyzer...')
print('-=-' * 20)
first_segment =  float(input('First segment:'))
second_segment = float(input('Second segment:'))
third_segment = float(input('Third segmant:'))
if first_segment < second_segment + third_segment and second_segment < first_segment + third_segment and third_segment < first_segment + second_segment:
    print('The segments above CAN form a triangle.')
else:
    print('The segments above CANNOT form a triangle.')


#Analisando Triângulo v1.0
#035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
primeiro = float(input('Digite o valor da primeira reta:'))
segundo = float(input('Digite o valor da segunda reta:'))
terceiro = float(input('Digite o valor da terceira reta:'))
if primeiro < segundo + terceiro and segundo < primeiro + terceiro and terceiro < segundo + primeiro:
    print('Você terá um triângulo.')
else:
    print('Você não terá um triângulo.')
    

#PT- Exercícios com uso de condicional.
#EN- Exercises using conditional.