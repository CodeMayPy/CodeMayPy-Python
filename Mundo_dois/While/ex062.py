#EN- Loop structure: While
#Super Arithmetic Progression v3.0
#62- Improve challenge 61 by asking the user if he wants to show some more terms. The program will exit when he says he
# wants to show 0 terms.
print("Arithmetic progression generator")
print("-=-" * 20)
first_term = int(input("Enter the first term:"))
reason = int(input("Enter the reason of the arithmetic progression:"))
term = first_term
counter = 1
total = 0
more = 10
while more != 0:
    total = more + total
    while counter <= total:
        print(f"{term}", end=' ')
        term += reason
        counter += 1
    print("Pause")
    more = int(input("How many more terms do you want to show?"))


#PT- Estrutura de repetição: While
#Super Progressão Aritmética v3.0
#62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará
# quando ele disser que quer mostrar 0 termos.