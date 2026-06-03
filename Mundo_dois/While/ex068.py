from random import randint

valor = 0
while True:
    jogador = int(input("Digite um número: "))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in "PI":
        tipo = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
    print(f"Você jogou {jogador} e o computador {computador}. O total é {total}")
    if tipo == "P":
        if total % 2 == 0:
            print("Você Venceu!")
            valor += 1
        else:
            print("Você Perdeu!!")
            break
    elif tipo == "I":
        if total % 2 == 1:
            print("Você Venceu!")
            valor += 1
        else:
            print("Você Perdeu!!")
            break
    print("Vamos jogar novamente...")
print(f"Você venceu {valor} vezes.")