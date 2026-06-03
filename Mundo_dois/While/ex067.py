while True:
    numero = int(input("Digite um número para ver a tabuada: "))
    if numero < 0:
        break
    for contador in range(1, 11):
        print(f"{numero} X {contador} = {numero * contador}")