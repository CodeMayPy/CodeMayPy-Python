#Sine, Cosine and Tangent
#18- Write a program that reads any angle and displays on the screen the value of the sine, cosine and tangent of that angle.
import math
angle = float(input('Enter a value of an angle:'))
sine = math.sin(math.radians(angle))
print('The value of sine is {:.2f}.'.format(sine))
cosine = math.cos(math.radians(angle))
print('The value of cosine is {:.2f}'.format(cosine))
tangent = math.tan(math.radians(angle))
print('The value of tangent is {:.2f}'.format(tangent))


#Seno, Cosseno e Tangente
#18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''import math
angulo = float(input('Digite o valor de um ângulo qualquer:'))
print(f'Se o ângulo é {angulo}º, seu seno é {math.sin(math.radians(angulo)):.2f}, seu cosseno é {math.cos(math.radians(angulo)):.2f} e sua tangente é {math.tan(math.radians(angulo)):.2f}.')'''

#PT- Treinando o uso de modulos, no caso math.
#EN- Training the use of modules, in this case math
