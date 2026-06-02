#Legs and Hypotenuse.
#17- Write a program that reads the length of the opposite and adjacent sides of a right triangle. Calculate and
# show the length of the hypotenuse.
import math
opposite_side = float(input('Enter the value of opposite side of triangle:'))
adjacent_leg = float(input('Enter the value of adjacente leg of triangle:'))
hypotenuse = math.hypot(opposite_side,adjacent_leg)
print('The value of opposite side is {} and the value of adjacent leg is {}, its hypotenuse is {:.2f}.'.format(opposite_side, adjacent_leg, hypotenuse))


# Catetos e Hipotenusa.
# 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule
# e mostre o comprimento da hipotenusa.
'''import math
cateto_oposto = float(input('Digite o valor do cateto oposto:'))
cateto_adjacente = float(input('Digite o valor do cateto adjacente:'))
print(f'O cateto oposto é {cateto_oposto} e o cateto adjacente é {cateto_adjacente} logo a hipotenusa é {math.hypot(cateto_oposto,cateto_adjacente):.2f}')'''

#PT- Treinando o uso de modulos, no caso math.
#EN- Training the use of modules, in this case math