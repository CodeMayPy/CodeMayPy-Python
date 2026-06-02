#Majority Group
#54: Create a program that reads the birth year of seven people. At the end, show how many people have not yet
# the age of majority and how many are already adults.
from datetime import date
actual = date.today().year
higthest_total = smaller_total= 0
for people in range(1,8):
    birth = int(input(f"What year was {people}ª person born?"))
    age = actual - birth
    if age >= 21:
        higthest_total += 1
    else:
        smaller_total += 1
print(f"In total we had {higthest_total} people of legal age.")
print(f"and {smaller_total} people under age.")


#Grupo da Maioridade
#54- Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores.
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
    nas = int(input(f'Em que ano a {pessoas}ª pessoa nasceu?'))
    idade = atual - nas
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f' Ao todo tivemos {totmaior} pessoas maiores de idade.')
print(f'E {totmenor} pessoas menores de idade.')

#PT- Estruturas de repetições: For.
#EN- Loop structures: For.
